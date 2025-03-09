from collections import deque
import sys
def read():
    return sys.stdin.readline().strip().split()
dirs = [(1,0),(0,-1),(-1,0),(0,1)]
n = int(input())
group = [list(map(int,read()))for i in range(n)]
def is_valid(x,y):
    return 0<= x < n and 0<= y < n
def is_side(x,y):
    return x == 0 or x == (n-1) or y == 0 or y == (n-1)
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        group[x][y] = -1
        for dir in dirs:
            n_x,n_y = x+dir[0],y+dir[1]
            if is_valid(n_x,n_y) and group[n_x][n_y] == 0:
                group[n_x][n_y] = -1
                queue.append((n_x,n_y))
    return
for i in range(n):
    for j in range(n):
        if is_side(i,j) and group[i][j] == 0:
            bfs(i,j)
for i in range(n):
    for j in range(n):
        if group[i][j] == 0:
            group[i][j] = 2
        elif group[i][j] == -1:
            group[i][j] = 0
for _ in group:
    print(*_)

