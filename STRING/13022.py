import sys

a = sys.stdin.readline().rstrip('\n')
flag = 0
i = 0
wolf = 0
while 1 :

    if wolf % 4 == 0 : # 'w'인지 판단
        if a[i] == 'w' :
            if a[i+1] =='w':
                i+=1
                pass
            elif a[i+1] == 'o':
                i+=1
                wolf+=1
            else :
                break
        else :
            break

    if wolf % 4 == 1:
        if a[i] == 'o' :
            if a[i+1] =='o':
                i+=1
                pass
            elif a[i+1] == 'l':
                i+=1
                wolf+=1
            else :
                break
        else :
            break

    if wolf % 4 == 2:
        if a[i] == 'l' :
            if a[i+1] =='l':
                i+=1
                pass
            elif a[i+1] == 'f':
                i+=1
                wolf+=1
            else :
                break
        else :
            break
    if wolf%4 ==3 :
        if a[i] == 'f' and i+1 == len(a):
            flag = 1
            break
        else :
            if a[i+1] == 'f':
                i+=1
                pass
            elif a[i+1] == 'w':
                i+=1
                wolf+=1
            else :
                break


print(flag)
