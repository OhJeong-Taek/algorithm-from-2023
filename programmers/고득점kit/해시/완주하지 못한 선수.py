# hash 숫자 더했다가, 빼기

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
        
    for com in completion:
        temp -= hash(com)
        
    answer = dic[temp]

    return answer
