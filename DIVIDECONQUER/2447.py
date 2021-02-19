import sys

n = int(sys.stdin.readline())
res = [['*' for _ in range(n)] for i in range(n)]

tmp = n
cnt=0
while tmp != 1 :
    tmp = tmp/3
    cnt+=1

for i in range(cnt) :
    idx = [j for j in range(n) if (j//3**i) % 3 == 1 ]
    for x in idx :
        for y in idx :
            res[x][y] = ' '

for i in range(n) :
    for j in range(n) :
        print(res[i][j],end='')
    print()
