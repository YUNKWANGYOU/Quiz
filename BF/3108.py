import sys
from collections import deque

def bfs(x,y) :
    q.append([x,y])
    check[x][y] = 1

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000 :
                if a[nx][ny] == 1 and check[nx][ny] != 1:
                    check[nx][ny] = 1
                    q.append([nx,ny])
dx = [-1,1,0,0]
dy = [0,0,1,-1]
n = int(sys.stdin.readline())
a = [[0]*2001 for _ in range(2001)]
check = [[0]*2001 for _ in range(2001)]
init = []
for _ in range(n) :
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    x1+=500
    x1*=2
    y1+=500
    y1*=2
    x2+=500
    x2*=2
    y2+=500
    y2*=2

    init.append([x1,y1])

    for i in range(x1, x2+1) :
        if i == x1 or i == x2 :
            for j in range(y1, y2+1) :
                a[i][j] = 1
        else :
            a[i][y1] = 1
            a[i][y2] = 1

q = deque()
res = 0
for i in range(len(init)) :
    x,y = init[i]
    if check[x][y] == 0 :
        bfs(x,y)
        res += 1

if a[1000][1000] == 1 :
    res -= 1

print(res)
