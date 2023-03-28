def solution(answers):
    answer = []
    candidate_1 = [1,2,3,4,5]
    candidate_2 = [2,1,2,3,2,4,2,5]
    candidate_3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0,0]
    
    for idx, answer in enumerate(answers):
        if candidate_1[idx%len(candidate_1)] == answer:
            score[1] += 1
        if candidate_2[idx%len(candidate_2)] == answer:
            score[2] += 1
        if candidate_3[idx%len(candidate_3)] == answer:
            score[3] += 1
    
    max_val = max(score)
    if max_val == 0:
        return []
    else:
        return [idx for idx, val in enumerate(score) if val == max_val]
    