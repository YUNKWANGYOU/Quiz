import sys

def dfs(start,tree,res) :
    for v,e in tree[start] :
        if res[v] == 0 :
            res[v] = res[start] + e
            dfs(v,tree,res)

n = int(sys.stdin.readline())
tree = [[]for _ in range(n+1)]
res_1 = [0 for _ in range(n+1)]
res_2 = [0 for _ in range(n+1)]

for _ in range(n) :
    edge = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(edge)//2) :
        tree[edge[0]].append([edge[2*i-1],edge[2*i]])

dfs(1,tree,res_1)
res_1[1] = 0

tmpmax = 0
tmpidx = 0

for i in range(len(res_1)) :
    if res_1[i] > tmpmax :
        tmpmax = res_1[i]
        tmpidx = i

dfs(tmpidx,tree,res_2)
res_2[tmpidx] = 0

print(max(res_2))
