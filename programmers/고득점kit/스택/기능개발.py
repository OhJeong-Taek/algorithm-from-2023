# Original
import math
def solution(progresses, speeds):
    answer = []
    max = 0
    for idx, progress in enumerate(progresses):
        days = math.ceil((100 - progress) / speeds[idx])
        if days > max:
            max = days
            answer.append(1) 
        else:
            answer[-1] += 1
    return answer

#Things I learned through other's opinion
# 1. zip
# 2. not using math.ceil by negative number //


def solution(progresses, speeds):
    answer = []
    max = 0
    for progress, speed in zip(progresses, speeds):
        days = -((progress - 100) // speed)
        if days > max:
            max = days
            answer.append(1) 
        else:
            answer[-1] += 1
    return answer