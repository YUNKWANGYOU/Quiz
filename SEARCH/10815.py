#####다시풀기#####
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

for i in check :
    start,end = 0,n
    while start <= end :
        mid = (start+end)//2
        if 0 <= mid < n :
            if card[mid] < i :
                start = mid + 1
            else :
                end = mid - 1
        else :
            break

    if 0 <= end + 1 < n :
        if card[end + 1] == i :
            print(1,end = ' ')
        else :
            print(0,end = ' ')
    else :
        print(0, end = ' ')

print()
