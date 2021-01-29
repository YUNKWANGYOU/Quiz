import sys

n,k = map(int,sys.stdin.readline().split())

group = [i for i in range(1,n+1)]

cur = k-1

print('<',end ='')
for i in range(n) :
    if len(group) != 1 :
        if len(group) > cur :
            print(group.pop(cur),end=', ')
            cur += k-1
        else :
            cur = cur % len(group)
            print(group.pop(cur),end=', ')
            cur+=k-1
    else :
        print(group.pop(),end = '>\n')
