import sys
import math

n,m = map(int,sys.stdin.readline().split())

cnt = 0

def prime(a) :
    if a == 1 :
        return 0
    elif a == 2 :
        return 1
    for i in range(2,int(math.sqrt(a))+1) :
        if a%i == 0 :
            return 0
    return 1

for i in range(n,m+1) :
    if prime(i) :
        print(i)
