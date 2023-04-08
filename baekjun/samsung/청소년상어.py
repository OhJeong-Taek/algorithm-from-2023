# 제일... 간결
# 삼중 array로 해결하자

import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)


# my original answer
import sys; sys.stdin.readline
from copy import deepcopy

def printBoard(board):
    for r in range(4):
        for c in range(4):
            print(board[r][c], end=' ')
        print()
    print()

def handle_input():
    fish_board = [[0] * 4 for _ in range(4)]
    dir_board = [[0] * 4 for _ in range(4)]
    fish_pos = {}

    # input
    for r in range(4):
        for idx, elem in enumerate(list(map(int, input().split()))):
            if idx % 2 == 0:
                fish_board[r][idx // 2] = elem
                fish_pos[elem] = (r, idx // 2)
            else:
                dir_board[r][idx // 2] = elem - 1

    return fish_board, dir_board, fish_pos

def sharkMove(r, c, fb, db, fp):
    if not 0 <= r < 4 or not 0 <= c < 4:
        return 0

    num = fb[r][c]
    if num in fp:
        fp.pop(num) # dead
    fb[r][c] = 0

    fishMove(r,c, fb, db, fp)
    return num  # num of fish killed

def DFS(sr, sc, cnt, fb, db, fp):
    global max_cnt, DIR
    if not (0 <= sr < 4 and 0 <= sc < 4):
        return


    num = sharkMove(sr, sc, fb, db, fp)
    if num == 0:
        return

    cnt += num

    max_cnt = max(max_cnt, cnt)

    dr, dc = DIR[db[sr][sc]]
    for i in range(3):
        nr, nc = sr + dr*(i+1), sc+dc*(i+1)
        if not 0 <= nr < 4 or not 0 <= nc < 4:
            return
        DFS(nr, nc, cnt, deepcopy(fb), deepcopy(db), deepcopy(fp))

    return

def fishMove(sr, sc, fb, db, fp):
    for key in sorted(fp.keys()):
        fr, fc = fp[key]
        fd = db[fr][fc]

        for idx in range(8):
            changed_d = (fd + idx) % 8
            dr, dc = DIR[changed_d]
            nr, nc = fr+dr, fc+dc

            #움직 일 수 있을때만 자리 바꿈
            #class 로 구현하는게 나았을 거 같다... 괜히 다르게 풀어본다고... 아니면 3차원 array로 풀던가... 2개 관리하는건 까다롭고, 실수여지...

            if not (nr == sr and nc == sc) and 0 <= nr < 4 and 0 <= nc < 4:
                #교체

                np_fish_num = fb[nr][nc]
                fb[nr][nc] = fb[fr][fc]
                fb[fr][fc] = np_fish_num

                db[fr][fc] = db[nr][nc]
                db[nr][nc] = changed_d

                if np_fish_num:
                    fp[np_fish_num] = (fr, fc)
                fp[key] = (nr, nc)
                break

    return

if __name__ == '__main__':
    max_cnt = -1e10
    DIR = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] #BUG!! 찾기 힘듬.... 하 r,c 헷갈려서 잘못 작성하지 말자 (0,1) 을 (1,0) 으로 잘못 씀
    shark = [0, 0, -1]
    fish_board, dir_board, fish_pos = handle_input()


    DFS(0, 0, 0, fish_board, dir_board, fish_pos)
    print(max_cnt)

# 1. 상어 0.0 물고기 먹음
# 2.  물고기 같은 번호 없음, 16 index, 방향 8가지
# 3. index 낮은 거 부터 이동
# 3 물고기 한칸 이동, 상어, 공간경계 x 45 ccw 회전 if 이동불가 --> 이동 x
# 4.  물고기가 다른 물고기가 있는 칸 이동시. 서로의 위치 변경?

# 5. 상어 이동
# 6 여러칸 이동, 물고기 있는 칸, 물고기 죽음, 물고기의 방향이 상어의 방향,
# 7. 진행 중 물고기 안먹음
# 8. 상어 이동 할 공간 없으면 집

# 이 과정 반복