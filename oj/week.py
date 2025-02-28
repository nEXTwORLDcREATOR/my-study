# from cgitb import reset
# from idlelib.pyparse import C_NONE
# import math
# x,y = map(int,input().split())
# c = x**2 + y**2
# nm = math.sqrt(c)
# def function(k):
#     if k <= 10:
#         return k
#     elif 10 < k <= 50:
#         return k + function(k - 5)
#     elif 50 < k <= 100:
#         return k + function(k - 20)
# result = function(nm)
# print(f'{result:.4f}')
# from itertools import count
# from stringprep import c22_specials
from itertools import count, permutations
from operator import index

# i = 1
# while i < 520:
#     print("回应我吧，爱莉希雅！")
#     i += 1

# x = int(input("请输入讨厌的数字 x（x 不为 1）："))
# current_year = 2024
# original_age = 50000
# actual_age = 0
#
# for year in range(1, current_year + 1):
#     if str(x) not in str(year) and year % x!= 0:
#         actual_age += 1
#
# print(f"符华如今实际年龄为{actual_age}岁。")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, "*", i, "=", j * i, end=" ")
#         j += 1
#     print()
#     i += 1

# i =1
# while i <= 9:
#     j =1
#     while j <= i:
#         print(j,"*",i,"=",j*i,sep="",end=" ")
#         j +=1
#     print()
#     i +=1
# #
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f'{j}*{i}={j * i}', end=' ')
#         j += 1
#     print()
#     i += 1

# a,b,c = map(int,input().split())
# print(c,b,a)

# a,b,c = map(int,input())
# print(c,b,a)

# a,b = map(int,input().split())
# c = a * 2**b
# print(c)

# a = input()
# c = int(ord(a))
# print(c * 2)

# numbs = 0
# a,b = map(int,input().split())
# for n in range(a,b):
#     for x in range(2,n):
#         if n % x == 0:
#             break
#     else:
#         numbs += 1
# print(numbs)

# a, b, d = map(int, input().split())
# n = (b - a) // d + 1
# s = n * (a + b) // 2
# print(s)

# n,x,y = map(int,input().split())
# a = y // x
# e = y % x
# if e > 0:
#     a += 1
#     print(n-a)
# else:
#     print(n-a)

# a,b,c = map(int,input().split())
# print(a+b+c)

# idcard = input()
# print(idcard[6:10],"-",idcard[10:12],"-",idcard[12:14],sep="")

# n,m = map(int,input().split())
# tuzi = (m-2*n)//2
# ji = n - ((m-2*n)//2)
# print(ji,tuzi)
#
# m,n,k = map(int,input().split())
# day=1
# while day % 2 == 0:
#     n = k * 6 + n
# else:
#     n = k * 8 + n
# day += 1
# if n >= m:
#     print(day)


# m, n, k = map(int, input().split())
# day = 1
# while True:
#     if day % 2 == 0:
#         n = k * 6 + n
#     else:
#         n = k * 8 + n
#         if n >= m:
#             print(day)
#             break
#     day += 1

#
# m, n, k = map(int, input().split())
# day = 0
# while True:
#     day += 1
#     if day % 2 == 0:
#         n = k * 6 + n
#     else:
#         n = k * 8 + n
#
#     if n >= m:
#         print(day)
#         break

# m, n, k = map(int, input().split())
# day = 0
# while n < m:
#     day += 1
#     if day % 2 == 0:
#         n += k * 6
#     else:
#         n += k * 8
# print(day)


#
# m, n, k = map(int, input().split())
# # 假设需要 x 天追上芽衣
# # 第奇数天修炼 8 小时，第偶数天修炼 6 小时，平均每天修炼 7 小时
# # 那么 x 天修炼的总量为 7kx
# # 追上芽衣时，修炼总量等于芽衣的战斗力与初始战斗力之差
# x = (m - n) / (7 * k)
# if x % 1!= 0:
#     x = int(x) + 1
# print(int(x))

# grid = [input() for _ in range(10)]
# mine_count = sum(row.count('*') for row in grid)
# result_grid = [list(row) for row in grid]
#
# def count_mines(x, y):
#     count = 0
#     for i in range(max(0, x - 1), min(10, x + 2)):
#         for j in range(max(0, y - 1), min(10, y + 2)):
#             if grid[i][j] == '*':
#                 count += 1
#     return count
#
# for i in range(10):
#     for j in range(10):
#         if grid[i][j]!= '*':
#             count = count_mines(i, j)
#             result_grid[i][j] = str(count)
#
# print(mine_count)
# for row in result_grid:
#     print(''.join(row))

# a,b,c,d = map(int,input().split())
# time = (c * 60 + d)-(a * 60 + b)
# print(time//60,time % 60)

# s = [1, 2, 3, 4, 5]
# s.insert(0,7)
#
# s.pop(2)
# print(s)

# a,b = map(int,input().split())
# c,d = map(int,input().split())
# if a * c > 2147483647 or b * d >2147483647:
#     print("long long int")
# elif a * d < -2147483648 or b * c < -2147483648:
#     print("long long int")
# else:
#     print("int")

# nums = [3,4,5,32,56,333,21,2,5,7,8]
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)
# print(nums.count(5))
# print(nums.index(4))  #下标
# b = nums.copy()
# print(b)
# b = nums
# print(b)
# print(b[-1])
# b.insert(-1,0)
# print(b)
# print(len(nums))

# print(f"p={pow(1 + 0.07,10):.2f}")

# import math
# d = 300000
# p = 6000
# r = 0.01
# m = math.log(p / (p-d*r)) / math.log(1 + r)
# print(f"m={m:.1f}")

# x,y = map(int,input().split())
# y,x = x,y
# print(x,y)
#
# c1 = 'C'
# c2 = 'h'
# c3 = 'i'
# c4 = 'n'
# c5 = 'a'
#
# c1 = chr(ord(c1)+4)
# c2 = chr(ord(c2)+4)
# c3 = chr(ord(c3)+4)
# c4 = chr(ord(c4)+4)
# c5 = chr(ord(c5)+4)
# print(f"{c1}{c2}{c3}{c4}{c5}")

# a,b,c = map(int,input().split())
# i = [a,b,c]
# i.sort()
# for n in i:
#     print(f"{n}",end=" ")

# n = int(input())
# if n > 0:
#     print("positive")
# elif n == 0:
#     print('zero')
# else:
#     print('negative')

# a,b,s,t = map(int,input().split())
# if s/a < s/b+t:
#     print('Turtle win')
# elif s/a > s/b+t:
#     print('Rabbit win')
# else:
#     print('Tie')


# import cmath,math
# a,b,c = map(int,input().split())
# n = b**2 - 4*a*c
# if a == 0:
#     print('This is not a quradratic equation')
# if n > 0:
#     s = math.sqrt(n)
#     a1 , a2 = (-b + s)/(2*a) , (-b - s)/(2*a)
#     print(f'{a1:.2f}',f'{a2:.2f}')
# elif n == 0:
#     a3 = (-b )/(2*a)
#     print(f'{a3:.2f}')
# else:
#     s = cmath.sqrt(n)
#     a1, a2 = (-b + s) / (2 * a), (-b - s) / (2 * a)
#     print(f'{a1:.2f}'.replace('j','i'), f'{a2:.2f}'.replace('j','i'))

# n = int(input())
# if n % 2 == 0:
#     print('even')
# else:
#     print('odd')

# n = int(input())
# if n % 4 == 0 and n % 100 != 0:
#     print(f'{n} is a leep year')
# else:
#     print(f'{n} is not a leap year')
#
# year = int(input())
# if (year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# a,b = map(int,input().split())
# n = [a,b]
# print(max(n))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     for each in i:
#         print(each,end=" ")
#     print()

# a = [1,2,3,4,5]
# print(len(a))
# print(range(len(a)))
# score = int(input())
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f"{grade}")

# num = float(input())
# if num > 0:
#     result = int(num)
# else:
#     result = int(num // 1)
# print(result)

# num = float(input())
# if num > 0:
#     result = int(num)
# else:
#     if num % 1 == 0:
#         result = int(num)
#     else:
#         result = int(num)
# print(result)

# num = float(input())
# print(int(num))

# a,b,c = map(int,input().split())
# print(max(a,b,c),min(a,b,c))

# a,b,c = input().split()
# a = float(a)
# b = float(b)
# result = a c b
# print(f'{result:.2f}')

# num1, operator, num2 = input().split()
# num1 = float(num1)
# num2 = float(num2)
#
# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 == 0:
#         result = None
#     else:
#         result = num1 / num2
# else:
#     result = None
#
# if result is not None:
#     print(f"{result:.2f}")

# amount = float(input())
# if amount < 500:
#     pay_amount = amount
# elif amount < 1000:
#     pay_amount = amount * 0.95
# elif amount < 3000:
#     pay_amount = amount * 0.9
# elif amount < 5000:
#     pay_amount = amount * 0.85
# else:
#     pay_amount = amount * 0.8
# print(f"{pay_amount:.2f}")

# A = 1,2,3,4,5,"上山打老虎"
# A[0]
# x = eval(input())
# if x < 1:
#     a = x
# elif 1 <= x < 10:
#     a = 2*x - 1
# elif x >= 10:
#     a = 3*x - 11
# print(f'y={a:.2f}')

# import math
# def building_height(x, y):
#     centers = [(2, 2), (-2, 2), (-2, -2), (2, -2)]
#     radius = 1
#     height = 0
#     for center in centers:
#         cx, cy = center
#         distance = math.sqrt((x - cx)**2 + (y - cy)**2)
#         if distance <= radius:
#             height = 10
#             break
#     return height
# while True:
#     input_str = input()
#     parts = input_str[1:4].split(",")
#     x = float(parts[0])
#     y = float(parts[1])
#     height = building_height(x, y)
#     print(f"{height}")

# w1,w2,w3 = input()
# word = [w1,w2,w3]
# word.sort()
# w1 = word[0]
# w2 = word[1]
# w3 = word[2]
# print(w1,w2,w3,sep='')

# t = int(input())
# if t <= 160:
#     m = t * 10
#     print(m)
# elif t > 160:
#     m = 1600 + (t - 160)*30
#     print(m)

# x,y = map(int,input().split())
# if y in [1,3,5,7,8,10,12]:
#     days = 31
# elif y in [4,6,9,11]:
#     days = 30
# else:
#     if (x % 4 == 0 and x % 100 != 0)or x % 400 == 0:
#         days = 29
#     else:
#         days = 28
# print(days)
# import math
# x,y = map(float,input().split())
# s = math.sqrt(x**2 + y**2)
# if s < 4.5:
#     print('in')
# elif s == 4.5:
#     print('on')
# else:
#     print('out')

# word = input()
# fruit = {'A':'Apple',
#          'B':'Banana',
#          'C':'Cherry',
#          'D':'Durian'}
# print(fruit.get(word,'Mango'))
#
# sum = 0
# m,n = map(int,input().split())
# for i in range(m,n+1):
#     sum += i
# print(sum)

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break
#
# n = int(input())
# s = 0
# i = 0
# while s < n:
#     i += 1
#     s += i
# print(i)
#
# n = int(input())
# if n < 2:
#     print('No')
# else:
#     p = True
#     for i in range(2,n):
#         if n % i == 0:
#             p = False
# if p == True:
#     print('yes')
# else:
#     print('No')

# n = int(input())
# if n < 2:
#     print('No')
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print('Yes')
#     else:
#         print('No')

# 1
# -2/3
# 3/5
# -4/7
#
# (-1)**2*(N/2N-1)
# sum = 0
# def f(x):
#     return (-1)**(x+1)*(x/(2*x - 1))
# sum = 0
# n = int(input())
# for i in range(1,n+1):
#     sum += f(i)
# print(f'{sum:.3f}')
#
# print('You can do anything you set your mind to mian.',end="\n")
#
# n = int(input())
# for i  in range(2,n):
#     if n % i == 0 :
#         print("No")
#         break
# else:
#     print("Yes")
# try:
#     n = int(input())
#     if n < 2:
#         print("No")
#     else:
#         is_prime = True
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print("Yes")
#         else:
#             print("No")
# except ValueError:
#     print("请输入有效的整数。")

# a,b = map(int,input().split())
# for i in range(a,b+1):
#     if i % 3 != 0:
#         print(f'{i}',end=" ")
# x = 0
# m = int(input())
# while True:
#     try:
#         y = int((m-7*x)/4)
#         z = int(m - x -y)
#         if 5*x + 3*y + z/3 == m:
#             print(x,y,z,sep=" ")
#             break
#         else:
#             x += 1
#     except:
#         print("No answer")

# x = 0
# m = int(input())
# while True:
#     y = int((m-7*x)/4)
#     z = int(m - x -y)
#     if 5*x + 3*y + z/3 == m:
#         if x < 0 or y < 0 or z < 0:
#             print("No answer")
#             break
#         else:
#             print(x,y,z,sep=" ")
#             break
#     x += 1

# n = int(input())
# count = 1
# if n < 10 :
#     print("1")
# else:
#     while n >= 10:
#         n //= 10
#         count += 1
#     print(count)
# n,s,m = map(int,input().split())
# sum = 0
# for i in range(n):
#     l,r = map(int,input().split())
#     x = r - l
#     sum += x
# if m - sum >= s :
#     print("Bang Dream it’s MyGO!!!")
# else:
#     print("你这个人只想着你自己")

# n = int(input())
# y = []
# for i in range(n):
#     a,b,c,d = input().split()
#     sum = int(b) + int(c) + int(d)
#     m = [a,sum]
#     y.append(m)
# y.sort()
# import random
# number = [10,1,2,3,4,5,6,7,8,9]
# number.sort(reverse=True)
# print(number)

# new = [5,4,3,2,1]
# old = [1,2,3,4,5]
# a = old.index(1)
# print(new[a])

# a = {"吕布":"口口布","关羽":"关习习"}
# b = dict(吕布="口口布",关羽="关习习")
# c = dict([("吕布","口口布")])

# x1,y1,x2,y2 = map(int,input().split())
# x3,y3,x4,y4 = map(int,input().split())














# w = False
# n = int(input())
# if n <= 2 :
#     w = False
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             w = True
# if w == True:
#     print('I will win')
# else:
#     print('tui you')

# n = int(input())
# student = []
# for i in range(n):
#     name,yu,shu,ying = input().split()
#     total_scores = int(yu) + int(shu) + int(ying)
#     student.append((name,total_scores))
# new = sorted(student,key= lambda x : (-x[1],x[0]))
# for name,total_scores in new:
#     print(name,total_scores)

# n = int(input())
# reversed_num = 0
# is_negative = False
# if n < 0:
#     is_negative = True
#     n = -n
# while n > 0:
#     reversed_num = reversed_num * 10 + n % 10
#     n //= 10
# if is_negative:
#     print(-reversed_num)
# else:
#     print(reversed_num)

# fan = 0
# n = int(input())
# fushu = False
# if n < 0:
#     fushu = True
#     n = -n
# while n > 0:
#     fan = (fan * 10) + (n % 10)
#     n //= 10
# if fushu == True:
#     print(-fan)
# else:
#     print(fan)
# s = []
# n = int(input())
# for i in range(n):
#     if str(4) not in str(i):
#         s.append(i)
# print(len(s))

# i = 2
# n = int(input())
# s = []
# while n > 1:
#     if n % i:
#         i += 1
#     else:
#         s.append(i)
#         n /= i
# print(*s,sep="*")

# n,a = map(int,input().split())
# s = a
# sum = 0
# for i in range(n):
#     sum += a
#     a = a*10 + s
# print(sum)

# result = 1
# n = int(input())
# for i in range(1,n+1):
#     result *= i
# top = str(result)
# print(top[0])


# x,y = 0,0
# speed = 10
# fx0 = 1 #默认方向指向北
# ftime = 0
# ntime = 0
# def fx2(a):
#     global x, y
#     if a == 1:
#         y = y + speed * ftime
#     elif a == 2:
#         x = x + speed * ftime
#     elif a == 3:
#         y = y - speed * ftime
#     else:
#         x = x - speed * ftime
# while True:
#     try:
#
#         time,fx = map(int,input().split())
#         ftime = time - ntime
#         ntime = time
#
#         if fx == 1:
#             fx2(fx0)
#             fx0 = fx0 - 1 if fx0 > 1 else 4
#
#         elif fx == 2:
#             fx2(fx0)
#             fx0 = (fx0 + 1)%4
#
#         else:
#             fx2(fx0)
#             break
#     except:
#         break
# print(x,y)

# x, y = 0, 0
# speed = 10
# direction = 1  # 1: north, 2: east, 3: south, 4: west
# last_time = 0
#
# while True:
#     try:
#         time, command = map(int, input().split())
#         time_interval = time - last_time
#         last_time = time
#         if direction == 1:  # north
#             y += time_interval * speed
#         elif direction == 2:  # east
#             x += time_interval * speed
#         elif direction == 3:  # south
#             y -= time_interval * speed
#         else:  # west
#             x -= time_interval * speed
#         if command == 1:
#             direction = direction - 1 if direction > 1 else 4
#         elif command == 2:
#             direction = direction % 4 + 1
#         else:
#             break
#     except:
#         break
# print(x, y)






























