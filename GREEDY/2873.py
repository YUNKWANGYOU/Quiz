import sys

r,c = map(int,sys.stdin.readline().split())
loc = []
visit = [[0]*c for i in range(r)]
for _ in range(r) :
    loc.append(list(map(int,sys.stdin.readline().split())))

if r%2 == 1 :
    for _ in range(r//2) :
        for _ in range(c-1) :
            print('R',end = '')
        print('D',end = '')
        for _ in range(c-1) :
            print('L',end = '')
        print('D',end = '')
    for _ in range(c-1) :
        print('R',end = '')
elif c%2 == 1 :
    for _ in range(c//2) :
        for _ in range(r-1) :
            print('D',end = '')
        print('R',end = '')
        for _ in range(r-1) :
            print('U',end = '')
        print('R',end = '')
    for _ in range(r-1) :
        print('D',end = '')
elif r%2 == 0 and c%2 == 0 :
    tmp = 1000
    position = [-1,-1]
    for i in range(r):
        if i%2 == 0 :
            for j in range(1,c,2):
                if tmp > loc[i][j] :
                    tmp = loc[i][j]
                    position = [i,j]

        elif i%2 != 0 :
            for j in range(0,c,2) :
                if tmp > loc[i][j] :
                    tmp = loc[i][j]
                    position = [i,j]

    res = ('D'*(r-1)+'R'+'U'*(r-1)+'R')*(position[1]//2)
    x = 2*(position[1]//2)
    y=0
    x2 = x+1
    while x != x2 or y != r-1 :
        if x < x2 and [y,x2] != position :
            x+=1
            res += 'R'
        elif x == x2 and [y,x2-1] != position:
            x-=1
            res+='L'
        if y != r-1 :
            y+=1
            res+='D'

    res += ('R' + 'U'*(r-1) + 'R' + 'D'*(r-1))*((c-position[1]-1)//2)

    print(res)
