#2/18 풀어보기

import sys

def cut_paper(x,y,N):
    global matrix, cnt1, cnt2, cnt3
    flag = False

    for i in  range(x,x+N) :
        if flag :
            break

        for j in range(y,y+N):
            if matrix[j][i] != matrix[y][x] :
                k = N//3

                cut_paper(x, y, k)
                cut_paper(x + k, y, k)
                cut_paper(x + 2*k, y, k)
                cut_paper(x, y + k, k)
                cut_paper(x + k,  y+ k, k)
                cut_paper(x + 2*k, y + k, k)
                cut_paper(x, y + 2*k, k)
                cut_paper(x + k, y + 2*k, k)
                cut_paper(x + 2*k, y + 2*k, k)

                flag = True
                break

    if flag == 0 :
        if matrix[y][x] == -1 :
            cnt1 += 1
        elif matrix[y][x] == 0 :
            cnt2 += 1
        elif matrix[y][x] == 1 :
            cnt3 += 1

N = int(sys.stdin.readline())
matrix = []
#cnt1 : -1, cnt2 : 0 , cnt3 : 1
cnt1,cnt2,cnt3 = 0,0,0

for _ in range(N) :
    matrix.append(list(map(int,sys.stdin.readline().split())))

cut_paper(0,0,N)
print(cnt1)
print(cnt2)
print(cnt3)
