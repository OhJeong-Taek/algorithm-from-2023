# 시간 소요 원인
# 1. dice move 할때, 좌표를 잘 못 바꿈 --> 그림을 그릴 것
# 2. score bfs, if not 0 <= r < N or not 0 <= c < N (M인데) 이라 함
# 3. 벽 만날 때 방향 바꾸는 것 고려안하고 짜고, 답 안나와서 수정 --> 애초에 설계할 때 빼먹지 않게 정리를 할 것
# 4. 그래도 그나마, 클래스로 다 구현을 해서, 나쁘지는 않은 것 같은데,
# 5. 계속 dfs 를 하는 것 보다는, dfs 값을 memo해두자: 2000s --> 48s 7둥
# 6  dfs to bfs

import sys; input = sys.stdin.readline

def score_dfs(visited, r, c, val, memo_candidates):
    global dfs_cnt

    if not 0 <= r < N or not 0 <= c < M:
        return

    if visited[r][c] or board[r][c] != val:
        return

    visited[r][c] = True
    if board[r][c] == val:
        memo_candidates.append((r,c))
        dfs_cnt += 1

    d_r = [1, 0, -1, 0]
    d_c = [0, 1, 0, -1]
    for _r, _c in zip(d_r, d_c):
        n_r = r + _r
        n_c = c + _c
        score_dfs(visited, n_r, n_c, val, memo_candidates)


class Dice:
    def __init__(self):
        self.front = 2
        self.top = 1
        self.back = 5
        self.bottom = 6
        self.left = 4
        self.right = 3
        self.r = 0
        self.c = 0
        self.move_dir = 0  # 0: right, 1: down 2: left 3: up  A>B number increase, A<B number decrease

    def move(self):
        if self.move_dir == 0:
            self.move_right()
        elif self.move_dir == 1:
            self.move_down()
        elif self.move_dir == 2:
            self.move_left()
        elif self.move_dir == 3:
            self.move_up()

    def rotate_cw(self):
        self.move_dir = (self.move_dir + 1) % 4

    def rotate_ccw(self):
        self.move_dir = (self.move_dir - 1) % 4

    def move_right(self):
        if self.c == M-1:
            self.move_left()
            return

        self.move_dir = 0
        self.c += 1
        tmp = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = self.top
        self.top = tmp

    def move_left(self):
        if self.c == 0:
            self.move_right()
            return

        self.move_dir = 2
        self.c -= 1

        tmp = self.left
        self.left = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = tmp

    def move_up(self):
        if self.r == 0:
            self.move_down()
            return

        self.move_dir = 3
        self.r -= 1
        tmp = self.front
        self.front = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = tmp


    def move_down(self):
        if self.r == N-1:
            self.move_up()
            return

        self.move_dir = 1
        self.r += 1
        tmp = self.back
        self.back = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = tmp

    def rc(self):
        return (self.r, self.c)


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*M for _ in range(N)]

dice = Dice()
answer = 0

for _ in range(K):
    # 처음 이동방향 동쪽
    dice.move()

    #이동된 좌표
    r, c = dice.rc()

    # 점수 획득
    visited = [[False] * M for _ in range(N)]   # visited clear for every K
    memo_candidates = []
    dfs_cnt = 0
    val = board[r][c]

    if memo[r][c] > 0:
        dfs_cnt = memo[r][c]
    else:
        score_dfs(visited, r, c, val, memo_candidates)

    answer += dfs_cnt * val

    for c_r, c_c in memo_candidates:
        memo[c_r][c_c] = dfs_cnt

    #이동 방향 결정
    if dice.bottom > val:
        dice.rotate_cw()
    elif dice.bottom < val:
        dice.rotate_ccw()


print(answer)

'''
from collections import deque


def score_bfs(r, c, val, memo_candidates):
    global bfs_cnt

    if not 0 <= r < N or not 0 <= c < M:
        return 0

    if board[r][c] != val:
        return 0

    queue = deque([(r, c)])
    visited = [[False] * M for _ in range(N)]
    visited[r][c] = True
    bfs_cnt = 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < N or not 0 <= nc < M or visited[nr][nc] or board[nr][nc] != val:
                continue
            visited[nr][nc] = True
            bfs_cnt += 1
            queue.append((nr, nc))
            memo_candidates.append((nr, nc))

    return bfs_cnt
'''

