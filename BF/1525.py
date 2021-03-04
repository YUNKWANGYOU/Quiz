import sys
from collections import deque

def bfs():
    q = deque()
    q.append(a)
    dist[a] = 0

    while q :
        tmp = q.popleft()
        if tmp == 123456789 :
            return dist[tmp]

        s = str(tmp)
        #print(s)
        loc_9 = s.find('9')
        #print(loc_9)

        x,y = loc_9//3, loc_9%3

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny <3 :
                nk = nx*3 + ny
                ns = list(s)
                ns[loc_9],ns[nk] = ns[nk],ns[loc_9]
                nd = int(''.join(ns))
                if not dist.get(nd) :
                    dist[nd] = dist[tmp] + 1
                    q.append(nd)

    return -1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dist = dict()

a = ''
for i in range(3) :
    b = sys.stdin.readline().rstrip('\n')
    b = b.replace(' ','')
    a += b
a = int(a.replace('0','9'))

print(bfs())
