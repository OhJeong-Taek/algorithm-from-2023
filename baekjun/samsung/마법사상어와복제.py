# deepcopy 1.77s ->
# dfs인데, visited 방문 가능하고 (핵심), 방문한 곳은 더하지 않기...
# 
import sys; input = sys.stdin.readline

class Fish:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def move(self):
        global smell, shark, move_dir, N
        # 냄새, 상어, 격자
        nx = self.x + move_dir[self.d][0]
        ny = self.y + move_dir[self.d][1]
        nd = self.d
        # 격자, 상어, 냄새 구현해야함

        while not 0 <= nx < N or not 0 <= ny < N or (nx == shark.x and ny == shark.y) or smell[nx][ny] > 0:
            #방향 다 전환 해봐도, 안될 때
            nd = (nd - 1) % len(move_dir)
            if nd == self.d:
                return

            nx = self.x + move_dir[nd][0]
            ny = self.y + move_dir[nd][1]

        self.x = nx
        self.y = ny
        self.d = nd

class Shark:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.route = '999'
        self.max_num = 0
        
    def move(self):
            global move_dir, fishes, smell, fish_board
            self.DFS(self.x, self.y, '', 0)
            dir_str = self.route
            arr = [int(x)-1 for x in dir_str]
            m_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for idx in arr:
                self.x += m_dir[idx][0]
                self.y += m_dir[idx][1]

                # fish 죽이고, 냄새 남김
                if fish_board[self.x][self.y] > 0:
                    smell[self.x][self.y] = 3
                    fish_board[self.x][self.y] = 0

            fishes = [fish for fish in fishes if fish_board[fish.x][fish.y] > 0]
            self.route = '999'
            self.max_num = 0

    def DFS(self, x, y, s, num_fishes):
        if not 0 <= x < N or not 0 <= y < N:
            return

        if len(s) == 3:
            if num_fishes > self.max_num:
                self.max_num = num_fishes
                self.route = s
            elif num_fishes == self.max_num and s < self.route:
                self.route = s
            return

        for idx, (dx, dy) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    self.DFS(nx, ny, s + str(idx + 1), num_fishes)
                else:
                    visited[nx][ny] = True
                    self.DFS(nx, ny, s + str(idx + 1), num_fishes + fish_board[nx][ny])
                    visited[nx][ny] = False

        return

    def DFS2(self):
        stack = [(self.x, self.y, '', 0, [[False] * N for _ in range(N)])]

        max_num = 0
        dir_candidate = '999'
        while stack:
            x, y, s, num_fishes, visited = stack.pop()
            if not 0 <= x < N or not 0 <= y < N:
                continue

            if len(s) == 3:
                if num_fishes > max_num:
                    max_num = num_fishes
                    dir_candidate = s
                elif num_fishes == max_num and s < dir_candidate:
                    dir_candidate = s
                continue

            # 상 좌 하 우
            # 1 2 3 4
            for idx, (dx, dy) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    #visited[x][y] = True ### 틀렸던 곳 
                    if visited[nx][ny]:
                        stack.append((nx, ny, s + str(idx + 1), num_fishes, [[x for x in row] for row in visited]))
                    else:
                        visited[nx][ny] = True
                        stack.append((nx, ny, s + str(idx + 1), num_fishes + fish_board[nx][ny],
                                      [[x for x in row] for row in visited]))
                        visited[nx][ny] = False
                    #visited[x][y] = False ### 틀렸던 곳 
        return dir_candidate


def updateFishBoard(fish_board, fishes):
    for r in range(N):
        for c in range(N):
            fish_board[r][c] = 0

    for fish in fishes:
        fx, fy = fish.x, fish.y
        fish_board[fx][fy] += 1

def printfishes():
    for r in range(N):
        for c in range(N):
            print(fish_board[r][c], end=' ')
        print()
    print()


def printSmell():
    for r in range(N):
        for c in range(N):
            print(smell[r][c], end=' ')
        print()
    print()

def smellDiminish():
    for r in range(N):
        for c in range(N):
            if smell[r][c] > 0:
                smell[r][c] -= 1

if __name__ == '__main__':
    move_dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]   # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    N = 4
    # Input
    M, S = map(int, input().split())
    fishes = []
    smell = [[0] * N for _ in range(N)]
    fish_board = [[0] * N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    
    for i in range(M):
        fx, fy, d = map(int, input().split())
        fishes.append(Fish(fx-1, fy-1, d-1))

    sx, sy = map(int, input().split())
    shark = Shark(sx-1, sy-1)

    for _ in range(S):
        ### Copy Fish -- 1st step
        copied_fishes = []
        for fish in fishes:
            copied_fishes.append((fish.x, fish.y, fish.d))

        ### fish move one step
        for fish in fishes:
            fish.move()

        updateFishBoard(fish_board, fishes)

        ### shark move
        shark.move()
        updateFishBoard(fish_board, fishes)

        ### step 4
        smellDiminish()

        ### step 5
        for fx, fy, fd in copied_fishes:
            fishes.append(Fish(fx, fy, fd))

        updateFishBoard(fish_board, fishes)

    print(sum(sum(x) for x in fish_board))