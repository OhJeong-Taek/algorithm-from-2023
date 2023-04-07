# 틀린 부분 - 연속하는 숫자 모아뒀다 한꺼번에 터뜨려야함. - 문제를 잘 읽지 않으면 예외 케이스가 나옴

import sys; input = sys.stdin.readline

def printBoard(board):
    for r in range(N):
        for c in range(N):
            print(board[r][c], end=' ')
        print()
    print()

def updateBoard(board, marvelList):
    for r in range(N):
        for c in range(N):
            board[r][c] = 0

    r = c = N // 2
    marvelCnt = 0
    while r != 0 and c != 0:
        idx = 0
        for cnt in moveCnt:
            for _ in range(cnt):
                diff_r, diff_c = rc_dir[idx]
                r += diff_r
                c += diff_c
                board[r][c] = marvelList[marvelCnt] if marvelCnt < len(marvelList) else 0
                marvelCnt += 1
            idx = (idx + 1) % 4


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    D = []
    S = []
    for _ in range(M):
        d, s = map(int, input().split())
        D.append(d)
        S.append(s)

    rc_dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    moveCnt = []
    for idx in range(1, N):
        for _ in range(2):
            moveCnt.append(idx)
        if idx == N-1:
            moveCnt.append(idx)

    answer = 0
    for turn in range(M):
        marvelList = []
        # fill marvelList with board
        rc_idx_map = [[0]*N for _ in range(N)]
        rc_idx_map_cnt = 0
        r = c = N // 2
        while r!=0 and c!=0:
            idx = 0
            for cnt in moveCnt:
                for _ in range(cnt):
                    diff_r, diff_c = rc_dir[idx]
                    r += diff_r
                    c += diff_c
                    if board[r][c] > 0:
                        marvelList.append(board[r][c])
                    rc_idx_map[r][c] = rc_idx_map_cnt
                    rc_idx_map_cnt += 1
                idx = (idx + 1) % 4

        # use blizzard magic
        s_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        r = c = N//2
        for i in range(S[turn]):
            diff_r, diff_c = s_dir[D[turn]-1]
            r += diff_r
            c += diff_c
            remove_idx = rc_idx_map[r][c] - i
            marvelList = marvelList[:remove_idx] + marvelList[remove_idx + 1:]

        # successive explosion
        successive = True
        while successive:
            bef = -1
            cnt = 1
            start_idx = final_idx = -1

            bef_answer = answer
            explosion_candidates = []
            for idx, cur in enumerate(marvelList):
                if cur == bef:
                    cnt += 1
                    final_idx = idx
                    if idx == len(marvelList) - 1 and cnt >= 4:
                        explosion_candidates.append((start_idx, final_idx))
                else:
                    if cnt >= 4:
                        explosion_candidates.append((start_idx, final_idx))
                    start_idx = idx
                    cnt = 1
                bef = cur

            for i in range(len(explosion_candidates)-1, -1, -1):
                start_idx, final_idx = explosion_candidates[i]
                answer += marvelList[start_idx] * (final_idx-start_idx+1)
                marvelList = marvelList[:start_idx] + marvelList[final_idx+1:]

            successive = bef_answer != answer

        #marvelList change!
        marvelList = [x for x in marvelList if x != 0]
        if len(marvelList) > 0:
            new_marvel_list = []
            bef = marvelList[0]
            cnt = 1
            for idx in range(1, len(marvelList)):
                cur = marvelList[idx]
                if bef == cur:
                    cnt += 1
                else:
                    new_marvel_list.append(cnt)
                    new_marvel_list.append(bef)
                    cnt = 1

                if idx == len(marvelList) - 1:
                    new_marvel_list.append(cnt)
                    new_marvel_list.append(cur)
                    break
                bef = cur
            marvelList = new_marvel_list

        #updateBoard
        updateBoard(board, marvelList)


    print(answer)

