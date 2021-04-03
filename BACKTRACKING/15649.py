import sys
from itertools import permutations

n,m = map(int,sys.stdin.readline().split())

a = [i for i in range(1,n+1)]

p = permutations(a,m)

for i in p :
    for j in i :
        print(j,end = ' ')
    print()
