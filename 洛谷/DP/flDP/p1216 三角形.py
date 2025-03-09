import sys
r = int(input())
def read():
    return sys.stdin.readline().split()
sam = [list(map(int,read()))for i in range(r)]
def is_valid(x,y):
    return 0 <=x < r and 0<= y <=x
res = []
memo = {}
def dfs(x,y):
    if (x,y) in memo:
        return memo[(x,y)]
    if not is_valid(x,y):
        return 0
    max_sum = sam[x][y]+ max(dfs(x+1,y),dfs(x+1,y+1))
    memo[(x,y)] = max_sum
    return max_sum
max_sum = dfs(0,0)
print(max_sum)