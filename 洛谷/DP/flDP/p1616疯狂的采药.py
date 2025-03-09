t,m = map(int,input().split())
time1 = []
value1 = []
for i in range(m):
    ti,vi = map(int,input().split())
    time1.append(ti)
    value1.append(vi)
dp = [0] * (t+1)
for i in range(m):
    ti = time1[i]
    vi = value1[i]
    for j in range(ti,t+1):
        dp[j] = max(dp[j-ti]+vi,dp[j])
print(dp[t])