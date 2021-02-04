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

i = 0

while 1 :
    try :
        if n%list[i] == 0 :
            n = int(n/list[i])
            print(list[i])
        elif n%list[i] != 0 :
            i = i + 1
    except :
        sys.stdout.write("소인수분해 할 수 없습니다.\n")

    if n == 1 :
        break
