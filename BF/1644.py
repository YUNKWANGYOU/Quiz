import sys
import math

n = int(sys.stdin.readline())

def prime(x):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

a = prime(n)

cnt = 0
for i in range(len(a)) :
    tmp = 0
    for j in range(i, len(a)) :
        tmp += a[j]
        if tmp == n:
            cnt+=1
            break
        elif tmp > n :
            break

print(cnt)
