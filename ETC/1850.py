import sys

n,m  = map(int, sys.stdin.readline().split())

x,y = (n,m) if (n > m) else (m,n)

while x % y :
    x,y = y,x%y

sys.stdout.write(''.join(['1']*y)+'\n')
