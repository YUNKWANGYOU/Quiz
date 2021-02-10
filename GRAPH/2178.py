dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int,input().split())

maze = []
queue = [[0,0]]

for i in range(m) :
    maze.append(list(input()))

maze[0][0] =1

while queue:
    x, y = queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '1' :
            maze[nx][ny] =  maze[x][y] + 1
            queue.append([nx,ny])

print(maze[m-1][n-1])
