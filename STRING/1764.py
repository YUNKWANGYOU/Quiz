# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

import sys
n,m = map(int,sys.stdin.readline().split())
a = []
b = []
res = []

for i in range(n) :
    a.append(sys.stdin.readline().rstrip('\n'))

for i in range(m) :
    b.append(sys.stdin.readline().rstrip('\n'))

res = sorted(list(set(a)&set(b)))
print(len(res))
for i in res :
    print(i)
