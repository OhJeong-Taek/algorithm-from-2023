N = int(input())
arr = list(input().split())

x, y = 1, 1

for data in arr:
    if data == 'R' and y < N:
        y += 1
    elif data == 'L' and y > 1:
        y -= 1
    elif data == 'U' and x > 1:
        x -= 1
    elif data == 'D' and x < N:
        x += 1

print(x, y)