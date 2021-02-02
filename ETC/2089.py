import sys

n = int(sys.stdin.readline())

if n == 0 :
    sys.stdout.write('0')

num = ''

while n :
    if n % (-2) :
        num = '1' + num
        n = n//-2 + 1
    else :
        num = '0' + num
        n = n//-2

sys.stdout.write(num+'\n')
