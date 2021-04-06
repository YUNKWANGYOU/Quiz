import sys

def backtracking(index,n,m):
    if index == m :
        for i in res:
            print(i, end = ' ')
        print()
        return

    for i in range(1,n+1):
        res[index] = i
        backtracking(index+1,n,m)


n,m = map(int,sys.stdin.readline().split())
res = [0 for _ in range(m)]

backtracking(0,n,m)
