import sys
from collections import deque

def bfs(v) :
    q.append(v)
    group[v] = 1
    while q :
        v = q.popleft()
        for i in graph[v] :
            if group[i] == 0 :
                group[i] = -1*group[v]
                q.append(i)
            elif group[i] == group[v] :
                return 0
    return 1

T = int(sys.stdin.readline())

for _ in range(T) :
    v,e = map(int,sys.stdin.readline().split())
    graph = [[]for _ in range(v+1)]
    group = [0 for _ in range(v+1)]

    q = deque()

    for _ in range(e) :
        x,y = map(int,sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    res = 1

    for i in range(1,v+1) :
        if group[i] == 0 :
            res = bfs(i)
            if res == 0 :
                break

    if res == 1 :
        sys.stdout.write("YES\n")
    else :
        sys.stdout.write("NO\n")
