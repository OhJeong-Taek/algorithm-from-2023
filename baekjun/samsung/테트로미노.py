# 파이썬 내장함수인 input보다 빠르게 값을 입력받기 위해 sys.stdin.readline을 사용하였습니다.
import sys; input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max_sum = 0

def dfs(x, y, total, depth):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, total + board[nx][ny], depth + 1)
            visited[nx][ny] = False

def t_shape(x, y):
    global max_sum
    if x + 2 < n and y + 1 < m:
        max_sum = max(max_sum, board[x][y] + board[x+1][y] + board[x+2][y] + board[x+1][y+1])
    if x + 2 < n and y - 1 >= 0:
        max_sum = max(max_sum, board[x][y] + board[x+1][y] + board[x+2][y] + board[x+1][y-1])
    if y + 2 < m and x + 1 < n:
        max_sum = max(max_sum, board[x][y] + board[x][y+1] + board[x][y+2] + board[x+1][y+1])
    if y - 2 >= 0 and x + 1 < n:
        max_sum = max(max_sum, board[x][y] + board[x][y-1] + board[x][y-2] + board[x+1][y-1])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        t_shape(i, j)

print(max_sum)



'''
#Fixed
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 모든 테트로미노 모양에 대한 좌표 리스트
tetrominoes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], # -
    [(0, 0), (1, 0), (2, 0), (3, 0)], # l
    [(0, 0), (0, 1), (1, 0), (1, 1)], # ㅁ
    [(0, 0), (1, 0), (2, 0), (2, 1)], # ㄴ
    [(0, 0), (1, 0), (2, 0), (2, -1)], # ㄴ 반대
    [(0, 0), (0, 1), (0, 2), (1, 2)], #ㄱ
    [(0, 0), (0, 1), (0, 2), (-1, 2)], #ㄱ 반대
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], # ㄴ
    [(0, 0), (1, 0), (2, 0), (2, -1)], # ㄴ 
    [(0, 0), (1, 0), (1, -1), (2, -1)], #ㄹ
    [(0, 0), (1, 0), (1, -1), (2, -1)], #ㄹ 반대
    [(0, 0), (0, 1), (-1, 1), (-1, 2)], #ㄹ
    [(0, 0), (0, 1), (1, 1), (1, 2)], #ㄹ
    [(0, 0), (0, 1), (0, 2), (1, 1)], #T
    [(0, 0), (0, 1), (0, 2), (-1, 1)], #T
    [(0, 0), (1, 0), (2, 0), (1, 1)], #T
    [(0, 0), (1, 0), (2, 0), (1, -1)], #T
]

max_sum = 0
for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            total = 0
            for dx, dy in tetromino:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    total += board[nx][ny]
                else:
                    break
            max_sum = max(max_sum, total)

print(max_sum)

'''



#Original
'''
def DFS(array, visited, x,y,level, overall, max_num):
    xAlpha = [1, -1, 0, 0]
    yAlpha = [0, 0, 1, -1]
    if not 0<=x<len(array[0]) or not 0<=y<len(array) or visited[y][x]:
        return
    
    visited[y][x] = True  
    cur = overall + array[y][x]
      
    if level == 4:
        max_num[0] = max(cur, max_num[0])
        return
    
    for i in range(4):
        DFS(array, visited, x+xAlpha[i], y+yAlpha[i], level+1, cur, max_num)
        visited[y][x] = False
    
    
N, M = map(int, input().split())
array = [list(map(int,input().split())) for i in range(N)]

max_num = [0]
visited = [[False] * M for i in range(N)]

for y in range(N):
    for x in range(M):
        DFS(array, visited, x, y, 1, 0, max_num)        
        visited[y][x] = False
        
print(max_num[0])
'''
