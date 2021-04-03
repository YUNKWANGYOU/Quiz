import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

a = [i for i in range(1,n+1)]

c = combinations(a,m)

for i in c :
    for j in i :
        print(j,end = ' ')
    print()
