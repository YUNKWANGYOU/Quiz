import sys

s = sys.stdin.readline().rstrip('\n')

s2 = []

for i in range(len(s)) :
    s2.append(s[i:len(s)])

s2.sort()

for i in range(len(s2)) :
    print(s2[i])
