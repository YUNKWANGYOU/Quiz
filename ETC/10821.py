
a = list(map(str,input().split(',')))

cnt = 0

num = ['0','1','2','3','4','5','6','7','8','9']

for i in a :
    if i[0] == '0':
        if i[1] :
            cnt+=1
        else :
            break

    for j in range(len(i)) :

        if i[j] in num :
            pass
        else :
            cnt+=1
            break

print(len(a)-cnt)
