import sys

# ↑ : 0, ↗ : 1, → : 2, ↘ : 3, ↓ : 4, ↙ : 5, ← : 6, ↖ : 7
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


class FireBall:
    # 행, 열, 질량, 속도, 방향
    def __init__(self, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d


def move_fireball():
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for f in board[i][j]:
                nr, nc = (f.r + dy[f.d] * (f.s % N) + N) % N, (f.c + dx[f.d] * (f.s % N) + N) % N
                tmp_board[nr][nc].append(FireBall(nr, nc, f.m, f.s, f.d))
    for i in range(N):
        for j in range(N):
            board[i][j] = tmp_board[i][j]


def sum_fireball():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                sum_m, sum_s, odd_even, sz = 0, 0, board[i][j][0].d % 2, len(board[i][j])
                dir_flag = True
                for f in board[i][j]:
                    sum_m += f.m
                    sum_s += f.s
                    if odd_even != f.d % 2:
                        dir_flag = False
                board[i][j] = []
                if sum_m // 5 != 0:
                    for d in range(4):
                        if dir_flag:
                            board[i][j].append(FireBall(i, j, sum_m // 5, sum_s // sz, 2 * d))
                        else:
                            board[i][j].append(FireBall(i, j, sum_m // 5, sum_s // sz, 2 * d + 1))


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    board = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        r1, c1, m1, s1, d1 = map(int, sys.stdin.readline().split())
        board[r1 - 1][c1 - 1].append(FireBall(r1 - 1, c1 - 1, m1, s1, d1))

    for _ in range(K):
        move_fireball()
        sum_fireball()

    answer = 0
    for i1 in range(N):
        for j1 in range(N):
            for f1 in board[i1][j1]:
                answer += f1.m
    print(answer)
