def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    idx_list_dict = {}
    
    for idx, genre in enumerate(genres):
        genre_dict[genre] = genre_dict.get(genre, 0) + plays[idx]
        idx_list_dict.setdefault(genre,[]).append(idx)
        

    sorted_keys = sorted(genre_dict, key=genre_dict.get, reverse=True)

    for key in sorted_keys:
        key_idxes = idx_list_dict[key]
        sorted_idx = [i for i, val in sorted(enumerate([plays[i] for i in key_idxes]), key=lambda x: x[1], reverse=True)]
        res = [key_idxes[i] for i in sorted_idx][:2]
        answer.extend(res)
        
    return answer