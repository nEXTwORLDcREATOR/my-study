# from bisect import *
import sys
def bisect(a,x,lo=0,hi=None):
    if hi == None:hi=len(a)
    while lo < hi:
        i = (lo + hi) >> 1
        if a[i] > x:
            hi = i
        else:
            lo = i+1
    return lo
input = lambda: sys.stdin.readline().strip()
n,m = map(int,input().split())
arr = [map(int,input().split())]
find_list = [map(int,input().split())]
s = set(arr)#没有这个就超时
for i in find_list:
    if i in s:
        print(bisect(arr,i-1)+1,end=" ")
    else:
        print(-1,end=" ")
