import sys

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
snail = [[0]*n for _ in range(n)]

value = 1
direction = 1
cnt = 1
xtemp = int((n-1)//2)
ytemp = int((n-1)//2)
snail[xtemp][ytemp] = 1

while value != n*n :
    if direction == 1:
        for i in range(cnt) :
            value+=1
            xtemp-=1
            snail[xtemp][ytemp] = value
            if value == n*n :
                break
        direction = 2
    elif direction == 2 :
        for i in range(cnt) :
            value+=1
            ytemp+=1
            snail[xtemp][ytemp] = value
            if value == n*n :
                break
        cnt+=1
        direction = 3
    elif direction == 3 :
        for i in range(cnt) :
            value+=1
            xtemp+=1
            snail[xtemp][ytemp] = value
            if value == n*n :
                break
        direction = 4
    elif direction == 4 :
        for i in range(cnt) :
            value+=1
            ytemp-=1
            snail[xtemp][ytemp] = value
            if value == n*n :
                break
        cnt+=1
        direction = 1
x,y=-1,-1
for i in range(n):
    for j in range(n):
        print(snail[i][j], end = ' ')
        if snail[i][j] == num :
            x,y = i+1,j+1
    print()
print(x,y)
