import sys

a = ''

list_1 = ['a','e','i','o','u']
list_2 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

while 1 :
    flag = 1
    a = sys.stdin.readline().rstrip('\n')
    if a == 'end':
        break
    #1
    cnt=0
    for i in a :
        if i in list_1:
            cnt += 1
    if cnt == 0 :
        flag = 0

    #2
    cnt_1 = 0
    cnt_2 = 0
    tmp = ''
    for i in a :
        if tmp in list_1 :
            if i in list_1 :
                cnt_1 += 1
            else :
                cnt_1 = 0

        elif tmp in list_2:
            if i in list_2:
                cnt_2 += 1
            else :
                cnt_2 = 0

        if cnt_1 >= 2 or cnt_2 >= 2 :
            flag = 0

        else :
            pass
        tmp = i

    #3
    tmp = ''
    for i in a :
        if i != 'e' and i != 'o' :
            if tmp == i :
                flag = 0
        tmp = i

    
    if flag == 1 :
        print('<'+a+'> is acceptable.')
    else :
        print('<'+a+'> is not acceptable.')
