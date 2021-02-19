import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

def bubble() :
    global A
    cnt = 0
    for i in range(len(A)-1,-1,-1):
        for j in range(i) :
            if A[j] > A[j+1] :
                cnt+=1
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp

    return cnt

print(bubble())
