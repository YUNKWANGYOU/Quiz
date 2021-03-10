import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append([0,0])
    check[0][0] = 0

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if check[nx][ny] == -1 :
                    if a[nx][ny] == 0 :
                        check[nx][ny] = check[x][y]
                        #미로에서 0인곳을 먼저 거치기위해 appendleft 를 이용
                        q.appendleft([nx,ny])
                    else :
                        check[nx][ny] = check[x][y] + 1
                        q.append([nx,ny])


m,n  = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(n)]
check = [[-1]*m for _ in range(n)]
bfs()
print(check[n-1][m-1])
