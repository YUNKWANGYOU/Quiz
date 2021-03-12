import sys
from collections import deque

q = deque()
sen = sys.stdin.readline()
for i in sen :
    q.append(i)
a = [[0 for _ in range(5)] for _ in range(500)]
cnt = 0
i = 0
while q :
    x = q.popleft()
    if x == 'q' :
        a[i][0] = 1
