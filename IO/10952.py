sum = []

while True:

    a,b = input().split(" ")
    if a == "0" and b == "0" :
        break
    c = int(a) + int(b)

    sum.append(c)


for i in sum :
     print(i)
