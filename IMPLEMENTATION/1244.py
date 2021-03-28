import sys

n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))
num = int(sys.stdin.readline())
command = []

for i in range(num) :
    command.append(list(map(int,sys.stdin.readline().split())))

for i in range(num) :

    #Boys
    if command[i][0] == 1 :
        tmp = command[i][1]
        while 1 :
            if s[tmp-1] == 0 :
                s[tmp-1] = 1
            else :
                s[tmp-1] = 0

            tmp+=command[i][1]

            if tmp-1 >= n :
                break

    #Girls
    else :
        tmp = command[i][1]-1
        left = tmp - 1
        right = tmp + 1
        if s[tmp] == 1:
            s[tmp] = 0
        else :
            s[tmp] = 1

        while 1:
            if left < 0 or right >= n :
                break
            else :
                if s[left] == s[right] :
                    if s[left] == 0 :
                        s[left] = 1
                        s[right] = 1
                        left-=1
                        right+=1
                    else :
                        s[left] = 0
                        s[right] = 0
                        left-=1
                        right+=1
                else :
                    break

cnt=0
for i in s :
    print(i,end =' ')
    cnt+=1
    if cnt % 20 == 0 :
        print()
print()
