# 1. hash_map.get()

def solution(phone_book):
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = True
    
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            prefix = phone_number[:i]
            if hash_map.get(prefix):
                return False
            
    return True