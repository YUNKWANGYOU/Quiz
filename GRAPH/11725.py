import sys
sys.setrecursionlimit(10**9)

def dfs(start,tree,dfs_check) :
    for i in tree[start] :
        if dfs_check[i] == 0 :
            dfs_check[i] = start
            dfs(i,tree,dfs_check)

n = int(sys.stdin.readline())
tree = [[]for _ in range(n+1)]

for _ in range(n-1) :
    parent, child = map(int,sys.stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)

dfs_check = [0 for _ in range(n+1)]

dfs(1,tree,dfs_check)

for i in range(2,n+1) :
    sys.stdout.write(str(dfs_check[i]) + '\n')
