import os, sys

def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array)-1
    
    while left<=right:
        mid = (left+right)//2 
        val = array[mid]
        
        if val > target:
            right = mid - 1
        elif val < target:
            left = mid + 1 
        else:
            return 1
    return 0

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().split()))
    array.sort()
    m = int(f.readline())
    queries = list(map(int, f.readline().split()))
    
    for x in queries:
        print(binarySearch(array, x))