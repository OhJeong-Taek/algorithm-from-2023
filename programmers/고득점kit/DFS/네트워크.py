# 수정버전 
def DFS(computers, v, visited):
    if visited[v]:
        return
    
    visited[v] = 1
    for idx, val in enumerate(computers[v]):
        if idx != v and val == 1:
            DFS(computers, idx, visited)
        
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            DFS(computers, i, visited)
    
    return answer




#처음에 푼거
def DFS(computers, v, visited):
    if visited[v]:
        return
    
    visited[v] = 1
    for idx, val in enumerate(computers[v]):
        if idx != v and val == 1:
            DFS(computers, idx, visited)
        
def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    while sum(visited) < n:
        answer += 1
        min_idx = min((idx, val) for idx, val in enumerate(visited) if val == 0)[0]
        DFS(computers, min_idx, visited)
        
    
    return answer

