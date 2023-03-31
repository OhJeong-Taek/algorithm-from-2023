from itertools import combinations
from functools import reduce
from collections import defaultdict

def solution(clothes):
    
    cloth_count = defaultdict(int)
    for cloth_set in clothes:
        cloth = cloth_set[1]
        cloth_count[cloth] += 1
    
    count_list = list(cloth_count.values())

    return reduce(lambda acc, val: acc*(val+1), count_list, 1) - 1