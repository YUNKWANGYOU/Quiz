import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs() :
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and  0 <= ny < h and box[nx][ny] == 0 :
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])

queue = deque()
h,w = map(int,sys.stdin.readline().split())
box = [list(map(int,sys.stdin.readline().split())) for i in range(w)]

for i in range(w) :
    for j in range(h) :
        if box[i][j] == 1 :
            queue.append([i,j])

bfs()

m = []
flag = 0

for i in box :
    m.append(max(i))
    if 0 in i :
        sys.stdout.write('-1\n')
        flag = 1
        break

if flag == 0 :
    sys.stdout.write(str(max(m)-1) + '\n')
