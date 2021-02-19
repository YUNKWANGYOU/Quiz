#2/20 다시풀어보기
import sys

N = int(sys.stdin.readline())

star = ['  *   ',' * *  ','***** ']

def triangle(N) :
    for i in range(len(star)) :
        print(i)
        star.append(star[i] + star[i])
        star[i] = ('   ' * N + star[i] + '   ' * N)


tmp = N
tmp /= 3
cnt = 0

while tmp != 1 :
    tmp/=2
    cnt+=1

for i in range(cnt) :
    triangle(pow(2,i))

for i in star :
    print(i)
