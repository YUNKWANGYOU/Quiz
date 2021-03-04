import sys

def dfs(x,y,idx) :
    if idx == len(sen) :
        return 1
    if check[x][y][idx] != -1 :
        return check[x][y][idx]

    check[x][y][idx] = 0

    for i in range(4) :
        tmpx,tmpy = x,y
        for _ in range(k) :
            nx = tmpx + dx[i]
            ny = tmpy + dy[i]
            if 0 <= nx < n and 0 <= ny < m  :
                if a[nx][ny] == sen[idx] :
                    check[x][y][idx] += dfs(nx,ny,idx+1)
                tmpx,tmpy = nx, ny

    return check[x][y][idx]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,m,k = map(int,sys.stdin.readline().split())
a = []
for _ in range(n) :
    a.append(sys.stdin.readline().rstrip('\n'))
sen = sys.stdin.readline().rstrip('\n')
check = [[[-1]*len(sen) for _ in range(m)] for _ in range(n)]
init = []

for i in range(n) :
    for j in range(m) :
        if a[i][j] == sen[0] :
            init.append([i,j])

res = 0

for i in range(len(init)) :
    x,y = init[i]
    res += dfs(x,y,1)

print(res)
