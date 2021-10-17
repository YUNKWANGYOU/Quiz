import sys

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

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
    return cloud

def cnt_cross(c) :
    cx = [-1,-1,1,1]
    cy = [-1,1,-1,1]

    sum = 0
    x = c[0]
    y = c[1]

    for i in range(4) :
        nx = x+cx[i]
        ny = y+cy[i]
        if 0<=nx<n and 0<=ny<n and basket[nx][ny] >= 1 :
            sum+=1

    return sum

def water_magic(cloud) :

    # 대각선 0아닌거 판단해서 더해주기
    for i in cloud :
        basket[i[0]][i[1]]+= cnt_cross(i)

def makeitrain(cloud) :
    for i in cloud :
        basket[i[0]][i[1]] += 1


# 얕은복사여서 얘 변하게하면 같이변함
def move_cloud(cloud,dir,cnt) :
    # 옮긴 후에 비 내리게 함
    for i in range(cnt) :
        for j in cloud :
            j[0],j[1] = (j[0]+dy[dir]+n)%n,(j[1]+dx[dir]+n)%n
    makeitrain(cloud)

def solution() :
    # 구름 초기값
    cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

    for c in command :
        # 옮길 방향
        dir = c[0]
        # 옮길 횟수
        cnt = c[1]

        move_cloud(cloud,dir,cnt)
        water_magic(cloud)
        cloud = make_cloud(cloud)

    answer = 0
    for i in basket:
        for j in i:
            answer+=j
    print(answer)

if __name__ == '__main__':

    n,m = map(int,sys.stdin.readline().split(' '))
    basket = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]
    command = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(m)]

    solution()
