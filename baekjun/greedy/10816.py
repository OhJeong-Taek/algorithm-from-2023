import os, sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    data = f.read().split()

points = []
for i in range(0, len(data), 2):
    x, y = int(data[i]), int(data[i+1])
    points.append((x, y))
    
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)
    # n = int(f.readline())
    # array = list(map(int, f.readline().input()))
    # m = int(f.readline())
    # candidates = list(map(int, f.readline().split()))
   


