import os, sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    N, K = map(int, f.readline().split())
    arr = [int(f.readline()) for _ in range(N)]
    
    ans = 0
    for val in reversed(arr):
        ans += K // val
        K %= val
        if K == 0:
            break 
    
    print(ans)