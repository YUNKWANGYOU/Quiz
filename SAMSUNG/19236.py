import sys
import copy
# ↑ : 1, ↖ : 2, ← : 3, ↙ : 4, ↓ : 5, ↘ : 6, → : 7, ↗ : 8
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def food(array,x,y) :
    # 상어가 먹을 수 있는 물고기의 인덱스를 저장한 공간
    positions = []
    # 상어의 방향
    direction = array[x][y][1]
    # 상어는 해당 방향으로 근접 1칸, 2칸, 3칸 총 3개의 후보 먹이를 갖고있다.
    for i in range(1,4) :
        nx,ny = x+dx[direction], y+dy[direction]
        # 칸 안에 있고, 상어가 방문하지 않았다면
        if 0<= nx < 4 and 0 <= ny < 4 and  1 <= array[nx][ny][0] <= 16 :
            # 후보군에 추가
            positions.append([nx,ny])
        # 2번째 칸, 3번째 칸도 추가해주기 위해 사용한 식
        x,y = nx,ny
    return positions

def find_fish(array,index):
    # 현재 배열에서 특정 번호의 물고기 위치 찾기
    for i in range(4):
        for j in range(4) :
            if array[i][j][0] == index :
                return (i,j)
    return None

def move_fish(array,now_x,now_y) :
    flag = False

    # 교환할 물고기의 위치를 저장해주는 공간 postion
    position = []

    # 1번 물고기부터 16번 물고기까지 순차적으로 방향에 맞게 교환해주고,
    # 교환할 물고기가 없는 물고기는 방향을 반시계 방향으로 바꿔서 교환해줌.
    for i in range(1,17) :
        # 1번부터 16번까지 물고기의 위치를 찾아줌 (-1인 경우는 방문했으므로 None)
        position = find_fish(array,i)
        # None 인 경우 이미 방문(교환)했음을 의미
        if position is None :
            continue
        # 교환 준비
        x,y = position[0], position[1]
        direction = array[x][y][1]

        # 방향에 해당하는 배열이 교환 불가능할 경우를 대비해서 8방향 순서대로 체크해줘야해서 for문 사용
        for j in range(8) :
            # 비교할 인덱스 찾기
            nx, ny = x+dx[direction], y+dy[direction]
            # 인덱스의 범위가 적절하면
            if  0 <= nx < 4 and 0 <= ny < 4 :
                # 해당 인덱스의 값에 상어가 없을  경우
                if not(nx == now_x and ny == now_y) :
                    # 물고기 번호 교체
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    # 물고기 방향 교체
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], direction
                    break
            # 해당 조건에 안맞을 경우 반시계 45도 바꿔줌
            direction = (direction+1) % 8

def dfs(array,x,y,total) :
    global answer
    array = copy.deepcopy(array)

    # 1. 해당 위치 물고기 먹기
    # 번호의 합에 더할 거 미리 빼두기
    number = array[x][y][0]
    # -1로 지나갔음을 표시해줌
    array[x][y][0] = -1

    # 2. 물고기 이동
    move_fish(array,x,y)

    # 3. 상어의 이동 후보 확인
    res = food(array,x,y)

    # 해당 먹이 먹는 모든 과정을 탐색하고, 최댓값 도출
    answer = max(answer,total+number)
    for next_x,next_y in res :
        dfs(array,next_x,next_y,total+number)

if __name__ == '__main__' :
    sea = [list(sys.stdin.readline().split()) for i in range(4)]
    shark = []

    # [[번호, 방향]] 으로 바꾸기
    for i in sea :
        tmp = []
        for j in range(0,len(i),2) :
            tmp.append([int(i[j]),int(i[j+1])-1])
        shark.append(tmp)

    answer = 0
    # (배열,상어 x 위치, 상어 y 위치, 먹은 물고기 수)
    dfs(shark,0,0,0)
    print(answer)
