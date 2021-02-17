import sys

def paper(N):
    while 1 :
        if N == 1 :



N = int(sys.stdin.readline())

matrix = []
check = [[0 for _ in range(N)]for _ in range(N)]
#cnt1 : -1, cnt2 : 0 , cnt3 : 1
cnt1,cnt2,cnt3 = 0,0,0

for _ in range(N) :
    matrix.append(list(map(int,sys.stdin.readline().split())))
