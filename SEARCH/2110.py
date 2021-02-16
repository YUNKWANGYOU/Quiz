import sys

n,c = map(int,sys.stdin.readline().split())

x = []

x = [int(sys.stdin.readline()) for _ in range(n)]

x.sort()

start = 1
end = x[-1] - x[0]
result = 0

while start <= end :
    mid = (start+end)//2
    old = x[0]
    count = 1

    for i in range(1,len(x)):
        if x[i] >= mid + old :
            count += 1
            old = x[i]
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid-1

print(result)
