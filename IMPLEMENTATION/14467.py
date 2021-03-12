import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
check = [-1]*11
cnt = 0
for i in a :
    if check[i[0]] == -1 :
        check[i[0]] = i[1]
    else :
        if check[i[0]] != i[1]:
            cnt+=1
            check[i[0]] = i[1]
        elif check[i[0]] == i[1] :
            pass

print(cnt)
