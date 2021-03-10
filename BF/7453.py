import sys

n = int(sys.stdin.readline())
a,b,c,d = [],[],[],[]

for _ in range(n) :
    a2,b2,c2,d2 = map(int,sys.stdin.readline().split())
    a.append(a2);b.append(b2);c.append(c2);d.append(d2)

ab = dict()

for a2 in a :
    for b2 in b :
        ab[a2+b2] = ab.get(a2+b2,0) + 1

res = 0

for c2 in c :
    for d2 in d:
        res += ab.get(-c2-d2,0)

print(res)
