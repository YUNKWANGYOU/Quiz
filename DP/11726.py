a = int(input())

n = [0,1,2]

for i in range(0,1001) :
    n.append(n[i+1]+n[i+2])

print(n[a]%10007)
