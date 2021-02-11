import sys
from collections import deque
############FUNCTION############
def bfs1(i,j,cnt) :
    q.append([i,j])
    c1[i][j] = cnt
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if glob[nx][ny] == 1 and c1[nx][ny] == 0 :
                    c1[nx][ny] = cnt
                    q.append([nx,ny])

def bfs2(t) :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if glob[nx][ny] == 1 and c1[nx][ny] != t :
                    return c2[x][y] -1
                if glob[nx][ny] == 0 and c2[nx][ny] == 0 :
                    c2[nx][ny] = c2[x][y] + 1
                    q.append([nx,ny])

############FUNCTION############

############DEFINE##############
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(sys.stdin.readline())
glob = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q, q2 = deque(), deque()
c1 = [[0]*n for _ in range(n)]
cnt = 1
############DEFINE##############

#############MAIN###############
#섬끼리 Grouping
for i in range(n) :
    for j in range(n) :
        if glob[i][j] == 1 and c1[i][j] == 0 :
            bfs1(i,j,cnt)
            cnt+=1
ans = sys.maxsize
#섬 크기를 늘려가며 가장 작은 숫자 구해버리기
for t in range(1,cnt) :
    q = deque()
    c2 = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if glob[i][j] == 1 and c1[i][j] == t :
                q.append([i,j])
                c2[i][j] = 1
    res = bfs2(t)
    ans = min(ans,res)
print(ans)
#############MAIN###############
