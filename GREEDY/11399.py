import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

for i in range(n) :
    if i != 0 :
        a[i] += a[i-1]

print(sum(a))
