import sys

def div(a,b) :
    cnt = 0
    while a != 0 :
        a = a//b
        cnt += a
    return cnt

n,m = map(int,sys.stdin.readline().split())

div_2 = div(n,2) - div(m,2) - div(n-m,2)
div_5 = div(n,5) - div(m,5) - div(n-m,5)

print(min(div_2,div_5))
