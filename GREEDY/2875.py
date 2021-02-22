import sys

n,m,k = map(int,sys.stdin.readline().split())
cnt = 0
while k-n-m <= 0 and n >= 0 and m >= 0:
    n-=2
    m-=1
    cnt+=1

print(cnt-1)
