import sys

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [0,-1,-1,0,1,1,1,0,-1]
dx = [0,0,1,1,1,0,-1,-1,-1]

def make_cloud(cloud) :
    # 현재 구름인 곳을 제외한 인덱스 구하기
    tmp = cloud
    cloud = []

    for i in range(n) :
        for j in range(n) :
            if [i,j] not in tmp :
                if basket[i][j] >= 2 :
                    cloud.append([i,j])
                    basket[i][j] -= 2

def cnt_cross(c) :
    sum = 0
    if 0<= c[0]-1 <= n-1 and 0<= c[1]-1 <= n-1 :
        if basket[c[0]-1][c[1]-1] :
            sum+=1
    if 0<= c[0]+1 <= n-1 and 0<= c[1]-1 <= n-1 :
        if basket[c[0]+1][c[1]-1] :
            sum+=1
    if 0<= c[0]-1 <= n-1 and 0<= c[1]+1 <= n-1 :
        if basket[c[0]-1][c[1]+1] :
            sum+=1
    if 0<= c[0]+1 <= n-1 and 0<= c[1]+1 <= n-1 :
        if basket[c[0]+1][c[1]+1] :
            sum+=1

    return sum

def water_magic(cloud) :
    # 대각선  0 이 아닌것 판단해서 개수만큼 더해주자
    # 대각선 개수 세주기
    # print(cnt_cross(cloud_1),cnt_cross(cloud_2),cnt_cross(cloud_3),cnt_cross(cloud_4))

    # 각 칸에 더해주기
    for i in cloud :
        basket[i[0]][i[1]]+= cnt_cross(i)

def makeitrain(cloud) :
    for i in cloud :
        basket[i[0]][i[1]] += 1


# 얕은복사여서 얘 변하게하면 같이변함
def move_cloud(cloud,dir,cnt) :
    # 옮긴 후에 비 내리게 함
    # c1[0], = c1 - dy[dir]

    # print(cloud_1,cloud_2,cloud_3,cloud_4)
    for i in range(cnt) :
        for j in cloud :
            j[0],j[1] = (j[0]+dx[dir]+n)%n,(j[1]+dy[dir]+n)%n
    # print(cloud_1,cloud_2,cloud_3,cloud_4)
    makeitrain(cloud)

def solution() :
    cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

    for c in command :
        # 옮길 방향
        dir = c[0]
        # 옮길 횟수
        cnt = c[1]

        move_cloud(cloud,dir,cnt)
        water_magic(cloud)
        make_cloud(cloud)

    for b in basket :
        print(b)

if __name__ == '__main__':

    n,m = map(int,sys.stdin.readline().split(' '))
    basket = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]
    command = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(m)]

    solution()
