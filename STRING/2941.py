import sys

dict = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = sys.stdin.readline().rstrip('\n')
sum = len(a)

i = 0
while 1 :
    if i == len(a):
        break

    tmp = a[i:i+2]
    tmp2 = a[i:i+3]
    if tmp in dict :
        sum-=1
        i+=1

    elif tmp2 == 'dz=' :
        sum-=2
        i+=2
    i+=1


print(sum)
