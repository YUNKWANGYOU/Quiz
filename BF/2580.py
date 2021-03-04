import sys
sudoku = []
for _ in range(9) :
    sudoku.append(list(map(int,sys.stdin.readline().split())))

for i in sudoku :
    print(i)
