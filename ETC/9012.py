import sys

t = int(sys.stdin.readline())

list = []

for _ in range(t) :

    list.append(sys.stdin.readline().rstrip('\n'))

for i in range(t) :
    cnt = 0

    for j in range(len(list[i])) :
        if list[i][j] == '(' :
            cnt+=1
        elif list[i][j] == ')' :
            cnt-=1
            if cnt < 0 :
                break

    if cnt == 0 :
        print("YES")
    else :
        print("NO")
