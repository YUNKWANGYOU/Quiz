import sys
e,s,m = map(int,sys.stdin.readline().split())

while 1 :
    if e == s and s == m :
        print(e)
        break

    if min(e,s,m) == e :
        e+=15
    elif min(e,s,m) == s :
        s+=28
    elif min(e,s,m) == m :
        m+=19
