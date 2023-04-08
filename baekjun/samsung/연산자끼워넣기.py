# dfs가 가장빠름

from sys import stdin
input = stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

max_res = -1e10
min_res = 1e10
def div(a, b):
    if a < 0:
        return -(-a//b)
    else:
        return a//b
    
def dfs(num, p, m, t, d, idx):
    if idx == n - 1:
        global max_res, min_res
        if num > max_res:
            max_res = num
        if num < min_res:
            min_res = num
        return
    
    if p:
        dfs(num + num_list[idx + 1], p - 1 , m, t, d, idx + 1)
    if m:
        dfs(num - num_list[idx + 1], p , m - 1, t, d, idx + 1)
    if t:
        dfs(num * num_list[idx + 1], p , m, t - 1, d, idx + 1)
    if d:
        dfs(int(num /num_list[idx + 1]), p , m, t, d - 1, idx + 1)
    
dfs(num_list[0], op_list[0], op_list[1], op_list[2], op_list[3], 0)
print(max_res)
print(min_res)

# original -- permutations itertools 사용

import sys; input = sys.stdin.readline
from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    num_list = list(map(int, input().split()))
    n_plus, n_minus, n_multiple, n_divide = map(int, input().split())

    p = ['+'] * n_plus + ['-'] * n_minus + ['*'] * n_multiple + ['/'] * n_divide


    # 시간초과 원인 - permutation 기호는 문자가 같아도 다른 것으로 처리 되어, 중복을 제거해야 함
    permuted_operators = list(set(permutations(p)))

    candidates = []
    for perm in permuted_operators:
        ans = num_list[0]
        for idx in range(1, N):
            if perm[idx-1] == '+':
                ans += num_list[idx]
            elif perm[idx-1] == '*':
                ans *= num_list[idx]
            elif perm[idx-1] == '-':
                ans -= num_list[idx]
            elif perm[idx-1] == '/': #careful
                if ans < 0:
                    ans = (-1) * (((-1) * ans) // num_list[idx])
                else:
                    ans //= num_list[idx]

        candidates.append(ans)

    print(max(candidates))
    print(min(candidates))



