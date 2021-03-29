import sys

n = int(sys.stdin.readline())
a = [list(map(str,sys.stdin.readline().split())) for _ in range(n)]

for i in a :
    for j in i :
        print(j[::-1],end = ' ')
    print()
