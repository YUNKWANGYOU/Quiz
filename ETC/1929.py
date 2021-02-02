import sys
import math

n = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))

cnt = 0

def prime(a) :
    if a == 1 :
        return 0
    elif a == 2 :
        return 1
    for i in range(2,a) :
        if a%i == 0 :
            return 0
    return 1

for i in num :
    if prime(i) :
        cnt+=1

print(cnt)
