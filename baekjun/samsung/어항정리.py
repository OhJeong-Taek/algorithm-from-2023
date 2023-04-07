# 전반적으로 코드를 읽기 쉽게 짰다.
# pileOnFishBowls 규칙만 좀 이해하기 어려울 수도 있으나, cnt 가 1씩 올라갈때마다, pile(move)되어야 할 (r,c)를 계산해서 rotate 후 pile한다.
# while mr <= res: 인데 while mr < res: 로 해서, 예제 7,8이 틀렸으나 빠른 시간 내에 debugging 성공할 수 있었다.
# 어쨌든, 회전에 관한 문제이고, 코드를 step 별로 간결하게 썼던게, 빠른 시간 내에 풀 수 있었던 이유인 것 같다.

import sys; input = sys.stdin.readline

def solve():
    global board
    # step 1 - find min and plus one -  board[0]
    min_val = min(board[0])
    board[0] = [x + 1 if x == min_val else x for x in board[0]]

    # step 2 - 어항 위에 올리기
    pileOnFishBowls()

    # step 3 - distribute fish
    distributeFish()

    # step 4 - 바닥에 다시 놓기
    backToBottom()

    # step 5 - N/2 180도 회전
    rotate180()

    # step 6 - distribute fish
    distributeFish()

    # step 7 - 바닥에 다시 놓기
    backToBottom()

    return max(board[0]) - min(board[0])

def pileOnFishBowls():
    global board, N
    cnt = 2
    mc = cnt // 2
    mr = cnt - mc
    res = N - mr * mc

    while mr <= res:
        copyboard = [[0] * N for _ in range(N)]
        # rotate
        for r_i in range(mr):
            for c_i in range(mc):
                copyboard[mc - c_i][r_i] = board[r_i][c_i]

        # mc만큼 땡김
        for idx in range(res):
            copyboard[0][idx] = board[0][idx + mc]

        board = copyboard
        cnt += 1
        mc = cnt // 2
        mr = cnt - mc
        res = N - mr * mc



def distributeFish():
    global board, N
    visited_map = {}
    copyboard = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                        if (r, c) not in visited_map:
                            visited_map[(r, c)] = []

                        if (nr, nc) not in visited_map:
                            visited_map[nr, nc] = []

                        if (nr, nc) in visited_map[(r, c)] or (r, c) in visited_map[(nr, nc)]:
                            continue

                        visited_map[(r, c)].append((nr, nc))
                        visited_map[(nr, nc)].append((r, c))

                        diff = board[r][c] - board[nr][nc]

                        copyboard[r][c] -= int(diff/5)
                        copyboard[nr][nc] += int(diff/5)

    for r in range(N):
        for c in range(N):
            board[r][c] += copyboard[r][c]

    return

def backToBottom():
    global board, N
    copyboard = []
    for c in range(N):
        for r in range(N):
            if board[r][c]:
                copyboard.append(board[r][c])

    board = [[0]*N for _ in range(N)]
    board[0] = copyboard

def rotate180():
    global board, N
    r_num = 1
    c_num = N//2
    for _ in range(2):
        copyboard = [[0] * N for _ in range(N)]
        for r in range(r_num):
            for c in range(c_num):
                copyboard[r_num * 2 - 1 - r][c_num-1-c] = board[r][c]

        for r in range(r_num):
            for c in range(c_num):
                copyboard[r][c] = board[r][c + c_num]

        board = copyboard
        r_num *= 2
        c_num //= 2


def printBoard():
    global board
    for r in range(N - 1, -1, -1):
        for c in range(N):
            print(board[r][c], end=' ')
        print()
    print()

if __name__ == '__main__':
    N, K = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    board[0] = list(map(int, input().split()))

    ans = 1
    while solve() > K:
        ans += 1

    print(ans)

