import sys

a,b,c = map(int,sys.stdin.readline().split())

res1 = (a+b)%c
res2 = ((a%c) + (b%c))%c
res3 = (a*b)%c
res4 = ((a%c) * (b%c))%c

sys.stdout.write(str(res1)+'\n')
sys.stdout.write(str(res2)+'\n')
sys.stdout.write(str(res3)+'\n')
sys.stdout.write(str(res4)+'\n')
