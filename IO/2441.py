a =  input()

for i in range(0,int(a)) :
    for j in range(0,i) :
        print(" ",end = '')
    for j in range(0,int(a)-i) :
        print("*",end = '')

    print("")
