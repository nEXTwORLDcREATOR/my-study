import sys
from bisect import *
input = lambda:sys.stdin.readline().strip()

N,C = map(int,input().split())
num_list = sorted([i for i in map(int,input().split())])

res = 0
for i,x in enumerate(num_list):
    L = bisect(num_list,C+x-1,i+1)
    R = bisect(num_list,C+x,i+1)
    res += (R-L)
print(res)
