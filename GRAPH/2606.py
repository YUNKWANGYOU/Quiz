import sys

def dfs(vertex) :
    check[vertex] = 1
    for i in range(n):
        if graph[vertex][i] == 1 and check[i] == 0 :
            dfs(i)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]
check = [0 for i in range(n)]

for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

dfs(0)
cnt=0
for i in range(1,n) :
    if check[i] == 1 :
        cnt+=1

print(cnt)
