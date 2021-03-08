import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]
res = 0

def dfs(x,y,cnt):
    global res
    res = max(res,cnt)

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and check[board[nx][ny]] == 0 :
            check[board[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            check[board[nx][ny]] = 0

r,c = map(int,sys.stdin.readline().split())
#알파벳을 숫자로 바꿔놓자
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
for i in board :
    print(i)
#알파벳 개수
check = [0]*26
check[board[0][0]] = 1
dfs(0,0,1)
print(res)
