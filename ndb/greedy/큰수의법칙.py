import os, sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    N, M, K = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
    
    arr.sort()
    
    first = arr[N-1]
    second = arr[N-2]
    
    ans = 0
    for i in range(1,M+1):
        ans += first if i % (K+1) != 0 else second
    print(ans)

    







