import sys; input = sys.stdin.readline

#board[r][c][0] shark num
#board[r][c][1] smell
#sharks[shark_num] = r, c, d

SHARKNUM = 0
SMELL = 1

def HandleInput():
    N, M, k = map(int, input().split())
    # M shark num, k smell num
    board = [[] for _ in range(N)]
    sharks = {}

    for r in range(N):
        row = list(map(int, input().split()))
        board[r] = [[x, k] if x > 0 else [x, 0] for x in row]
        for c in range(N):
            shark_num = board[r][c][SHARKNUM]
            if shark_num:
                sharks[shark_num] = (r, c, 0)


    for idx, elem in enumerate(list(map(int, input().split()))):
        r, c, d = sharks[idx+1]
        sharks[idx+1] = (r, c, elem)

    prefer_dir_list = []


    for i in range(M):
        prefer_board = []
        for j in range(4):
            prefer_board.append(list(map(int, input().split())))
        prefer_dir_list.append(prefer_board)

    return N, M, k, board, prefer_dir_list, sharks

def PrintBoard(smell = False):
    for r in range(N):
        for c in range(N):
            print(board[r][c][1] if smell else board[r][c][0], end=' ')
        print()
    print()

def SharkMove():
    # smell로 갈 수 없다.


    board_update_candidates = []
    for shark_num in sharks.keys():

        r, c, sd = sharks[shark_num]
        # current pos r, c
        # check move front
        p_d_l = prefer_dir_list[shark_num - 1][sd - 1]
        moved = False

        prev_pos_dir = (-1, -1, -1)
        for p_d in p_d_l:  # 우선순위 방향 체크
            dr, dc = DIR[p_d - 1]
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc][SMELL] == 0:  # 냄새가 없으면 움직인다.
                    moved = True
                    # board update를 for 문에서 할 것이 아니라 한꺼번에 다 한다.

                    board_update_candidates.append((nr, nc, shark_num))
                    sharks[shark_num] = (nr, nc, p_d)
                    break
                elif board[nr][nc][SHARKNUM] == shark_num and prev_pos_dir == (-1, -1, -1):
                    prev_pos_dir = (nr, nc, p_d)


        if not moved and prev_pos_dir != (-1, -1, -1):  # 전의 루트로 간다
            pr, pc, pd = prev_pos_dir
            board_update_candidates.append((pr, pc, shark_num))
            sharks[shark_num] = (pr, pc, pd)

    # 보드 한꺼번에 업데이트
    for candidate in board_update_candidates:
        r, c, val = candidate
        prev_val = board[r][c][SHARKNUM]

        # 새로 업데이트된 상어가 r,c에 있는 경우
        if board[r][c][SHARKNUM] > 0 and board[r][c][SMELL] == k+1:
            board[r][c][SHARKNUM] = min(prev_val, val)
            larger_val_shark = max(prev_val, val)
            sharks.pop(larger_val_shark)
        else:
            board[r][c][SHARKNUM] = val
        board[r][c][SMELL] = k+1

    # 냄새 다 줄이고, 냄새 없어지면 상어 num도 삭제
    for r in range(N):
        for c in range(N):
            if board[r][c][SMELL]:
                board[r][c][SMELL] -= 1
                if board[r][c][SMELL] == 0:
                    board[r][c][SHARKNUM] = 0  # 냄새 없어지면, 상어 루트 삭제


if __name__ == '__main__':

    N, M, k, board, prefer_dir_list, sharks = HandleInput()
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cnt = 0
    while len(sharks) > 1:
        SharkMove()
        cnt += 1
        if cnt > 1000:
            break

    print(cnt if cnt <= 1000 else -1)