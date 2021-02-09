import sys

def dfs(v):
    check[v] = 1
    num = stu[v]
    if check[num] == 0 :
        dfs(num)

t = int(sys.stdin.readline())

while t :
    n = int(sys.stdin.readline())
    stu = [0] + list(map(int,sys.stdin.readline().split()))

    check = [0] * (n+1)

    for i in range(1,n+1) :
        if check[i] == 0 :
            num = i
            while check[i] == 0 :
                check[i] = num
                i = stu[i]
            while check[i] == num :
                check[i] = -1
                i = stu[i]
    t-=1
    print(n-check.count(-1))
