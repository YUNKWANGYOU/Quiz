import sys
from itertools import combinations

while 1:
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 0:
        break
    a.remove(a[0])
    nCr = list(combinations(a,6))
    for i in nCr:
        for j in i :
            print(j,end = ' ')
        print()
    print()
