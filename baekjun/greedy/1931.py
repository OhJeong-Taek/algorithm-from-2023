import os, sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    N = int, f.readline()
    arr = [int(f.readline()) for _ in range(N)]