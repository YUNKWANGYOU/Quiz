import sys
sys.setrecursionlimit(2000)

def length(y,x,py,px,word) :
    if board[y+py][x+px] != word :
        return 0
    else:
        return length(y+py,x+px,py,px,word) + 1

n = int(sys.stdin.readline())
board = [['' for _ in range(19)] for _ in range(19)]
word = ''
wb = 0
flag = 0

for i in range(1,n+1) :
    x,y = map(int,sys.stdin.readline().split())

    if flag :
        continue

    if wb :
        word = 'w'
    else :
        word = 'b'

    board[x][y] = word

    cnt = length(y,x,-1,0,word) + length(y,x,1,0,word) + 1
    if cnt == 5 :
        flag = i

    cnt = length(y,x,0,-1,word) + length(y,x,0,1,word) + 1
    if cnt == 5 :
        flag = i

    cnt = length(y,x,-1,-1,word) + length(y,x,1,1,word) + 1
    if cnt == 5 :
        flag = i

    cnt = length(y,x,-1,1,word) + length(y,x,1,-1,word) + 1
    if cnt == 5 :
        flag = i

    if wb :
        wb = 0
    else :
        wb = 1

if flag :
    print(flag+1)
else :
    print(-1)
