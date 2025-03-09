t, m = map(int, input().split())
time = []
value = []
for _ in range(m):
    t1, v1 = map(int, input().split())
    time.append(t1)
    value.append(v1)

# 初始化动态规划数组
dp = [0] * (t + 1)

# 动态规划过程
for i in range(m):
    for j in range(t, time[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - time[i]] + value[i])

# 输出结果
print(dp[t])