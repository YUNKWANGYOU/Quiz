import sys


def jh(stock,tmp):
    cnt = 0
    for i in range(14) :
        if tmp//stock[i] > 0 :
            cnt += tmp//stock[i]
            tmp -= stock[i]*(tmp//stock[i])

    sum = tmp + cnt*stock[13]
    return sum

def sm(stock,tmp):
    cnt = 0
    for i in range(14) :
        if 2 <= i < 13 :
            if stock[i-2] > stock[i-1] and stock[i-1] > stock[i] :
                if tmp//stock[i+1] > 0 :
                    cnt += tmp//stock[i+1]
                    tmp -= stock[i+1]*(tmp//stock[i+1])
            elif stock[i-2] < stock[i-1] and stock[i-1] < stock[i] :
                    tmp += cnt*stock[i+1]
                    cnt = 0

    sum = tmp + cnt*stock[13]
    return sum

cash = int(sys.stdin.readline())
stock = list(map(int,sys.stdin.readline().split()))
tmp = cash

j = jh(stock,tmp)
s = sm(stock,tmp)
if j>s :
    print("BNP")
elif j<s :
    print("TIMING")
else :
    print("SAMESAME")
