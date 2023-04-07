# fixed

import sys; input = sys.stdin.readline

def searchDiagonal(board, r, c):
    answer = 0
    if r-1 >=0 and c-1 >=0 and board[r-1][c-1] > 0:
        answer += 1
    if r-1 >= 0 and c+1 < N and board[r-1][c+1] > 0:
        answer += 1
    if r+1 < N and c-1 >=0 and board[r+1][c-1] > 0:
        answer += 1
    if r+1 < N and c+1 < N and board[r+1][c+1] > 0:
        answer += 1
    return answer

N, M = map(int, input().split())

board = [list(map(int, input().split())) for i in range(N)]
directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)] #(r,c)
d = []
s = []
for i in range(M):
    _d, _s = map(int, input().split())
    d.append(_d)
    s.append(_s)

clouds = {(N-1, 0): True, (N-1, 1): True, (N-2, 0): True, (N-2, 1): True}

for i in range(M):
    # cloud move

    dr, dc = directions[d[i]-1]
    new_clouds = []
    #rain
    for r,c in clouds:
        r = (r + dr * s[i]) % N
        c = (c + dc * s[i]) % N
        board[r][c] += 1
        new_clouds.append((r,c))
    clouds = dict.fromkeys(new_clouds, True)

    #diagonal
    for r,c in clouds:
        board[r][c] += searchDiagonal(board, r, c)


    #new clouds
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r,c) not in clouds:
                new_clouds.append((r,c))
                board[r][c] -= 2

    clouds = dict.fromkeys(new_clouds, True)

answer = 0
for r in range(N):
    for c in range(N):
        answer += board[r][c]

print(answer)
