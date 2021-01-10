a =  input()

for i in range(0,int(a)) :
    for j in range(0,int(a)-i-1):
        print(" ",end = "")
    for j in range(0,i+1) :
        print("*",end = " ")
    print("")
