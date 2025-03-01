n = int(input())
mark = [0 for i in range(n)]
def dfs(strat,group):
    if len(group) == n:
        result.append(group.copy())
        return
    if 0 not in mark :
        return
    for i in range(1,n+1):
        if mark[i-1] != 1 and i <= n:
            group.append(i)
            mark[i-1] = 1
            dfs(i+1,group)
            mark[i-1] = 0
            group.pop()
result = []
dfs(0,group=[])
result.sort()
for i in result:
    for _ in i:
        print(f"{_:5d}",end="")
    print()