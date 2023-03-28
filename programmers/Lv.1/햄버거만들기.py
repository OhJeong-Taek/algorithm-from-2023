#del 1.ingredient[i:i+4]
# 2. ingredient = ingredient[:a] + ingredient[b:] 는 메모리할당량을 많이 잡게 된다.
def solution(ingredient):
    answer = 0
    i = 0
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1,2,3,1]:
            del ingredient[i:i+4]
            answer += 1
            i -= 3
        else:
            i += 1
    return answer
