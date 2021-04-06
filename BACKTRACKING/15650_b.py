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
            backtracking(index+1,i+1,n,m)
            visited[i] = 0
            res.pop()

n,m = map(int,sys.stdin.readline().split())

visited = [0] * n
res = []

backtracking(0,0,n,m)
