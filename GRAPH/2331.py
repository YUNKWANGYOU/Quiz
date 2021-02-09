import sys

a,p = map(int,sys.stdin.readline().split())

permu  = [a]

while 1 :
    t = permu[-1]
    sum = 0

    while t :
        sum += ((t%10)**p)
        t = t//10

    if sum in permu :
        sys.stdout.write(str(permu.index(sum)) + '\n')
        break
    else :
        permu.append(sum)
