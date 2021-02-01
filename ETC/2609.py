import sys

a, b = map(int,sys.stdin.readline().split())
c = a*b

while 1 :
    a2 = b
    b2 = a%b

    a = a2
    b = b2

    if b == 0 :
        break

print(a)
print(int(c/a))
