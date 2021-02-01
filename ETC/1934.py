import sys

def lcm(a,b) :
    c = a*b
    while 1 :
        a2 = b
        b2 = a%b

        if b2 == 0 :
            return int(c/a2)
            break

        a = a2
        b = b2

t = int(sys.stdin.readline())
a = []

for _ in range(t) :
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(t) :
    print(lcm(a[i][0],a[i][1]))
