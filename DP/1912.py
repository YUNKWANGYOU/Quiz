n = int(input())
a = list(map(int,input().split(" ")))

sum = []
sum.append(a[0])

for i in range(n-1) :
    sum.append(max(sum[i] + a[i+1],a[i+1]))

print(max(sum))
