import sys

def backtracking(index,start,n,m):
    if index == m :
        for i in res :
            print(i,end =' ')
        print()

    for i in range(start,n) :
        if visited[i] == 0 :
            visited[i] = 1
            res.append(i+1)
            backtracking(index+1,i+1,n,m) #탐색 시작 (i+1부터 n까지만)
            visited[i] = 0 #탐색 완료
            res.pop()

n,m = map(int,sys.stdin.readline().split())

visited = [0] * n
res = []

backtracking(0,0,n,m)
