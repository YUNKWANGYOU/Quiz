a =  input()

for i in range(int(a)-1,0,-1) :
    for j in range(0,i) :
        print(" ",end = '')
    for j in range(0,1) :
        print("*",end = '')
    for j in range(0,int(a)-i-1):
        print(" ",end = '')
    for j in range(0,int(a)-i-2):
        print(" ",end = '')
    for j in range(0,1) :
        if i == int(a)-1:
            print("",end = '')
        else:
            print("*",end = '')

    print("")

for i in range(0,int(a)*2-1):
    print("*",end ='')

print('')
