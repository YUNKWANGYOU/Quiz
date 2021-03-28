import sys

a = [sys.stdin.readline().rstrip('\n') for _ in range(2)]

x = 3600*int(a[0][0:2]) + 60*int(a[0][3:5]) + int(a[0][6:8])
y = 3600*int(a[1][0:2]) + 60*int(a[1][3:5]) + int(a[1][6:8])

tmp = y-x

b = (tmp//3600)%24
c = (tmp%3600)//60
d = tmp%3600%60
if tmp != 0:
    if b < 10 :
        print(0,end='')
        print(b,end='')
        print(':',end='')
    else :
        print(b,end='')
        print(':',end='')

    if c < 10 :
        print(0,end='')
        print(c,end='')
        print(':',end='')
    else :
        print(c,end='')
        print(':',end='')

    if d < 10 :
        print(0,end='')
        print(d,end='')
        print()
    else :
        print(d,end='')
        print()
else :
    print("24:00:00")
