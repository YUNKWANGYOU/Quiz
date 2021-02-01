import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

dq = deque([i for i in range(1,n+1)])

result = []

while dq :
    dq.rotate(-k+1)
    result.append(str(dq.popleft()))

sys.stdout.write("<" + ", ".join(result) + ">")
