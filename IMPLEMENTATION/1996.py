import sys

num = ['1','2','3','4','5','6','7','8','9']
n = int(sys.stdin.readline())

a = [list(map(str,sys.stdin.readline().rstrip('\n'))) for _ in range(n)]
res = [[ 0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if a[i][j] in num :
            try :
                res[i+1][j] += int(a[i][j])
            except :
                pass
            try :
                res[i-1-n][j] += int(a[i][j])
            except :
                pass
            try :
                res[i][j+1] += int(a[i][j])
            except :
                pass
            try :
                res[i][j-1-n] += int(a[i][j])
            except :
                pass
            try :
                res[i+1][j+1] += int(a[i][j])
            except :
                pass
            try :
                res[i+1][j-1-n] += int(a[i][j])
            except :
                pass
            try :
                res[i-1-n][j+1] += int(a[i][j])
            except :
                pass
            try :
                res[i-1-n][j-1-n] += int(a[i][j])
            except :
                pass

for i in range(n) :
    for j in range(n) :
        if a[i][j] in num :
            res[i][j] = -1

for i in res :
    for j in i :
        if j == -1:
            print('*',end='')
        elif j > 9 :
            print('M',end='')
        else :
            print(j,end='')
    print()
