import os, sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().input()))
    m = int(f.readline())
    candidates = list(map(int, f.readline().split()))
   
#memoization

