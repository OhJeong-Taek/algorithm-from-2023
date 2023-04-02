#THings to remember
#1. sort(key=lambda x: x[1])  # sort by second element of tuple
#2 all() function
#3. join() function
#4. str(int()) function

def solution(numbers):
    if all(num == 0 for num in numbers):
        return "0"

    def compare(x):
        return x*3

    # 문자열로 변환한 숫자들을 정렬하여 이어붙인 결과 반환
    numbers = list(map(str, numbers))
    numbers.sort(key=compare, reverse=True)
    return ''.join(numbers)


#Other's opinion
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
