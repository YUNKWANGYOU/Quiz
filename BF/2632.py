import sys

order = int(sys.stdin.readline())
m,n = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(m)]
b = [int(sys.stdin.readline()) for _ in range(n)]

l_sum,r_sum = [0]*2000001, [0]*2000001
l_sum[0] = 1
r_sum[0] = 1

for i in range(m) :
    s = 0
    for j in range(m) :
        s+=a[(i+j)%m]
        if s > order :
            break
        else :
            l_sum[s] += 1

for i in range(n) :
    s = 0
    for j in range(n) :
        s+=b[(i+j)%n]
        if s > order :
            break
        else :
            r_sum[s] += 1

l_sum[sum(a)] = 1
r_sum[sum(b)] = 1

res = 0

for i in range(order+1):
    res += (l_sum[i]*r_sum[order-i])
print(res)
