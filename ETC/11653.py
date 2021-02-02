import sys
import math

n = int(sys.stdin.readline())

def prime(a) :
    if a == 1 :
        return 0
    elif a == 2 :
        return 1
    for i in range(2,int(math.sqrt(a))+1) :
        if a%i == 0 :
            return 0
    return 1

list = []

for i in range(1,n+1) :
    if prime(i) :
        list.append(i)

print(list)

while 1 :
    i = 0
    try :
        if n%list[i] == 0 :
            n = n/list[i]
            print(list[i])
        elif n == 1 :
            break
        else :
            i+=1
    except :
        print(n)
