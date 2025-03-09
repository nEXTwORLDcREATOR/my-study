from collections import deque
dirs = [lambda x,y:(x+1,y),
        lambda x,y:(x,y+1),
        lambda x,y:(x,y-1),
        lambda x,y:(x-1,y)]

m = int(input())
farm = [[float('inf')]*302 for i in range(302)]
def is_valid(x,y):
    return 0 <= x < 302 and 0 <= y < 302

for i in range(m):
    x,y,t = map(int,input().split())
    farm[x][y] = min(t,farm[x][y])
    for dir in dirs:
        n_x,n_y = dir(x,y)
        farm[n_x][n_y] = min(t,farm[n_x][n_y])

def bfs():
    if farm[0][0] == 0:
        return -1
    visited = [[False]*302 for i in range(302)]
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = True
    while queue:
        x,y,t = queue.popleft()

        if farm[x][y] == float('inf'):
            return t
        for dir in dirs:
            next_code = dir(x,y)
            if is_valid(next_code[0],next_code[1]) and not visited[next_code[0]][next_code[1]]:
                if t+1 < farm[next_code[0]][next_code[1]]:
                    visited[next_code[0]][next_code[1]] = True
                    queue.append((next_code[0],next_code[1],t+1))
    return -1
result = bfs()
print(result)