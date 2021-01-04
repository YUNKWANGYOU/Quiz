n = int(input())
sum = []

for i in range(1,n+1) :
    a,b = input().split(" ")
    c = int(a) + int(b)
    sum.append(c)


for i in sum :
     print(i)
