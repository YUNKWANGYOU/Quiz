import sys
from collections import deque

def bfs():
    q = deque()
    q.append([a,""])
    while q :
        num, cnt = q.popleft()
        # D : n을 두배로 바꿈
        D = (num*2) % 10000
        if D == b :
            return cnt+'D'
        elif check[D] == 0 :
            check[D] = 1
            q.append([D, cnt + 'D'])

        # S : n-1을 레지스터에 저장
        if num == 0 :
            S = 9999
        else :
            S = num-1

        if S == b :
            return cnt+'S'
        elif check[S] == 0 :
            check[S] = 1
            q.append([S,cnt+'S'])

        # L : 각 자릿수를 왼편으로 회전
        L = int(num/1000 + num%1000*10)
        if L == b :
            return cnt+'L'
        elif check[L] == 0 :
            check[L] = 1
            q.append([L,cnt+'L'])

        # R : 각 자릿수를 오른편으로 회전
        R = int(num//10 + num%10*1000)
        if R == b :
            return cnt+'R'
        elif check[R] == 0 :
            check[R] = 1
            q.append([R,cnt+'R'])

n = int(sys.stdin.readline())
for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    check = [0] * 10000
    print(bfs())
