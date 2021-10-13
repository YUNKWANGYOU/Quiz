import sys
import copy
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(array,x,y) :
    global answer
    array = copy.deepcopy(array)
    print(answer,array)

def check_board(n) :
    for i in range(N) :
        for j in range(N) :
            if array[i][j] != 0 and array[i][j] < n :
                return True
    return False


if __name__ == '__main__' :

    # 입력한 수를 NxN 배열로 바꾸기
    N = int(sys.stdin.readline())
    array = []
    for i in range(N) :
        tmp = list(map(int,sys.stdin.readline().split()))
        array.append(tmp)

    # 아기 상어의 초기 위치
    x,y = -1,-1
    for i in range(N):
        for j in range(N) :
            if array[i][j] == 9 :
                x,y = i,j
                break

    answer = 0

    if check_board(array,2) :
        answer = bfs(array,x,y)
        print(answer)
    else :
        print(0)
