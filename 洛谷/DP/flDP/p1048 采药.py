t,m = map(int,input().split())
time = []
value = []
for i in range(m):
    t1,v1 = map(int,input().split())
    time.append(t1)
    value.append(v1)
cache = {}
def dfs(m,t):
    if (m,t) in cache:
        return cache[(m,t)]
    if m < 0:
        return 0
    if t < time[m]:
        return dfs(m-1,t)
    cache[(m,t)] = max(dfs(m-1,t),dfs(m-1,t-time[m])+value[m])
    return cache[(m,t)]
res = dfs(m-1,t)
print(res)
