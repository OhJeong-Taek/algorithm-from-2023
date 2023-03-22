import sys, os

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    6
    largest = 0
    for _ in range(N):
        arr = list(map(int, f.readline().split()))
        minVal = min(arr)
        if largest < minVal:
            largest = minVal
        
    print(largest)