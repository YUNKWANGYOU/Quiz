import sys
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Fish:
    def __init__(self,x,y,dist) :
        self.x = x
        self.y = y
        self.dist = dist

def solution(start) :

    visit = [[False]*n for _ in range(n)]
    dq  = deque([start])
    visit[start.y][start.x] = True
    size,time,eat = 2,0,0


    while True :
        fish_arr = []
        while dq :
            cur = dq.popleft()

            # 현재 아기상어가 먹을 수 있는 물고리를 fish_arr배열에 넣음
            if 0 < board[cur.y][cur.x] < size :
                fish_arr.append(cur)
            # 아기 상어가 현재 시점에서 갈 수 있는 방향을 모두 담음
            for i in range(4) :
                ny,nx = cur.y  + dy[i], cur.x + dx[i]
                if 0 <= ny < n and 0 <= nx < n :
                    next = Fish(nx,ny,cur.dist+1)
                    if board[ny][nx] <= size and not visit[ny][nx] :
                        dq.append(next)
                        visit[ny][nx] = True

        fish_arr.sort(key = lambda f : (f.dist,f.y,f.x))

        visit = [[False]*n for _ in range(n)]

        if fish_arr :
            tmp = fish_arr[0]
            board[tmp.y][tmp.x] = 0
            eat+=1
            time = tmp.dist
            dq.append(tmp)
            visit[tmp.y][tmp.x] = True
        else :
            ret = time
            break

        if eat == size :
            size+=1
            eat = 0

    return ret


if __name__ == '__main__' :

    # 입력한 수를 NxN 배열로 바꾸기
    n = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]

    # 아기 상어의 초기 위치
    cur1 = None
    for i in range(n):
        for j in range(n) :
            if board[i][j] == 9 :
                cur1 = Fish(j,i,0)
                board[i][j] = 0
                break

    print(solution(cur1))
