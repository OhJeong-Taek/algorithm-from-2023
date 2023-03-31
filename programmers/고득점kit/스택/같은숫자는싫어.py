# my answer
def solution(arr):
    answer = []
    bef = ''
    for elem in arr:
        if bef != elem:
            answer.append(elem)
        bef = elem
    return answer

# other's answer
def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
    