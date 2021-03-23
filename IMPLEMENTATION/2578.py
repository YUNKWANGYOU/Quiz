import sys

bingo = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
nums = list(map(int,sys.stdin.readline().split()))
for _ in range(4) :
    nums += list(map(int,sys.stdin.readline().split()))
check = [0]*12

cnt = 0
flag = False

for n in range(25) :
    if flag == True :
        break
    for i in range(5) :
        if flag == True :
            break
        for j in range(5) :
            if flag == True :
                break
            if bingo[i][j] == nums[n] :
                bingo[i][j] = 0
                check[i] += 1
                check[j+5] += 1
                if i == j :
                    check[10] += 1
                if i == 4-j :
                    check[11] += 1
                for k in range(12) :
                    if check[k] == 5 :
                        check[k] = 0
                        cnt+=1
                        if cnt == 3 :

                            flag = True
                            print(n+1)
                            break
