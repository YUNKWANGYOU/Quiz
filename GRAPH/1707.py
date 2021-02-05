import sys

def dfs(v,c) :
    check[v] = c
    for i in range(1,n+1) :
        if check[i] == 0 and graph[v][i] == 1 :
            dfs(i,-c)

T = int(sys.stdin.readline())

for _ in range(T) :
    n,m = map(int,sys.stdin.readline().split())
    check = [0 for i in range(n+1)]
    graph = [[0]*(n+1) for i in range(n+1)]
    cnt = 0

    for i in range(m) :
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
        graph[y][x] = 1

    dfs(1,1)

    flag = 0

    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if graph[i][j] :
                if check[i] == check[j] :
                    flag = 0
                    break
                else :
                    flag = 1

    if flag :
        sys.stdout.write("YES\n")
    else :
        sys.stdout.write("NO\n")
