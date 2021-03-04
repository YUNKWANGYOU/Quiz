from collections import deque
import sys

def bfs() :
    q.append(s-1)
    sum[s-1] = 1
    while q :
        stair = q.popleft()
        if stair+1 == g :
            print(sum[stair] - 1)
            return
        if stair + u < f and sum[stair+u] == 0 :
            q.append(stair+u)
            sum[stair+u]  = sum[stair] + 1
        if stair - d >= 0 and sum[stair-d] == 0 :
            q.append(stair-d)
            sum[stair-d]  = sum[stair] + 1

    print("use the stairs")

f,s,g,u,d = map(int,sys.stdin.readline().split())
sum = [0] * f # 누적된 경로의 개수를 세는 리스트
q = deque()
bfs()
