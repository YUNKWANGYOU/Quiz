import sys
from itertools import combinations

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

asum = {}
bsum = {}

for i in range(n) :
    tmp = 0
    for j in range(i,n) :
        tmp += a[j]
        if asum.get(tmp) :
            asum[tmp] += 1
        else :
            asum[tmp] = 1

for i in range(m) :
    tmp = 0
    for j in range(i,m) :
        tmp += b[j]
        if bsum.get(tmp) :
            bsum[tmp] += 1
        else :
            bsum[tmp] = 1

res = 0
for _,i in enumerate(asum) :
    if bsum.get(t-i) :
        res+=(asum[i]*bsum[t-i])

print(res)
