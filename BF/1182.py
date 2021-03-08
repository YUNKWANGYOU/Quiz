import sys
from itertools import combinations

n,s = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
res = []

for i in range(0,len(a)+1):
    c = combinations(a,i)
    res.extend(c)
cnt = 0

for i in res :
    if sum(i) == s :
        cnt+=1
        
if s == 0 :
    print(cnt-1)
else :
    print(cnt)
