import sys

def backtracking(index,n,m):
    if index == m :
        for i in res :
            print(i,end =' ')
        print()

        return

    for i in range(len(visited)) :
        res.append(i+1)
        backtracking(index+1,n,m) #탐색 시작
        res.pop()

n,m = map(int,sys.stdin.readline().split())

visited = [0] * n
res = []

backtracking(0,n,m)
