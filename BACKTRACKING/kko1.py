import sys

card = list(map(int,sys.stdin.readline().split()))
want = list(map(int,sys.stdin.readline().split()))
d = dict()

for i in card :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

cnt = 0
for i in want :
    if i in d and d[i] != 0 :
        d[i]-=1
    else :
        cnt+=1

print(cnt)
