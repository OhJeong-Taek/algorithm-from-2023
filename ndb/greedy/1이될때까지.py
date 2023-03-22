import sys, os

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    N, K = map(int, f.readline().split())
    cnt = 0
    while N > 1:
        if N % K == 0:
            N //= K
        else:
            N -= 1
        cnt += 1
    print(cnt)
        