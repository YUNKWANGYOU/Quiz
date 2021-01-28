import sys

n = int(sys.stdin.readline())

dict = {}

for i in range(n) :

    num = int(sys.stdin.readline())

    if num not in dict.keys() :
        dict[num] = 1
    else :
        dict[num] += 1

max_num = max(list(dict.values())) #개수중 최대 반환

a = []

for key, value in dict.items() : #아이템 쓱 한번 훑음
    if value == max_num :
        a.append(key)

print(min(a))
