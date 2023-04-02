# my first solution
# Things I learned
# enumerate(citations, start=1) -> returns tuple so, map(min, enumerate(citations, start=1)) returns tuple of min value

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        if idx+1 <= citation:
            answer = idx+1
    return answer

# other's solution

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer