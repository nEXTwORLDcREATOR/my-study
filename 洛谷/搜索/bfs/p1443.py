from collections import deque
dirs = [lambda x,y:(x+2,y+1),
        lambda x,y:(x+1,y+2),
        lambda x,y:(x+2,y-1),
        lambda x,y:(x-1,y+2),
        lambda x,y:(x-2,y-1),
        lambda x,y:(x-1,y-2),
        lambda x,y:(x+1,y-2),
        lambda x,y:(x-2,y+1)]
n,m,x,y = map(int,input().split())

board = [[-1]*m for i in range(n)]
def is_valid(x,y):
    return 0 <= x <n and 0<= y < m

def bfs(x1,y1):
    queue = deque()
    queue.append((x1,y1))
    board[x1][y1] = 0
    while len(queue) > 0:
        cur_code = queue.popleft()
        for dir in dirs:
            next_code = dir(cur_code[0],cur_code[1])
            if is_valid(next_code[0],next_code[1]) and board[next_code[0]][next_code[1]]== -1:
                board[next_code[0]][next_code[1]] = board[cur_code[0]][cur_code[1]] + 1
                queue.append((next_code[0],next_code[1]))
bfs(x-1,y-1)

for _ in board:
    for i in _:
        print(f"{i:5d}",end="")
    print()

