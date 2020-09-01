i = input()
d = []

for j in range(0,int(i)):
    a,b = input().split()
    d.append([])
    d[j].append(int(a))
    d[j].append(int(b))

for k in range(0,int(i)):
    print("Case #{}: {} + {} =".format(k+1,d[k][0],d[k][1]),d[k][0]+d[k][1])
