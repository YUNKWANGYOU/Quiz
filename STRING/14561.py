import sys

t = int(sys.stdin.readline())
res = []
for i in range(t):
    a,n = map(int,sys.stdin.readline().split())
    word = ''
    while a>=n:
        word = str(hex(a%n)[2:]) + word
        a = a//n
    word = str(hex(a)[2:]) + word
    print(int(word == word[::-1]))

