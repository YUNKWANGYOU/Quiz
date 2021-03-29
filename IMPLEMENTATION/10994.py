import sys

def dot(n,idx) :
    if n == 1 :
        star[idx][idx] = '*'
        return

    tmp = 4*n-3

    for i in range(idx,tmp+idx) :
        star[idx][i] = '*'
        star[idx+tmp-1][i] = '*'
        star[i][idx] = '*'
        star[i][idx+tmp-1] = '*'

    return dot(n-1,idx+2)

n = int(sys.stdin.readline())
w = n*4-3
star = [[' ' for _ in range(w)] for _ in range(w)]

dot(n,0)

for i in range(w):
    for j in range(w):
        print(star[i][j],end='')
    print()
