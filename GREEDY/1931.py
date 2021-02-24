import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n) :
    a.append(list(map(int,sys.stdin.readline().split())))

a.sort(key = lambda x : (x[1],x[0]))

cnt=1
end = a[0][1]

for i in range(1,n) :
    if end <= a[i][0]:
        cnt+=1
        end = a[i][1]

print(cnt)
