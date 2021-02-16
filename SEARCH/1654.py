import sys

k,n = map(int,sys.stdin.readline().split())

lan = []

for i in range(k) :
    lan.append(int(sys.stdin.readline()))

s = 1
l = max(lan)

while 1 :
    m = (s+l)//2
    line = 0

    for i in lan :
        line += i//m

    if line >= n :
        s = m+1
    else :
        l = m-1

    if s > l :
        print(l)
        break
