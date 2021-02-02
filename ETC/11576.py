import sys

A,B = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

dec = list(map(int,sys.stdin.readline().split()))

sum = 0

for i in range(m) :
    sum += pow(A,i) * dec[m-i-1]

list = []

while 1 :
    x = int(sum/B)
    y = sum%B
    list.append(y)
    if x == 0 :
        break
    sum = x

for i in range(len(list)):
    print(list[len(list)-i-1],end = ' ')

print("")
