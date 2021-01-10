global a
a = []

def func1(x,cnt) :
    global a
    if x%3 == 0 :
        # print(x,end = '->')
        x = x/3
        cnt = cnt +1
    elif x%2 == 0 :
        # print(x,end = '->')
        x = x/2
        cnt = cnt +1
    elif x == 1 :
        # print(x)
        # print(cnt)
        a.append(cnt)
        return 0
    else :
        # print(x,end = '->')
        x = x-1
        cnt = cnt +1

    func1(x,cnt)

def func2(x,cnt) :
    global a
    if x%3 == 0 :
        #print(x,end = '->')
        x = x/3
        cnt = cnt +1
    elif x%2 == 0 :
        #print(x,end = '->')
        x = x/2
        cnt = cnt +1
    elif x == 1 :
        # print(x)
        # print(cnt+1)
        a.append(cnt+1)
        return 0
    else :
        print(x,end = '->')
        x = x-1
        cnt = cnt +1

    func2(x,cnt)



if __name__ == "__main__" :

    cnt = 0
    x = int(input())
    func1(x,cnt)


    #print(x,end= "->")
    x = x-1
    func2(x,cnt)

    print(min(a))
