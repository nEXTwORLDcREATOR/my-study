v = int(input())
n = int(input())
a_v = []
for i in range(n):
    vi = int(input())
    a_v.append(vi)
dp = [0]* (v+1)
for i in range(n):
    vi = a_v[i]
    for j in range(v,vi-1,-1):
        dp[j] = max(dp[j],dp[j-vi]+vi)
print(v-dp[v])
