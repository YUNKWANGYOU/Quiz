import sys
import math

list = []

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

while 1 :
    list.append(int(sys.stdin.readline()))
    if list[len(list)-1] == 0:
        list.pop()
        break

for i in range(len(list)) :
    flag = 0
    for j in range(2,list[i]) :
        if prime(j) :
            if prime(list[i] - j) :
                print(list[i],'=',j,'+',list[i]-j)
                flag = 1
                break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")
