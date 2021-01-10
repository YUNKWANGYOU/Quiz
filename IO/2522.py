a =  input()

for i in range(int(a),0,-1) :
    for j in range(0,i-1) :
        print(" ",end = '')
    for j in range(0,int(a)-i+1) :
        print("*",end = '')

    print("")

for i in range(1,int(a)) :
    for j in range(0,i) :
        print(" ",end = '')
    for j in range(0,int(a)-i) :
        print("*",end = '')

    print("")
