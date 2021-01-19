import numpy

a = int(input())
temp = int(numpy.sqrt(a))
cnt = 0
while 1 :

    if a > pow(temp,2) :
        
        a = a-pow(temp,2)
        cnt+=1
        if a == 1 :
            cnt+=1
            break
    else :
        temp = temp-1


print(cnt)
