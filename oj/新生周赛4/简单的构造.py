n,m,k = map(int,input().split())
a = [m*i for i in range(1,n)]
b = []
for i in range(n//2):
    if i == k:
        continue
    else:
        b.append(a[i])
for i in range(1,n+1):
    if i%2 !=0:
        print(a.pop(0),end=' ')
    else:
        print(b.pop(0),end=' ')





