a = []

while 1 :
    try :
        b= input()
        if b=="":
            break
        else :
            a.append(b)
    except :
        break

for i in a :
    print(i)
