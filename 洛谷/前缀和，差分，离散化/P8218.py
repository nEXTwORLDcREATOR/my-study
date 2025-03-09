import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
num_list = list(map(int,input().split()))
sum = [0] * (n+1)
for i in range(n):
    sum[i+1] = sum[i] + num_list[i]

m = int(input())
for i in range(m):
    l,r = map(int,input().split())
    print(sum[r]-sum[l-1])
