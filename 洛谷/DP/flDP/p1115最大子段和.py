n = int(input())
a = [0]+ [i for i in map(int,input().split())]
s = [0] * (n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
max_sum = 0
for i in range(n,-1,-1):
    for j in range(0,i):
        max_sum = max(max_sum,s[i]-s[j-1])
print(max_sum)