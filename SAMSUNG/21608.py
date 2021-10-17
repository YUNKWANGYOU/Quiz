import sys

dy = [0,-1,0,1]
dx = [-1,0,1,0]

def solution():
    for _ in range(n*n) :
        input = list(map(int,sys.stdin.readline().split(' ')))
        like[input[0]] = input[1:]

        max_x = 0
        max_y = 0
        max_like = -1
        max_zero = -1

        for i in range(n) :
            for j in range(n) :
                if board[i][j] == 0 :
                    likecnt = 0
                    zerocnt = 0
                    for k in range(4) :
                        nx = i+dx[k]
                        ny = j+dy[k]
                        if 0<=nx<n and 0<=ny<n :
                            if board[nx][ny] in input :
                                likecnt+=1
                            if board[nx][ny] == 0 :
                                zerocnt+=1
                    if max_like < likecnt or (max_like == likecnt and max_zero < zerocnt) :
                        max_x = i
                        max_y = j
                        max_like = likecnt
                        max_zero = zerocnt
        board[max_x][max_y] = input[0]

    score_board = [[0]*n for _ in range(n)]
    score = 0
    for i in range(n) :
        for j in range(n) :
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<n :
                    if board[nx][ny] in like[board[i][j]] :
                        score+=1
            score_board[i][j] = score
            score = 0

    answer = 0
    for i in score_board:
        for j in i:
            if j == 0 :
                answer+=0
            elif j == 1 :
                answer+=1
            elif j == 2 :
                answer+=10
            elif j == 3 :
                answer+=100
            elif j == 4 :
                answer+=1000

    print(answer)
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    like = {}
    board = [[0]*n for _ in range(n)]

    # board[1][1] = 4
    solution()
