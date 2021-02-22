import sys

n = list(sys.stdin.readline().rstrip('\n'))
n.sort(reverse = True)
sum = 0

for i in range(len(n)) :
    sum += int(n[i])

if sum%3 == 0 and '0' in n :
    for i in n :
        print(i,end ='')
else :
    print(-1)

print()
