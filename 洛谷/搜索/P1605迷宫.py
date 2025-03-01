dirs = [lambda x,y:(x+1,y),
        lambda x,y:(x,y+1),
        lambda x,y:(x-1,y),
        lambda x,y:(x,y-1)]
N,M,T = map(int,input().split())
sx,sy,fx,fy = map(int,input().split())
maze = [[0]*(N) for i in range(M)]
for i in range(T):
    x,y = map(int,input().split())
    maze[x-1][y-1] = 1
result = []
def maze_path(maze,start,path):
    if start == (fx-1,fy-1):
        path.append(start)
        result.append(path.copy())
        return
    if start[0] < 0 or start[1] < 0 or start[0]>= N or start[1] >= M:
        return
    if maze[start[0]][start[1]] != 0:
        return
    maze[start[0]][start[1]] = 2
    path.append(start)
    for dir in dirs:
        nextcode = dir(start[0],start[1])
        if 0 <= nextcode[0] < N and 0 <= nextcode[1] < M:
            if maze[nextcode[0]][nextcode[1]] == 0:
                maze_path(maze,nextcode,path)
                maze[nextcode[0]][nextcode[1]] = 0
                path.pop()
maze_path(maze,(sx-1,sy-1),path=[])
print(len(result))