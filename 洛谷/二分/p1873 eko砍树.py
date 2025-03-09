import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
tree_hi = [i for i in map(int,input().split())]

def check(x,arr):
    res = 0
    for i in arr:
        if i > x:
            res += i-x
    return res

def bisect(x,lo=0,hi=tree_hi[-1]):
    while lo < hi:
        mid = (lo+hi) >> 1
        if check(mid,tree_hi)<x:
            hi = mid
        else:
            lo = mid + 1
    return lo - 1
print(bisect(m))
