#아직 못품

import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,r = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

while 1 :
    px,py = 0,0
