import sys

def gcd(a,b) :
    if b == 0 :
        return a
    else :
        if a>b :
            return gcd(b,a%b)
        else :
            return gcd(a,b%a)

n = int(sys.stdin.readline())

for _ in range(n) :
    a = list(map(int,sys.stdin.readline().split()))
    sum = 0

    for j in  range(1, a[0] + 1) :
        for k in range(1, a[0] + 1 ):
            if j!= k :
                sum += gcd(a[j], a[k])

    print(int(sum/2))
