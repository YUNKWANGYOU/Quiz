import sys

need = []

while 1 :
    tmp = list(map(int,sys.stdin.readline().split()))
    if tmp == [] :
        break
    else :

        need.append(tmp)

r = int(sys.stdin.readline())

res = [0 for _ in range(len(need[0]))]
d = dict()

for i in need :
    for j in range(len(i)) :
        if i[j] == 1 and j in d :
            d[j] += 1
        elif i[j] == 0 :
            pass
        else :
            d[j] = 1

d = sorted(d.items(),key=lambda x: -x[1])

print(d)

tmp = []

for i in range(r) :
    tmp.append(d[i][0])

print(tmp)

cnt = 0
for i in need :
    for j in range(len(tmp)) :
        i[tmp[j]] =
