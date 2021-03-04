import sys
from itertools import combinations

vowel = ['a','e','i','o','u']

l,c = map(int,sys.stdin.readline().split())
a = list(map(str,sys.stdin.readline().split()))
a.sort()

comb = combinations(a,l)

for i in comb :
    cnt_v = 0
    cnt_c = 0
    for j in i :
        if j in vowel :
            cnt_v+=1
        else :
            cnt_c+=1

    if cnt_v >= 1 and cnt_c >= 2 :
        print(''.join(i))
