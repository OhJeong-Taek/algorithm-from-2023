### 시간 효율면 상위 50퍼에서  상위 5퍼로 올라간 점
'''
    for idx in range(len(robot)-2, -1, -1):
        robot[idx+1] = robot[idx]
        robot[idx] = 0 
    robot[-1] = 0  
    
    을 다음과 같이 바꾸었다....
    애초에 왜... 벨트는 그렇게하고? 

    위의 코드가 느린 이유는.... len(robot)같이 계산하는 부분과, robot[idx+1] = robot[idx] 같은 부분 때문인가... 
    robot = [0] + robot[:-1]
    robot[-1] = 0
'''


#### 약간의 수정본

import sys; input = sys.stdin.readline

def moveBelt():
    global belt, robot
    belt = [belt[-1]] + belt[:len(belt)-1]
    robot = [0] + robot[:-1]
    robot[-1] = 0

def robotMove():
    global belt, robot
    #내구성이 변한다
    for idx in range(len(robot)-2, -1, -1):
        if robot[idx+1] == 0 and robot[idx] > 0 and belt[idx+1] > 0: # 다음칸에 내구성이 있고, 로봇이 없을때
            robot[idx], robot[idx + 1] = 0, 1
            belt[idx + 1] -= 1  # 내구성은 하나 줄고

            if idx+1 == len(robot)-1:
                robot[idx + 1] = 0

def robotOnDesk():
    global belt, robot
    if belt[0]:
        belt[0] -= 1 # 내구성은 하나 줄고
        robot[0] = 1

def solve():
    moveBelt()
    robotMove()
    robotOnDesk()
    return belt.count(0)

if __name__ == '__main__':

    N, K = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0] * N
    ans = 1

    while solve() < K:
        ans += 1

    print(ans)


### original
import sys; input = sys.stdin.readline

def moveBelt():
    global belt, robot
    belt = [belt[-1]] + belt[:len(belt)-1]

    # robot move 내구성이 변할일은 없다.
    for idx in range(len(robot)-2, -1, -1):
        robot[idx+1] = robot[idx]
        robot[idx] = 0  # 이게 답 틀리던 원인 --> 금방 찾긴함,  한칸씩 옮기면 옮겨준 애 처리는 왜안함?
    robot[-1] = 0  # 마지막칸 처리

def robotMove():
    #내구성이 변한다
    for idx in range(len(robot)-2, -1, -1):
        if robot[idx+1] == 0 and robot[idx] > 0 and belt[idx+1] > 0: # 다음칸에 내구성이 있고, 로봇이 없을때
            robot[idx + 1] = 1
            robot[idx] = 0
            belt[idx + 1] -= 1  # 내구성은 하나 줄고

            if idx+1 == len(robot)-1:
                robot[idx + 1] = 0

def robotOnDesk():
    global belt, robot
    if belt[0]:
        belt[0] -= 1 # 내구성은 하나 줄고
        robot[0] = 1

def solve():
    moveBelt()
    robotMove()
    robotOnDesk()
    return sum(1 for x in belt if x == 0)

if __name__ == '__main__':

    N, K = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0] * N
    ans = 1

    while solve() < K:
        ans += 1

    print(ans)

