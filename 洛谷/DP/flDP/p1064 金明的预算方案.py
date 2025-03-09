n,m = map(int,input().split())
value1 = []
port = []
main1 = []
for i in range(m):
    vi,pi,qi = map(int,input().split())
    value1.append(vi)
    port.append(pi)
    main1.append(qi)
goods = []
for i in range(m):
    if main1[i] == 0:
        goods.append((value1[i],port[i]))
    else:
        goods.append((value1[i]+value1[main1[i]-1],port[i]+port[main1[i]-1]))
print(goods)
hehe = [(0,0)for i in range(5)]
for i in range(m):
    if main1[i] != 0:
        hehe[main1[i]] = (hehe[main1[i]][0]+value1[i],hehe[main1[i]][1]+port[i])
print(hehe)
for i in range(5):
    if hehe[i] != (0,0):
        hehe[i] = (hehe[i][0]+value1[i],hehe[i][1]+port[i])
        goods.append(hehe[i])
dp = [0] * (n+1)
print(goods)
for i in range(len(goods)-1):
    vi = goods[i][0]
    pi = goods[i][1]
    for j in range(n,vi-1,-1):
        dp[j] = max(dp[j],dp[j-vi]+pi)
print(dp[n])