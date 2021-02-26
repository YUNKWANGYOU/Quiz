import sys
from collections import deque

#소수인 곳에 1을, 아닌 곳에 0을 채워 저장
def prime():
    for i in range(2,100) :
        if p_num[i] == 1 :
            for j in range(2*i,10000,i) :
                p_num[j] = 0

def bfs(a) :
    q.append(a)
    check[a] = 1
    while q :
        a = q.popleft()
        if a == b :
            print(check[a]-1)
            return
        for i in range(10) :
            if i != 0 :
                na = (a%1000) + i*1000
                if p_num[na] == 1 and check[na] == 0 :
                    check[na] = check[a] + 1
                    q.append(na)
            na = int(a/1000)*1000 + (a%100) + i*100
            if p_num[na] == 1 and check[na] == 0 :
                check[na] = check[a] + 1
                q.append(na)
            na = int(a/100)*100 + (a%10) + i*10
            if p_num[na] == 1 and check[na] == 0 :
                check[na] = check[a] + 1
                q.append(na)
            na = int(a/10)*10 + i
            if p_num[na] == 1 and check[na] == 0 :
                check[na] = check[a] + 1
                q.append(na)

n = int(sys.stdin.readline())
p_num = [1] * 10000
prime()

for _ in range(n) :
    q = deque()
    check = [0] * 10000
    a,b = map(int,sys.stdin.readline().split())
    bfs(a)
