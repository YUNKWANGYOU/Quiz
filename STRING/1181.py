import sys

n = int(sys.stdin.readline())

a = []
for _ in range(n):
    x = sys.stdin.readline().rstrip('\n')
    y = len(x)
    a.append((x,y))

a = list(set(a))
a.sort(key = lambda a:(a[1],a[0]))

for i in a :
    print(i[0])
