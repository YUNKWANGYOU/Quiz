import sys
sys.setrecursionlimit(2000)

def dfs(v):
    dfs_check[v] = 1
    num = c[v]
    if dfs_check[num] == 0 :
        dfs(num)

t = int(sys.stdin.readline())

while t :
    n = int(sys.stdin.readline())
    c = [0] + list(map(int, sys.stdin.readline().split()))
    t-=1
    dfs_check = [0]*(n+1)

    sum = 0

    for i in range(1,n+1) :
        if dfs_check[i] == 0 :
            dfs(i)
            sum += 1

    print(sum)
