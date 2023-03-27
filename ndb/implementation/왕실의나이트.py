chessPos = input()

x = int(ord(chessPos[0])- ord('a')) + 1
y = int(chessPos[1])

moveSet = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1,2], [1, -2], [2, 1], [2, -1]]

count = 0
for move in moveSet:
    _x = move[0] + x
    _y = move[1] + y
    if 1 <= _x <= 8 and 1 <= _y <=8:
        count += 1
        
print(count)