import sys
from collections import deque
if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split(' '))
    a = list(map(int,sys.stdin.readline().split(' ')))
    print(n,k,a)

    up, down = deque(a[:n]), deque(a[n:])
    print(up,down)

    # while up.count(0)+down.count(0) < k :
        
