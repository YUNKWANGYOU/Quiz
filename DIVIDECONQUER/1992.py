import sys

def cut_paper(x,y,n):
    global tree, res
    flag = False

    for i in range(x,x+n) :
        if flag :
            break
        for j in range(y,y+n) :
            if tree[j][i] != tree[y][x]:
                k = n//2
                res +='('
                cut_paper(x,y,k)
                cut_paper(x+k,y,k)
                cut_paper(x,y+k,k)
                cut_paper(x+k,y+k,k)
                res +=')'

                flag = True
                break
    if not flag :
        if tree[y][x] == 1 :
            res +='1'
        elif tree[y][x] == 0 :
            res +='0'

N = int(sys.stdin.readline())
tree = []
res = ''
for _ in range(N):
    tree.append(list(map(int, str(input()))))

cut_paper(0,0,N)
print(res)
