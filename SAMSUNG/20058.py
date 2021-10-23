import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def FireStorm():
    tmp = [[0]*sz for _ in range(sz)]

    for i in range(0,len_a,sz) :
        for j in range(0,len_a,sz):
            for x in range(len(tmp)) :
                for y in range(len(tmp)) :
                    tmp[y][x] = A[i+sz-1-x][j+y]
            for x in range(len(tmp)) :
                for y in range(len(tmp)) :
                    A[i+x][j+y] = tmp[x][y]

def ICE_count() :
    ICE = [[0]*len_a for _ in range(len_a)]

    for i in range(len_a) :
        for j in range(len_a):
            cnt = 0
            for d in range(4) :
                nx =i+dx[d]
                ny =j+dy[d]
                if 0<=nx<len_a and 0<=ny<len_a :
                    if A[nx][ny] > 0:
                        cnt+=1

            if cnt<3 :
                ICE[i][j] = 0
            else :
                ICE[i][j] = 1

    for i in range(len_a):
        for j in range(len_a) :
            if ICE[i][j] == 0 and A[i][j] > 0 :
                A[i][j] -= 1

def print_sum():
    print(sum(sum(A, [])))

def dfs(i,j) :
    res = 1
    A[i][j] = 0
    for d in range(4) :
        nx,ny = i+dx[d], j+dy[d]
        if 0<=nx<len_a and 0<=ny<len_a and A[nx][ny]:
            res += dfs(nx,ny)
    return res

def print_maxice():
    answer = 0
    for i in range(len_a) :
        for j in range(len_a) :
            if A[i][j] > 0 :
                answer = max(answer,dfs(i,j))
    print(answer)

if __name__ == '__main__':

    n,q = map(int,sys.stdin.readline().split(' '))
    A = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(pow(2,n))]
    L = list(map(int,sys.stdin.readline().split(' ')))
    len_a = len(A)
    for l in L :
        sz = pow(2,l)
        FireStorm()
        ICE_count()
    print_sum()
    print_maxice()
