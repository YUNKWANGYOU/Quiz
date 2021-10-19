import sys
from collections import deque

if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split(' '))
    belt = deque(list(map(int,sys.stdin.readline().split(' '))))
    robot = deque([0]*n)

    answer = 0

    while belt.count(0) < k :
        belt.rotate(1)
        robot.rotate(1)
        robot[-1] = 0

        # 로봇이 있으면 벨트, 로봇 내구도 1씩 줄이면서옆으로 이동시켜줌
        if sum(robot) :
            for i in range(n-2,-1,-1) :
                if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                    robot[i+1]=1
                    robot[i]= 0
                    belt[i+1]-=1
            robot[-1]=0
        # 로봇이 없을 떄 첫 벨트에 로봇을 실어준다.
        if robot[0]== 0 and belt[0] >=  1 :
            robot[0] = 1
            belt[0] -= 1

        answer+=1

    print(answer)
