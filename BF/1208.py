import sys
from collections import defaultdict

def dfs(idx,e_idx,sum,direction):
    global res

    if idx == e_idx :
        if direction == "right" :
            res+=left[s-sum]
        else :
            left[sum]+=1
        return

    dfs(idx+1,e_idx,sum,direction)
    dfs(idx+1,e_idx,sum + a[idx],direction)

res = 0
n,s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
left = defaultdict(int)
dfs(0,n//2,0,"left")
dfs(n//2,n,0,"right")

if s == 0 :
    print(res-1)
else :
    print(res)
