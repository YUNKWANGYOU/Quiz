a = int(input())

n = [0,9]

for i in range(1,101) :
    n.append(n[i]*2-i)

print(n[a]%1000000000)
