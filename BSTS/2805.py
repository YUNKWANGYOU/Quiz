import sys

n,m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(tree)

while start <= end :
    mid = (start + end)//2
    tmpsum = 0

    for i in tree :
        if i >= mid :
            tmpsum += i - mid

    if tmpsum < m :
        end = mid - 1
    else :
        start = mid + 1

print(end)
