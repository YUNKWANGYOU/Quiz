import sys

sen = ''

while sen != 'END' :
    sen = sys.stdin.readline().rstrip('\n')
    if sen != 'END' :
        print(sen[::-1])
