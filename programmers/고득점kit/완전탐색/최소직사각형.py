#배운점: python newbie - grammar
#1. larger, smaller = max(pair[0], pair[1]), min(pair[0], pair[1])

def solution(sizes):
    max_larger = 0
    max_smaller = 0
    
    for pair in sizes:
        larger, smaller = max(pair[0], pair[1]), min(pair[0], pair[1])
        max_larger = larger if larger > max_larger else max_larger
        max_smaller = smaller if smaller > max_smaller else max_smaller
        
    return max_larger*max_smaller

