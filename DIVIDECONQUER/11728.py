import sys

_,_ = map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split())) + list(map(int,sys.stdin.readline().split()))
a.sort()

for i in a :
    print(i,end = ' ')
print()
