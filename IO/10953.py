i = input()
d = []

for j in range(0,int(i)):
    a,b = input().split(",")
    c = int(a) + int(b)
    d.append(c)

for k in range(0,int(i)):
    print(d[k])
