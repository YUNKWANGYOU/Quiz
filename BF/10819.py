import sys
from itertools import permutations

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
p = list(permutations(num))

sum = 0

for i in p :
    tmp = 0
    for j in range(n-1) :
        tmp += abs(i[j] - i[j+1])
    sum = max(tmp,sum)

print(sum)
