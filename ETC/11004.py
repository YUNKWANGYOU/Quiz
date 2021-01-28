import sys

n, m  = map(int,sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

print(a[m-1])
