def move_fish(board_fish):
    board_fish_new = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(8):
                if board_fish[i][j][k]:
                    move = False
                    nk = k
                    for _ in range(8):
                        ni,nj = i+di[nk],j+dj[nk]
                        if 0 <= ni < 4 and 0 <= nj < 4 and (ni,nj)!=(si,sj) and board_smell[ni][nj]==0:
                            move = True
                            break
                        nk = (nk-1)%8
                    if not move:
                        ni,nj = i,j
                    board_fish_new[ni][nj][nk] += board_fish[i][j][k]
    return board_fish_new

def dfs(i,j,path,cnt_tmp):
    if len(path) == 3:
        global cnt,dir_list
        if cnt < cnt_tmp:
            cnt = cnt_tmp
            dir_list = path
        return
    for idx in range(4):
        ni,nj = i+sdi[idx],j+sdj[idx]
        if 0 <= ni < 4 and 0 <= nj < 4:
            visited[ni][nj] += 1
            if visited[ni][nj] == 1:
                dfs(ni, nj, path+[idx], cnt_tmp+sum(board_fish[ni][nj]))
            else:
                dfs(ni, nj, path+[idx], cnt_tmp)
            visited[ni][nj] -= 1
        
di = [0,-1,-1,-1, 0,1,1,1]
dj = [-1,-1,0,1, 1,1,0,-1]
sdi = [-1,0,1,0] # 상좌하우 순으로 해야 사전순
sdj = [0,-1,0,1]

m,s = map(int,input().split())
board_fish = [[[0]*8 for _ in range(4)] for _ in range(4)]
board_smell = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    i,j,d = map(int,input().split())
    board_fish[i-1][j-1][d-1] += 1
si,sj = map(int,input().split())
si,sj = si-1,sj-1

while s>0:
    s -= 1
    # 1. 물고기 복사
    board_fish_copy = [[board_fish[i][j] for j in range(4)] for i in range(4)]
    # 2.모든 물고기 한칸 이동
    board_fish = move_fish(board_fish)
    # 3.상어가 연속 3칸 이동
    cnt,dir_list = -1, []
    visited = [[0]*4 for _ in range(4)]
    dfs(si,sj,[],0)
    # 4.두번 전 연습에서 생긴 물고기 냄새 삭제
    for i in range(4):
        for j in range(4):
            if board_smell[i][j] > 0:
                board_smell[i][j] -= 1
    for d in dir_list:
        si,sj = si+sdi[d],sj+sdj[d]
        if sum(board_fish[si][sj]):
            board_fish[si][sj] = [0]*8
            board_smell[si][sj] = 2
    # 5.물고기 복제
    for i in range(4):
        for j in range(4):
            for k in range(8):
                board_fish[i][j][k] += board_fish_copy[i][j][k]
                
ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(board_fish[i][j])
print(ans)