import sys

def bfs(v) :
    queue = [v]
    check[v] = 1
    while queue :
        v = queue.pop(0)
        for i in range(1, n+1) :
            if check[i] == 0 and graph[v][i] == 1 :
                queue.append(i)
                check[i] = 1

n, m = map(int,sys.stdin.readline().split())

graph = [[0]*(n+1) for i in range(n+1)]
check = [0 for i in range(n+1)]

for i in range(m) :
    x,y  = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 0

for i in range(1,n+1) :
    if check[i] == 0 :
        bfs(i)
        cnt+=1

sys.stdout.write(str(cnt)+'\n')
