import sys
input = lambda :sys.stdin.readline().strip()
n = int(input())
a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
def bisect(lo,hi,check):
    while lo < hi:
        mid = (lo + hi) >> 1
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
        return lo

m = bisect(1,1**9,lambda v : all(A // v <= B for A,B in zip(a,b)))
M = bisect(1,10**9,lambda v : all(A// v < B for A,B in zip(a,b)))
print(m,M)