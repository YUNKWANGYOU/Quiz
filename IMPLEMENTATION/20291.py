import sys

dict = {}

n = int(sys.stdin.readline())

for _ in range(n) :
    file = sys.stdin.readline().rstrip('\n').split('.')

    if file[1] in dict :
        dict[file[1]]+=1
    else :
        dict[file[1]] = 1

dict = sorted(dict.items(), key=lambda x : x[0])
for i in dict :
    print(i[0],end = ' ')
    print(i[1])
