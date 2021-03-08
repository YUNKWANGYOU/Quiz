import sys
n,m  = map(int,sys.stdin.readline().split())
a = []
for _ in range(m) :
    a.append(list(map(int,sys.stdin.readline().rstrip('\n'))))

for i in a :
    print(i)
