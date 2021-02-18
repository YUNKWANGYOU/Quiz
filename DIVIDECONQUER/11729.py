import sys

def hanoi(n,first,second,third) :
    if n == 1 :
        print(first,third)
    else :
        hanoi(n-1,first,third,second)
        print(first,third)
        hanoi(n-1,second,first,third)

n = int(sys.stdin.readline())

cnt = 0

for i in range(n) :
    cnt = cnt*2+1

print(cnt)
hanoi(n,1,2,3)
