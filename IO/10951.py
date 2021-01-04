sum = []

while True:
    try :
        a,b = input().split(" ")
    except :
        break

    c = int(a) + int(b)
    sum.append(c)


for i in sum :
     print(i)
