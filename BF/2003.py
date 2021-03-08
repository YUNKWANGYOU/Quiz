import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
cnt=0
for i in range(n) :
    tmp = 0
    for j in range(i, n) :
        tmp += a[j]
        if tmp == m:
            cnt+=1
            break
        elif tmp > m :
            break
print(cnt)
