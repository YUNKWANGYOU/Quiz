import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def FireStorm():
    tmp = [[0]*sz for _ in range(sz)]

    for i in range(0,pow(2,n),sz) :
        for j in range(0,pow(2,n),sz):
            for x in range(len(tmp)) :
                for y in range(len(tmp)) :
                    tmp[x][y] = A[i+y][j+sz-1-x]

            for x in range(len(tmp)) :
                for y in range(len(tmp)) :
                    A[i+x][j+y] = tmp[x][y]

    for a  in A :
        print(a)
    print()

def ICE_count() :
    ICE = [[0]*pow(2,n) for _ in range(pow(2,n))]

    for i in range(len(A)) :
        for j in range(len(A)):
            cnt = 0
            for d in range(4) :
                nx =i+dx[d]
                ny =j+dy[d]
                if 0<=nx<pow(2,n) and 0<=ny<pow(2,n) :
                    if A[nx][ny] > 0:
                        cnt+=1

            if cnt<3 :
                ICE[i][j] = 0
            else :
                ICE[i][j] = 1

    for i in range(len(A)):
        for j in range(len(A)) :
            if ICE[i][j] == 0 and A[i][j] > 0 :
                A[i][j] -= 1
    for a  in A :
        print(a)
    print()

def print_sum():
    sum = 0
    for i in A :
        for j in i :
            sum+=j
    print(sum)
if __name__ == '__main__':

    n,q = map(int,sys.stdin.readline().split(' '))
    A = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(pow(2,n))]
    L = list(map(int,sys.stdin.readline().split(' ')))

    for a in A :
        print(a)

    for l in L :

        sz = pow(2,l)
        FireStorm()
        ICE_count()
        print_sum()
        # print_maxice()
