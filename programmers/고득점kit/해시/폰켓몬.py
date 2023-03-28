# 1. set(list) works
def solution(nums):
    return min(len(nums)//2, len(set(nums)))