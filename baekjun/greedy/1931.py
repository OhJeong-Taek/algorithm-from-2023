N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    
points.sort(key=lambda x: (x[1], x[0]))

count = 0
last = 0
for point in points:
    if point[0] >= last:
        count += 1
        last = point[1]
        
print(count)
   
    
