#input
# 4 4 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16


import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,r = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

print(n,m,r)
print(a)

#solv.1
#배열은 그대로 냅두고 
# while 1 :
#     px,py = 0,0
