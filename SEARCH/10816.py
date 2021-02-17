import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in card :
    try :
        dic[i] += 1
    except :
        dic[i] = 1

for i in check :
    try :
        print(dic[i], end = " ")
    except :
        print(0, end = " ")

print()
