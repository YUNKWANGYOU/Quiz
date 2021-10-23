import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution():
    print(n,m,board)

    for i in range(n):
        for j in range(n) :
            
if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split(' '))
    board = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]

    solution()
