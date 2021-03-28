import sys
from collections import deque
a = list(map(str,sys.stdin.readline().rstrip('\n')))
b = sys.stdin.readline().rstrip('\n')
res = []

for i in a :
    if ord(i) < 91 and ord(i) >= 65 :
        res.append(i)
    elif ord(i) >= 97 and ord(i) < 123 :
        res.append(i)

res = ''.join(res)

if b in res :
    print(1)
else :
    print(0)
