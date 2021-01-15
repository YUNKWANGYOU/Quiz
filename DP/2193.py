a = int(input())

n = [0,1,1]

for i in range(3,91) :
    n.append(n[i-1]+n[i-2])

print(n[a])
