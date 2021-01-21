n = int(input())

tmp = []
for i in range(n) :
    tmp.append(int(input()))

pad = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,max(tmp)+1) :
    pad.append(pad[i-2] + pad[i-3])

for i in range(n) :
    print(pad[tmp[i]])
