import sys

n,k = map(int,sys.stdin.readline().split())

list = []

for _ in range(n) :
    list.append(int(sys.stdin.readline()))

i = n-1
cnt = 0
while k != 0 :
    if k < list[i]:
        i-=1
    elif k == list[i] :
        cnt+=1
        k = k - list[i]
    elif k > list[i] :
        k = k - list[i]
        cnt+=1


print(cnt)
