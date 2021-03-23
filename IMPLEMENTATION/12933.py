import sys
from collections import deque
sys.setrecursionlimit(10**4)
def go(quack,idx,c) :
    global duck
    if idx >= len(sen) :
        return
    if sen[idx] == sound[quack] and check[idx] == 0 :
        q.append(idx)
        if sound[quack] == 'k' :
            if c == 0 :
                duck += 1
                c = 1
            while q :
                check[q.popleft()] = 1

        if quack == 4 :
            quack = 0
        else :
            quack+=1

    go(quack,idx+1,c)

q = deque()
sen = sys.stdin.readline().rstrip('\n')
check = [0]*2505
sound = ['q','u','a','c','k']
duck = 0

for i in range(len(sen)) :
    if sen[i] == 'q' and check[i] == 0 :
        go(0,i,0)
for i in range(len(sen)) :
    if check[i] == 0 :
        print(-1)

if duck == 0 or len(sen)%5 != 0 :
    print(-1)


print(duck)
