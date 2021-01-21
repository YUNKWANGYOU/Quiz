N,K = map(int,input().split(" "))

mod = 1000000000
table = [1]
table += [0]* N

for i in range(1,K+1) :
    for j in range(1,N+1):
        table[j] += table[j-1]

print(table[N]%mod)
