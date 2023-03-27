n=8	
m=4	
section=[2, 3, 6]

def solution(n, m, section):
    answer = 0
    while len(section) > 0:
        first = section[0]
        while len(section) > 0 and section[0] - first < m:
            section.pop(0)
        answer += 1
            
   
    return answer

solution(n,m,section)