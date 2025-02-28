# n = int(input())
# numb_list = list(map(int,input().split()))
# aim = int(input())
# if aim in numb_list:
#     print(numb_list.index(aim)+1)
# else:
#     print(-1)
#
# old_str = input()
# new_str = ""
# for each in old_str:
#     if each.isdigit():
#         new_str += each
# result = int(new_str) * 2
# print(result)


# dict1 = dict(((1,'Mon'),(2,'Tue'),(3,'Wed'),(4,'Thur'),(5,'Fri'),(6,'Sat'),(7,'Sun')))
# x = int(input())
# print(dict1[x])

# binary_str = input()
# decimal_num = int(binary_str, 2)
# hex_str = hex(decimal_num)[2:]
#
# print(hex_str)
#
# n = input()
# num = n.count(' ')
# print(num + 1)

# n = list(input().split())
# print(max(n))
# raw = []
# n = int(input())
# for i in range(n):
#     s = list(map(int,input().split()))
#     raw.append(s)
# is_shangsanjiao = True
# for i in range(n):
#     for j in range(i):
#         if raw[i][j] != 0:
#             is_shangsanjiao = False
#             break
#     if is_shangsanjiao == False:
#         break
# if is_shangsanjiao:
#     print('Yes')
# else:
#     print('No')

# m,p,n = map(int,input().split())
# A = []
# for _ in range(m):
#     juzhen = list(map(int,input().split()))
#     A.append(juzhen)
# B = []
# for _ in range(p):
#     juzhen2 = list(map(int,input().split()))
#     B.append(juzhen2)
#
# result = [[0]*n for _ in range(m)]
#
# for i in range(m):
#     for j in range(n):
#         for k in range(p):
#             result[i][j] += A[i][k]*B[k][j]
# for each in result:
#     print(*each)


# m, p, n = map(int, input().split())

# A = []
# for _ in range(m):
#     A.append(list(map(int, input().split())))
#
# B = []
# for _ in range(p):
#     B.append(list(map(int, input().split())))
#
# result = [[0] * n for _ in range(m)]
#
# for i in range(m):
#     for j in range(n):
#         for k in range(p):
#             result[i][j] += A[i][k] * B[k][j]
#
# for row in result:
#     print(*row)

# try:
#     m, p, n = map(int, input().split())
#
#     A = []
#     for _ in range(m):
#         row = list(map(int, input().split()))
#         if len(row)!= p:
#             raise ValueError(f"矩阵 A 的行应该有 {p} 个元素，输入错误。")
#         A.append(row)
#
#     B = []
#     for _ in range(p):
#         row = list(map(int, input().split()))
#         if len(row)!= n:
#             raise ValueError(f"矩阵 B 的行应该有 {n} 个元素，输入错误。")
#         B.append(row)
#
#     result = [[0] * n for _ in range(m)]
#
#     for i in range(m):
#         for j in range(n):
#             for k in range(p):
#                 result[i][j] += A[i][k] * B[k][j]
#
#     for row in result:
#         print(*row)
#
# except ValueError as e:
#     print(e)
# s = []
# old = input()
# old = old.lower()
# for each in old:
#     if each.isalpha():
#         s.append(each)
# word = {}
# for i in s:
#     if i not in word:
#         word[i]=1
#     else:
#         word[i] += 1
# most = max(word.values())
# most_word = [v for v,k in word.items() if k==most]
# most_word.sort()
# print(most_word[0])

#
# y,m,d = map(int,input().split())
# days_in_mouth = [31,28,31,30,31,30,31,31,30,31,30,31]
# if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#     days_in_mouth[1]=29
# days = sum(days_in_mouth[:m-1])+d
# print(days)

# n,m = map(int,input().split())
# s = [range(1,n+1)]
# for _ in range(m):
#     x,y = map(int,input().split())
#     s.extend(range(x,y+1))
# l = {}
# for each in s:
#     if each not in l:
#         l[each]= 1
#     else:
#         l[each]+=1
# most = max(l.values())
# xuanshou = [k for k,v in l.items() if v == most]
# xuanshou.sort()
# print(*xuanshou)

# n, m = map(int, input().split())
# scores = [0] * n
# for _ in range(m):
#     l, r = map(int, input().split())
#     for i in range(l - 1, r):
#         scores[i] += 1
#
# max_score = max(scores)
# winners = [i + 1 for i, score in enumerate(scores) if score == max_score]
# print(*winners)

# n,m = map(int,input().split())
# scors = [0] * n
# for _ in range(m):
#     x,y = map(int,input().split())
#     for i in range(x-1,y):
#         scors[i] += 1
# max_scores = max(scors)
# winner = [v+1 for v,k in enumerate(scors) if k == max_scores]
# winner.sort()
# print(*winner)

# n = int(input())
# sam = [[1]*(i+1)for i in range(n)]
# for i in sam:
#     for j in sam[]:
#



# num=input()
# l_num=num.split()
# n=int(l_num[0])
# m=int(l_num[1])
# score={}
# for i in range(1,n+1):
#     score[i]=0
# for i in range(1,m+1):
#     num = input()
#     l_num = num.split()
#     l= int(l_num[0])
#     r= int(l_num[1])
#     for j in range(l,r+1):
#         score[j]+=1
# for k in range(1,n+1):
#     if score[k]==max(score.values()):
#         print(k,end='')
# n = int(input())
# N = list(map(int,input().split()))
# N.sort()
# print(*N,end=" ")
# total = []
# one = list(map(int,input().split()))
# two = list(map(int,input().split()))
# three = list(map(int,input().split()))
# total.extend([one,two,three])
# sumed = 0
# for _ in range(3):
#     sumed += total[_][_]
# print(sumed)
# for _ in range(3):
#     alpha = str()
#     digits = str()
#     space = str()
#     others = str()
#     words = input()
#     for each in words:
#         if each.isalpha():
#             alpha += each
#         elif each.isdigit():
#             digits += each
#         elif each.isspace():
#             space += each
#         else:
#             others += each
#     print(len(alpha),len(digits),len(space),len(others),sep=" ")
    #每次循环要重置！！！！


# words = input()
# new_word = str()
# for each in words:
#     if each.isalpha():
#         if each.isupper():
#             new_each = chr(ord('A')+ord('Z')-ord(each))
#         elif each.islower():
#             new_each = chr(ord('a') + ord('z') - ord(each))
#     else:
#         new_each = each
#     new_word += new_each
# print(new_word)
#
# m,n = map(int,input().split())
# for i in range(m,n+1):
#     if i == 1:
#         continue
#     ans = True
#     for j in range(2,i):
#         if i % j == 0 :
#             ans = False
#             break
#     if ans :
#         print(i,end=" ")

# import math
#
# m, n = map(int, input().split())
# for i in range(m, n + 1):
#     if i == 1:
#         continue
#     ans = True
#     sqrt_i = int(math.sqrt(i)) + 1
#     for j in range(2, sqrt_i):
#         if i % j == 0:
#             ans = False
#             break
#     if ans:
#         print(i, end=" ")
# import math
# n = input()
# x,y = map(float,n[1:-1].split(","))
# r = 1
# height = 0
# zuobiao = [(-2,2),(2,2),(-2,-2),(2,-2)]
# for each in zuobiao:
#     cx,cy = each
#     if math.sqrt((cx - x)**2 + (cy - y)**2) <= r:
#         height = 10
#         break
# print(height)

# n = int(input())
# sanjiao = []
# for i in range(n):
#     row = [1] * (i + 1)
#     if i > 1:
#       prev_row = sanjiao[i - 1]
#       for j in range(1,i):
#           row[j] = prev_row[j-1] + prev_row[j]
#     sanjiao.append(row)
#
# for row in sanjiao:
#     for i in row:
#         print(f'{i:<8}',end=" ")
#     print()

# a,b = map(int,input().split())
# print(a + b)
# import math
# s,v = map(int,input().split())
# time = math.ceil(s / v)
# total = 470
# new_total = total - time
# if new_total > 0 :
#     h = new_total // 60
#     m = new_total % 60
# else:
#     new_total = new_total * (-1)
#     total2 = 1440
#     new_total2 = total2 - new_total
#     h = new_total2 // 60
#     m = new_total2 % 60
# print(f'{h:0>2}:{m:0>2}')


# import math
# m,t,s = map(int,input().split())
# if t == 0:
#     print(0)
# else:
#     chile = math.ceil(s/t)
#     if chile > m:
#         print(0)
#     else:
#         print(m - chile)
# def binary_search(li,val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right)//2
#         if li[mid] == val:
#             if mid == 0 or li[mid - 1]< val:
#                 return mid + 1
#             else:
#                 right = mid -1
#         elif li[mid] > val:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         return -1
#
# n,m = map(int,input().split())
# list1 = list(map(int,input().split()))
# val1 = list(map(int,input().split()))
# for val in val1:
#     print(binary_search(list1,val),end=" ")

# n,c = map(int,input().split())
# list1 = list(map(int,input().split()))
# count = 0
# for i in list1:
#     for j in list1:
#         if i - j == c:
#             count += 1
# print(count)
# for each in list1:
#     aim = each - c
#     left = 0
#     right = len(list1) - 1
#     while left <= right:
#         mid = (left + right)//2
#         if list1[mid] == aim:
#             count += 1
#             break
#         elif list1[mid] > aim:
#             right = mid - 1
#         else:
#             left = mid + 1
# print(count)

# n, c = map(int, input().split())
# nums = list(map(int, input().split()))
#
# nums.sort()

# count = 0
# for num in nums:
#     target = num - c
#     left, right = 0, n - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] == target:
#             count += 1
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
# print(count)






















































