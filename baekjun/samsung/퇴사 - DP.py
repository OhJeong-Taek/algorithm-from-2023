#solution 1 - DP

import sys; input = sys.stdin.readline
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for _ in range(4):
        N = int(input())
        T = []
        P = []
        DP = [0] * (N+1)
        for _ in range(N):
            x,y = map(int, input().split())
            T.append(x)
            P.append(y)

        max_sum = 0
        for i in range(N-1, -1, -1):
            if i + T[i] <= N:
                max_sum = max(P[i] + DP[i + T[i]], max_sum)
            DP[i] = max_sum

        print(max_sum)