import sys

n = int(sys.stdin.readline())
minus,plus = [],[]
zero = 0

for _ in range(n) :
    number = int(sys.stdin.readline())
    if number < 0 :
        minus.append(number)
    elif number > 0 :
        plus.append(number)
    else :
        zero+=1

minus.sort()
plus.sort(reverse = True)
res = []

for i in range(0,len(minus)-1,2) :
    res.append(minus[i]*minus[i+1])
if len(minus) % 2 == 1 and zero == 0 :
    res.append(minus[len(minus)-1])

for i in range(0,len(plus)-1,2) :
    if plus[i] > 1 and plus[i+1] > 1 :
        res.append(plus[i]*plus[i+1])
    else :
        res.extend([plus[i],plus[i+1]])
if len(plus) % 2 == 1 :
    res.append(plus[len(plus)-1])

print(sum(res))
