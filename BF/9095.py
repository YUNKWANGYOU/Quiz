n = [0,1,2,4]
for i in range(0,1001) :
    n.append(n[i+1]+n[i+2]+n[i+3])

N = int(input())
list = []
for i in range(0,N) :
    list.append(int(input()))

for i in range(0,N) :
    print(n[list[i]])
