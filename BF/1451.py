import sys

#input
n, m = map(int,sys.stdin.readline().split())
rect = []
for i in range(n) :
    rect.append(list(map(int,sys.stdin.readline().rstrip('\n'))))

tmp = 0

#|||
for i in range(1,m-1) :
    for j in range(i+1,m) :
        r1 = sum(rect[a][b] for a in range(n) for b in range(i))
        r2 = sum(rect[a][b] for a in range(n) for b in range(i,j))
        r3 = sum(rect[a][b] for a in range(n) for b in range(j,m))
        tmp = max(tmp,r1*r2*r3)

#ㅡㅡ
#ㅡㅡ
#ㅡㅡ
for i in range(1,n-1) :
    for j in range(i+1,n) :
        r1 = sum(rect[a][b] for a in range(i) for b in range(m))
        r2 = sum(rect[a][b] for a in range(i,j) for b in range(m))
        r3 = sum(rect[a][b] for a in range(j,n) for b in range(m))
        tmp = max(tmp,r1*r2*r3)

#ㅡㅡ
#| |
for i in range(1,n) :
    for j in range(1,m) :
        r1 = sum(rect[a][b] for a in range(i) for b in range(m))
        r2 = sum(rect[a][b] for a in range(i,n) for b in range(j))
        r3 = sum(rect[a][b] for a in range(i,n) for b in range(j,m))
        tmp = max(tmp,r1*r2*r3)

#| |
#ㅡㅡ
for i in range(1,n) :
    for j in range(1,m) :
        r1 = sum(rect[a][b] for a in range(i) for b in range(j))
        r2 = sum(rect[a][b] for a in range(i) for b in range(j,m))
        r3 = sum(rect[a][b] for a in range(i,n) for b in range(m))
        tmp = max(tmp,r1*r2*r3)

#|ㅡ
#|ㅡ
for i in range(1,n) :
    for j in range(1,m) :
        r1 = sum(rect[a][b] for a in range(i) for b in range(j,m))
        r2 = sum(rect[a][b] for a in range(i,n) for b in range(j,m))
        r3 = sum(rect[a][b] for a in range(n) for b in range(j))
        tmp = max(tmp,r1*r2*r3)

#ㅡ|
#ㅡ|
for i in range(1,n) :
    for j in range(1,m) :
        r1 = sum(rect[a][b] for a in range(n) for b in range(j,m))
        r2 = sum(rect[a][b] for a in range(i) for b in range(j))
        r3 = sum(rect[a][b] for a in range(i,n) for b in range(j))
        tmp = max(tmp,r1*r2*r3)

print(tmp)
