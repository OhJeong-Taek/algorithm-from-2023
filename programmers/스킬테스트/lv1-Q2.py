def solution(dartResult):
    answer = 0
    cur,bef = -1,-1
    special_ch = ['*', '#']
    score_ch = ['D', 'T']

    ans_list = []
    exception = False
    for idx, x in enumerate(dartResult):
        if x.isdigit():
            if dartResult[idx+1] == '0':
                ans_list.append(10)
                exception = True
            else:
                if not exception:
                    ans_list.append(int(x))
                exception = False

        if x == 'D':
            ans_list[-1] **= 2
        elif x == 'T':
            ans_list[-1] **= 3
        elif x == '*':
            ans_list[-1] *= 2
            if len(ans_list) >= 2:
                ans_list[-2] *= 2
        elif x == '#': 
            ans_list[-1] *= -1

    answer = sum(ans_list)
    return answer