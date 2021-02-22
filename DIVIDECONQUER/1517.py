import sys
sys.setrecursionlimit(10**9)

def merge(start,end) :
    global swap, A
    size = end - start
    mid = (start+end)//2

    if size<=1:
        return

    #divide
    merge(start,mid)
    merge(mid,end)

    #merge
    B = []
    idx1, idx2 = start,mid
    cnt = 0

    while idx1 < mid and idx2 < end :
        if A[idx1] > A[idx2] :
            B.append(A[idx2])
            idx2 += 1
            cnt += 1
        else :
            B.append(A[idx1])
            idx1 += 1
            swap += cnt

    while idx1 < mid :
        B.append(A[idx1])
        idx1+=1
        swap += cnt
    while idx2 < mid :
        B.append(A[idx2])
        idx2+=1

    for i in range(len(B)) :
        A[start+i] = B[i]

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
swap = 0
merge(0,N)
print(swap)
