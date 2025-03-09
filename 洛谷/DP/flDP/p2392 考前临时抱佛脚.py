s1,s2,s3,s4 = map(int,input().split())
a = sorted([i for i in map(int,input().split())])
b = sorted([i for i in map(int,input().split())])
c = sorted([i for i in map(int,input().split())])
d = sorted([i for i in map(int,input().split())])

def time_cost_hh(li,s):
    total = sum(li)
    half = total // 2
    memo = {}
    def time_cost(half,n):
        if (half,n) in memo:
            return memo[(half,n)]
        elif n < 0:                    #  边界条件 dp初始值
            return 0
        elif half < li[n]:
            return time_cost(half,n-1)
        memo[(half,n)] = max(time_cost(half,n-1),time_cost(half-li[n],n-1)+li[n]) # 状态转移 dp[n] = max[dp[n-1],dp[n-1]+li[n])
        return max(time_cost(half,n-1),time_cost(half-li[n],n-1)+li[n])
    res = time_cost(half,s-1)
    ans = max(res,total-res)
    return ans

print(time_cost_hh(a,s1)+time_cost_hh(b,s2)+time_cost_hh(c,s3)+time_cost_hh(d,s4))




