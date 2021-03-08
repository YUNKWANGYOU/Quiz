import sys

flag = False

def promising(i,j) :
    tmp = [1,2,3,4,5,6,7,8,9]
    #row, column 검사
    for k in range(9) :

        if sudoku[i][k] in tmp :
            tmp.remove(sudoku[i][k])
        if sudoku[k][j] in tmp :
            tmp.remove(sudoku[k][j])

    i //= 3
    j //= 3
    #3x3 박스 검사
    for m in range(i*3,(i+1)*3) :
        for n in range(j*3,(j+1)*3) :
            if sudoku[m][n] in tmp :
                tmp.remove(sudoku[m][n])

    return tmp

def dfs(x) :
    global flag
    if flag == True :
        return

    #dfs(x+1)계속하다가 x == len(zero)이면 모두 다 탐색했으므로 종료
    if len(zero) == x :
        flag =True
        for m in range(9):
            for n in range(9):
                print(sudoku[m][n],end= ' ')
            print()
        return

    else :
        (i,j) = zero[x]
        tmp = promising(i,j)

        for k in tmp :
            sudoku[i][j] = k
            dfs(x+1)
            sudoku[i][j] = 0

sudoku = []
for _ in range(9) :
    sudoku.append(list(map(int,sys.stdin.readline().split())))
zero = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)
