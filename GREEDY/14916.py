import sys

n = int(sys.stdin.readline())
o = n%5
res = 0
if n == 1 or n == 3 :
    res = -1
elif o%2 == 0 :
    res = n//5 + o//2
else :
    res = n//5-1 + (o+5)//2

print(res)
