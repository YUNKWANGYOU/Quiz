# TODO: 1. '(' 가 나오는 경우 -> 생성된 파이프 개수 +1
#       2. ')' 가 나오는 경우 -> 생성된 파이프 개수 -1
#            (1). 바로 전 문자가 '('인 경우 -> 절단된 막대기 개수 + 생성되어있는 파이프 개수
#            (2). 바로 전 문자가 ')' 인 경우 -> 절단된 막대기 개수 + 1

import  sys

bar = sys.stdin.readline().rstrip('\n')

sum = 0     #절단된 막대기 개수
left = 0    #현재 생성된 파이프 개수

for i in range(len(bar)) :

    if bar[i] == '(' :
        left += 1
    elif bar[i] == ')' :
        left -= 1
        if bar[i-1] == '(':
            sum = sum + left
        else :
            sum = sum + 1
    else :
        pass


print(sum)
