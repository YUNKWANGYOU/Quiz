import sys

list_1 = ['A','B','C','D','E','F']
list_2 = ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n = int(sys.stdin.readline())

for i in range(n) :
    s = sys.stdin.readline().rstrip('\n')
    a = s.find('A')
    f = s.find('F')
    c = s.find('C')

    aend = a-1
    fend = f-1
    for j in s :
        if j == 'A' :
            aend += 1
        if j == 'F' :
            fend += 1

    check = 0

    if s[len(s)-1] == 'A' or s[len(s)-1] == 'F' or s[len(s)-1] == 'C':
        if (a<f) and (f<c) and(a<c) :
            if aend == f-1 and fend == c-1 :
                check = 1

    if check :
        print("Infected!")
    else :
        print("Good")
