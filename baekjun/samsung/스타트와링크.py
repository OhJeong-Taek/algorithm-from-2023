# 그냥 콤비네이션 두번 돌리면 되는 문제였는 줄... 그렇게 해도 되지만... 
# 아래 사람은 콤비네이션 한번 돌리고, 시간을 한 50배 아꼈다....
# # zip(*graph): graph의 각 열 
# 이런 문법도 있지만, 문법보다, 조금 더 효율적인 방법을 생각해보길...

import sys; sys.stdin.readline
from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    indexes = [x for x in range(N)]

    ans = 1e10
    for start_comb in combinations(indexes, N//2):
        start = 0
        link = 0
        link_comb = [x for x in indexes if x not in start_comb]

        for i, j in combinations(start_comb, 2):
            start += board[i][j]
            start += board[j][i]

        for i, j in combinations(link_comb, 2):
            link += board[i][j]
            link += board[j][i]


        ans = min(ans, abs(start-link))

    print(ans)

# 와.. 어의가 없네.. 어떻게 이렇게 풀었지..?

    # https://www.acmicpc.net/problem/14889
    import sys
    from itertools import combinations

    input = sys.stdin.readline


    def init():
        totalnum = int(input())
        stat_graph = [list(map(int, input().split())) for _ in range(totalnum)]

        return [totalnum, stat_graph]


    def run():
        totalnum, stat_graph = init()
        rows_sum = [sum(row) for row in stat_graph]
        cols_sum = [sum(col) for col in zip(*stat_graph)]  # zip(*graph): graph의 각 열
        stat_per_member = [i + j for i, j in zip(rows_sum, cols_sum)]
        total_stat = sum(rows_sum)

        min_score = total_stat
        for stat in combinations(stat_per_member, totalnum // 2):
            val = abs(total_stat - sum(stat))
            if val < min_score:
                min_score = val
        print(min_score)


    run()