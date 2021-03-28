import sys

n = int(sys.stdin.readline())
sen = []
for _ in range(n) :
    sen.append(sys.stdin.readline().rstrip('\n'))


for i in sen:
    max = 0
    max_res = ''
    for j in i:
        if i.count(j) > max and j != ' ' :
            max = i.count(j)
            max_res = j
        elif i.count(j) == max and max_res != j and j != ' ':
            max_res = '?'
    print(max_res)
