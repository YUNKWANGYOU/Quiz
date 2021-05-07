import sys

s = []
e = []
res = []
for i in range(3):
    a,b = map(str,sys.stdin.readline().split())
    s=list(map(int,a.split(':')))
    e=list(map(int,b.split(':')))
    cnt = 0

    while 1 :

        sum = int(s[2]/10) + s[2]%10 + int(s[1]/10) + s[1]%10 + int(s[0]/10) + s[0]%10
        if sum%3 == 0 :
            cnt+=1

        if s == e :
            break

        s[2]+=1
        if(s[2] == 60):
            s[2]=0
            s[1]+=1

        if(s[1] == 60) :
            s[1]=0
            s[0]+=1

        if(s[0] == 24):
            s[0]=0

    res.append(cnt)

for i in res:
    print(i)
