import sys

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for i in range(n)]

cnt = 0
villa = []

def dfs(x,y) :
    global cnt
    a[x][y] = '0'
    cnt+=1

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n :
            continue
        if a[nx][ny] == '1' :
            dfs(nx,ny)

for i in range(n) :
    for j in range(n) :
        if a[i][j] == '1' :
            cnt = 0
            dfs(i,j)
            villa.append(cnt)

print(len(villa))
villa.sort()
for i in range(len(villa)) :
    print(villa[i])
