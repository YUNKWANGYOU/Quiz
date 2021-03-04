import sys
from collections import deque

def checkappend(x,y):
    if check[x][y] != 1 :
        check[x][y] = 1
        q.append([x,y])

def bfs() :
    q.append([0,0])
    check[0][0] = 1

    while q :
        a1,b1 = q.popleft()
        c1 = c-a1-b1

        if a1 == 0 :
            res.append(c1)

        if b1 + a1 < b : #a->b
            checkappend(0,b1+a1)
        else :
            checkappend(a1+b1-b,b)

        if c1 + a1 < c : #a->c
            checkappend(0,b1)
        else :
            checkappend(a1+c1-c,b1)

        if b1 + c1 < c : #b->c
            checkappend(a1,0)
        else :
            checkappend(a1,b1+c1-c)

        if b1 + a1 < a : #b->a
            checkappend(b1+a1,0)
        else :
            checkappend(a,b1+a1-a)

        if c1 + a1 < a : #c->a
            checkappend(c1+a1,b1)
        else :
            checkappend(a,b1)

        if c1 + b1 < b : #c->b
            checkappend(a1,c1+b1)
        else :
            checkappend(a1,b)

a,b,c = map(int,sys.stdin.readline().split())
q = deque()
check = [[0]*201 for i in range(201)]
res = []
bfs()
res.sort()

print(' '.join(map(str,res)))
