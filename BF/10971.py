import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
p = permutations(list(i for i in range(n)))

res = 10**9
def router(i) :
    global a,n
    tmp = 0
    for j in range(n-1) :
        if a[i[j]][i[j+1]] != 0 :
            tmp += a[i[j]][i[j+1]]
        else :
            return -1
    if a[i[-1]][i[0]] == 0 :
        return -1
    else :
        tmp += a[i[-1]][i[0]]

    return tmp
    
for i in p :
    tmpres = router(i)
    if tmpres != -1 :
        res = min(res,tmpres)
print(res)
