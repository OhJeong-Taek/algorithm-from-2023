import sys; input = sys.stdin.readline

def DFS(day, acc):
    global max_num

    if day >= N or day + T[day] > N:
        return

    acc += P[day]
    max_num = max(acc, max_num)

    for i in range(5):
        DFS(day + T[day] + i, acc)

if __name__ == '__main__':
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        x,y = map(int, input().split())
        T.append(x)
        P.append(y)

    max_num = 0

    for i in range(N):
        DFS(i, 0)

    print(max_num)