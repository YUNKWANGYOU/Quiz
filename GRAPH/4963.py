import sys

dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

def bfs(x,y) :
    a[x][y] = 0
    queue = [[x,y]]

    while queue :
        nx, ny = queue[0][0],queue[0][1]
        del queue[0]
        for i in range(8) :
            X = nx + dx[i]
            Y = ny + dy[i]
            if 0 <= X < n_y and 0 <= Y < n_x and a[X][Y] == 1:
                a[X][Y] = 0
                queue.append([X, Y])


while 1:
    cnt = 0
    villa = []

    n_x,n_y = map(int,sys.stdin.readline().split())

    if n_x == 0 or n_y == 0 :
        break

    a = [list(map(int,sys.stdin.readline().split())) for i in range(n_y)]

    for i in range(n_y) :
        for j in range(n_x) :
            if a[i][j] == 1 :
                bfs(i,j)
                cnt+=1

    print(cnt)
