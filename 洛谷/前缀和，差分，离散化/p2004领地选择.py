n,m,c = map(int,input().split())
sum1 = [[0] *(m+1)]
value1 = [[0]+list(map(int,input().split()))for j in range(n)]
sum1.extend(value1)
sum2 = [[0]*(m+1)for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        sum2[i][j] = sum1[i][j]+sum2[i-1][j]+sum2[i][j-1]-sum2[i-1][j-1]

all_v = []
for i in range(1,n-c+2):
    for j in range(1,m-c+2):
        sum3 = sum2[i+c-1][j+c-1]-sum2[i+c-1][j-1]-sum2[i-1][j+c-1]+sum2[i-1][j-1]
        all_v.append((i,j,sum3))

all_v.sort(key=lambda x:x[2])
print(all_v[-1][0],all_v[-1][1],sep=" ")
