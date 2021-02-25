import sys

def check(num) :
    num = list(str(num))
    for i in num :
        if i in disable :
            return False
    return True

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
disable = list(sys.stdin.readline().split())

res = abs(100-n)

for i in range(1000001) :
    if check(i) :
        res = min(res,len(str(i))+abs(i-n))
print(res)
