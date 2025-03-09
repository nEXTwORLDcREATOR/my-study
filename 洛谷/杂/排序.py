# n,m = map(int,input().split())
# list_vote = [i for i in map(int,input().split())]
# list_vote.sort()
# print(*list_vote)

# def mub_sort(li):
#     for i in range(len(li)-1):
#         exchange = False
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#                 exchange =  True
#         if not exchange:
#             return
# n = int(input())
# list1 = [i for i in map(int,input().split())]
# mub_sort(list1)
# print(*list1)

# n = int(input())
# list2 = [i for i in map(int,input().split())]
# list2.sort()
# print(*list2)

# def select_sort(li):
#     for i in range(len(li)-1):
#         min_cal = i
#         for j in range(i,len(li)):
#             if li[j] < li[min_cal]:
#                 min_cal = j
#         li[min_cal],li[i] = li[i],li[min_cal]
#
# n = int(input())
# list3 = [i for i in map(int,input().split())]
# select_sort(list3)
# print(*list3)

# def insert_sort(name):
#     for i in range(1,len(name)):
#         tmp = name[i]
#         j = i-1
#         while j >= 0 and name[j] > tmp:
#             name[j+1]=name[j]
#             j -= 1
#         name[j+1] = tmp
# n = input()
# list1 = [i for i in map(int,input().split())]
# insert_sort(list1)
# print(*list1)

# n,k = map(int,input().split())
# list_num = list(i for i in map(int,input().split()))
#
# i = 1
# j = n-1
# while i < j:
#     mid = list_num[j//2]
#     while list_num[j] > mid:
#         j -= 1
#     while list_num[i] < mid:
#         i += 1
#     if i <= j:
#         list_num[i],list_num[j] = list_num[j],list_num[i]
#         i += 1
#         j -= 1

# def qsort(arr, l, r, k):
#     if l >= r:
#         return arr
#     i, j = l, r
#     mid = arr[(l + r) // 2]
#     while True:
#         while arr[j] > mid:
#             j -= 1
#         while arr[i] < mid:
#             i += 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#         if i > j:
#             break
#     # 快排后数组被划分为三块： l<=j<=i<=r
#     if k < j:
#         return qsort(arr, l, j, k)  # 在左区间只需要搜左区间
#     elif i < k:
#         return qsort(arr, i, r, k)  # 在右区间只需要搜右区间
#     else:
#         return arr[j]
#
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# qsort(arr, 0,n-1, k)
# print(qsort(arr, 0,n-1, k))

# n = input()
# list_a = [i for i in n]
# dict1 = dict.fromkeys(list_a,1)
# old = []
# for j in n:
#     if j in old:
#         dict1[j] += 1
#     else:
#         old.append(j)
# max_a = max(dict1.values())
# min_a = min(dict1.values())
#
# num = max_a - min_a
# zhi = True
# if num <= 2 and num > 1:
#     print('Lucky Word')
#     print(num)
# elif num == 0 or num ==1:
#     print('No Answer')
#     print(0)
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             zhi =  False
#     if zhi:
#         print('Lucky Word')
#         print(num)
#     else:
#         print('No Answer')
#         print(0)
#
# a,b = map(int,input().split())
# print(a+b+1)
# n = input()
# print(f'{n}是一个雷劈数')

# x,y = map(int,input().split())
# abs_x = abs(x)
# if abs_x >= 3:
#     print(5+int(y*0.1)+3)
# else:
#     print(5+int(y*0.1)+abs_x)

# n,m = map(int,input().split())
# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# n_m = m-1
# new = [0]*n
# j = 0
# # if n_m <= 9:
# #     for i in range(n):
# #         if i != n-1:
# #             new[i] = 'a'
# #         else:
# #             new[i] = alpha[n_m]
# for i in range(n):
#         new[i] = alpha[j]
# print(*new,sep="")

# t = int(input())
# for i in range(t):
#     n = input()
#     left = 0
#     right = len(n)-1
#     x = 0
#     y = 0
#     fu = True
#     while left < right:
#         if n[left] == '(':
#             x = left
#             left += 1
#         else:
#             left += 1
#
#         if n[right] == ")":
#             y = right
#             right -= 1
#         else:
#             right -= 1
#         if left >= right or x >= y:
#             fu = False
#     if fu:
#         print('Yes')
#     else:
#         print('No')

    # count_l = 0
    # count_r = 0
    # while True:
    #     if left < right:
    #         if n[left] == '(':
    #             count_l += 1
    #             left += 1
    #         else:
    #             left += 1
    #         if n[right] == ')':
    #             count_r += 1
    #             right -= 1
    #         else:
    #             right -= 1
    #     else:
    #         break
    # if count_r == count_l == (len(n)/2) and count_r !=0 and count_l != 0:
    #     print('Yes')
    # else:
    #     print('No')


# n = int(input())
# distance = [i for i in map(int,input().split())]
# x,y = map(int,input().split())
# i = x
# n_i = y
# l = 0
# n_l = 0
# while i != y:
#     l += distance[i]
#     i += 1
#     if i == y:
#         break
#     else:
#         if i >= n-1:
#             i = 0
# while n_i != x:
#     n_l += distance[n_i]
#     n_i += 1
#     if n_i == x:
#         break
#     else:
#         if n_i >= n-1:
#             n_i = 0
# print(min(n_l,l))

# n = int(input())
# distance = [i for i in map(int,input().split())]
# start, end = map(int, input().split())
#
# if start > end:
#     start, end = end, start
#
# sum_distance = sum(distance)
#
# clockwise = sum(distance[start:end])
# anticlockwise = sum_distance - clockwise
#
# ans = min(clockwise, anticlockwise)
#
# print(ans)



















# n,m,k = map(int,input().split())
# kg = 0
# value = 0
# for i in range(n):
#     w,s = map(int,input().split())
#     kg += w
#     value += s
# for j in range(m):
#     w, s = map(int, input().split())
#     kg += w
#     value += s
# value1 = value
# kg1 = kg
# for l in range(k):
#     w, s = map(int, input().split())
#     kg += w
#     value += s
# value = value * 0.8
# if value > value1:
#     print(kg,f'{value:.2f}')
# else:
#     print(kg1,f'{value1:.2f}')




# n = int(input())
# distance = [int(i) for i in input().split()]
# x, y = map(int, input().split())
#
# clockwise_distance = 0
# counterclockwise_distance = 0
#
# # 计算顺时针距离
# i = x
# while True:
#     clockwise_distance += distance[i]
#     i = (i + 1) % n  # 使用取模运算来确保索引在有效范围内
#     if i == y:
#         break
#
# # 计算逆时针距离
# n_i = x
# while True:
#     counterclockwise_distance += distance[n_i]
#     n_i = (n_i - 1 + n) % n  # 使用取模运算来确保索引在有效范围内，先减1再取模
#     if n_i == y:
#         break
#
# print(min(clockwise_distance, counterclockwise_distance))


n, m = map(int, input().split())
m -= 1
str_list = []
for i in range(n):
    str_list.append(chr(97 + m % 26))
    m //= 26
print("".join(str_list)[::-1])

































