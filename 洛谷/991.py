# n,m = map(int,input().split())
# list_in = [input().strip() for i in range(m)]
# for i in list_in:
#     if i == "A":
#         A = []
#         for _ in range(1,2*n+1,2):
#             A.append(_)
#         print(*A)
#     elif i == "B":
#         B = []
#         for _ in range(2,2*n+1,2):
#             B.append(_)
#         print(*B)
#     elif i == "C":
#         C = []
#         for _ in range(1,n+1):
#             C.append(15*_)
#         print(*C)
#     else:
#         D = []
#         m = 0
#         for _ in range(15*n):
#             if m < n and _ % 5 != 0 and _ % 3 != 0:
#                 D.append(_)
#                 m += 1
#         print(*D)
#
# n,atk = map(int,input().split())
# power = sum(i for i in map(int,input().split()))
# print(power+atk)
from operator import index

# n = int(input())
# monster_list = [i for i in input().strip().split()]
# monster_list.sort()
# def dfs(li,current_mo,index,result):
#     if index == len(li):
#         if current_mo:
#             result.append(current_mo)
#         return
#     dfs(li,current_mo+li[index],index+1,result)
#     dfs(li, current_mo, index + 1,result)
# result = []
# dfs(monster_list,str(),0,result)
# result.sort()
# for i in result:
#     print(i)
# from  collections import deque
# t,live,m,n = map(int,input().split())
# island = [[0]*n for _ in range(m)]
# dirs = [lambda x,y:(x+1,y),
#         lambda x,y:(x,y+1),
#         lambda x,y:(x-1,y),
#         lambda x,y:(x,y-1),
#         ]
# for i in range(t):
#     y,x = map(int,input().split())
#     if 0 <= y < m and 0 <= x < n:
#         island[y][x] = 1
#
# def deq(x1,y1,x2,y2,live):
#     queue = deque()
#     path = []
#     queue.append((x1,y1,-1))
#     while len(queue) > 0:
#         current = queue.popleft()
#         path.append(current)
#         if current[0] == x2 and current[1] == y2:
#             current = path[-1]
#             realpath = []
#             while current[2] != -1:
#                 realpath.append(current)
#                 current = path[current[2]]
#             if len(realpath) <= live:
#                 return True
#             else:
#                 return False
#         for dir in dirs:
#             nextcode = dir(current[0],current[1])
#             if 0<=nextcode[0] <m and 0 <= nextcode[1] <n:
#                 if island[nextcode[0]][nextcode[1]] == 0:
#                     queue.append((nextcode[0],nextcode[1],len(path)-1))
#                     island[nextcode[0]][nextcode[1]] = 2
#
#     else:
#         return False
#
# a = deq(0,0,m-1,n-1,live)
# if a:
#     print("I'm winner#")
# else:
#     print("Game Over!")

# m = int(input())
# meaningless = 0
# win = 0
# for i in range(m):
#     num = int(input())
#     if num == 0:
#         meaningless += 1
#     else:
#         remain = ""
#         while num > 0:
#             q = num % 4
#             remain = str(q) + remain
#             num = num // 4
#         if len(remain) == 1:
#             remain = "0" + remain
#         if "0" in remain:
#             meaningless += 1
#         elif len(remain) == 2:
#             if remain[0] == "1" and remain[1] == "2":
#                 win += 1
#             elif remain[0] == "2" and remain[1] == "3":
#                 win += 1
#             elif remain[0] == "3" and remain[1] == "1":
#                 win += 1
# print(win,meaningless,sep="\n")
#
# n,m = map(int,input().split())
# island_values = []
# for i in range(1,n+1):
#     value = int(input())
#     island_values.append((i,value))

# n,m = map(int,input().split())
# how_many = 0
# for i in range(0,n+1):
#     sum1 = 0
#     for _ in str(i):
#         sum1 += int(_)
#     if sum1 <= m:
#         how_many += 1
# print(how_many)
# import sys
# input = sys.stdin.read
# data = input().split()
# n = int(data[0])
# m = int(data[1])
# p = [i for i in range(n+1)]
# def find(x):
#     if p[x] != x:
#         p[x] = find(p[x])
#     return p[x]
# def union(x,y):
#     if find(x) != find(y):
#         p[find(x)] = find(y)
# island_v = []
# index2 = 2
# max1 = 0
# for i in range(1,n+1):
#     island_value = int(data[index2])
#     if island_value > max1:
#         max1 = island_value
#     island_v.append((i,island_value))
#     index2 += 1
# for i in range(m):
#     a,b = int(data[index2]),int(data[index2+1])
#     union(a,b)
#     index2 += 2
# group_sum = [0] * (n + 1)
# for i in range(1, n + 1):
#     group_sum[find(i)] += island_v[i - 1][1]
#
# print(max(max(group_sum),max1))

# n = int(input())
# numb_list = [1,2,4,7,8,11,13,14]
# round1_time = (n-1) // 8
# then_num = (n-1) % 8
# anser = 15*round1_time + numb_list[then_num]
# print(anser)












































