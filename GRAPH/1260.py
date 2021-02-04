import sys

def dfs(v):
    print(v, end = ' ')
    dfs_check[v] = 1
    for i in range(1,n+1) :
        if graph[v][i] == 1 and dfs_check[i] == 0 :
            dfs(i)

def bfs(v):
    queue = [v]
    bfs_check[v] = 1

    while queue :
        v = queue[0]
        print(v, end = ' ')
        del queue[0]
        for i in range(1,n+1) :
            if bfs_check[i] == 0 and graph[v][i] == 1 :
                queue.append(i)
                bfs_check[i] = 1

n, m, v = map(int,sys.stdin.readline().split())

graph = [[0]*(n+1) for i in range(n+1)]

dfs_check = [0 for i in range(n+1)]
bfs_check = [0 for i in range(n+1)]

for i in range(m) :
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
print()
bfs(v)
print()
