# n,m = map(int,input().split())
# if n >= 0 and m >= 0 :
#     print(n*m)

# n = input()
# new_n = n.upper()
# print(new_n)

# old = float(input())
# old_str = str(old)
# new_str = old_str[::-1]
# new = float(new_str)
# print(new)

# t,n = map(eval,input().split())
# ml = t/n
# beizi = n*2
# print(f'{ml:.3f}')
# print(beizi)
# import math
# a,b,c = map(eval,input().split())
# p = (a+b+c)/2
# squ = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f'{squ:.1f}')

# import math
# h,r = map(int,input().split())
# pi = 3.14
# ml = (pi*r**2)*h
# l = ml/1000
# t_num = math.ceil(20/l)
# print(t_num)

# a,b,c,d = map(int,input().split())
# fenzhong = (c*60 + d) - (a*60 + b)
# e = fenzhong//60
# f = fenzhong%60
# print(e,f,sep=" ")

# a,b = map(int,input().split())
# jiao = a*10 + b
# bi = jiao//19
# print(bi)

# a,b,c = map(int,input().split())
# total = int((a*0.2) + (b*0.3) + (c*0.5))
# print(total)

# x = int(input())
# xz1 = False
# xz2 = False
# if x%2 == 0 :
#     xz1 = True
# if x > 4 and x <= 12:
#     xz2 = True
# if xz1 and xz2:
#     a = 1
# else:
#     a = 0
# if xz1 or xz2:
#     uim = 1
# else:
#     uim = 0
# if xz1 and not xz2 or xz2 and not xz1:
#     b = 1
# else:
#     b = 0
# if not xz1 and not xz2:
#     z = 1
# else:
#     z = 0
# print(a,uim,b,z,sep=" ")

# n = int(input())
# if n%4==0 and n%100!=0 or n%400==0:
#     print(1)
# else:
#     print(0)

# n = int(input())
# if n == 0 or n == 1:
#     print(f'Today, I ate {n} apple.')
# else:
#     print(f'Today, I ate {n} apples.')

# n = int(input())
# luo = 0
# local = 0
# luo = 11 + 3*n
# local = 5 * n
# if luo < local:
#     print('Luogu')
# else:
#     print('Local')

# mad = False
# list1 = []
# for i in range(1,8):
#     a,b = map(int,input().split())
#     list1.append(a+b)
# max_mad = max(list1)
# if max_mad > 8:
#     a = list1.index(max_mad)+1
# else:
#     a = 0
# max_mad= max(list1)
# print(a)
# import math
# n = int(input())
# a1,b1 = map(int,input().split())
# a2,b2 = map(int,input().split())
# a3,b3 = map(int,input().split())
# m1 = math.ceil(n/a1) * b1
# m2 = math.ceil(n/a2) * b2
# m3 = math.ceil(n/a3) * b3
# min_m = min(m1,m2,m3)
# print(min_m)

# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
# l1 = list(map(int,input().split())) # list() 要注意！！！
# l1.sort()
# if is_triangle(l1[0],l1[1],l1[2]):
#     a = l1[0]
#     b = l1[1]
#     c = l1[2]
#     if a**2 + b**2 == c**2 :
#         print('Right triangle')
#     if a**2 + b**2 > c**2 :
#         print('Acute triangle')
#     if a**2 + b**2 < c**2 :
#         print('Obtuse triangle')
#     if a == b or a == c or b == c:
#         print('Isosceles triangle')
#     if a == b == c:
#         print('Equilateral triangle')
# else:
#     print('Not triangle')

# n = int(input())
# if n <= 150:
#     print('%.1f' % (n*0.4463))
# if n > 150 and n <= 400:
#     print('%.1f' % (150*0.4463 + (n-150)*0.4663))
# if n > 400:
#     print('%.1f' % (150*0.4463 + 250*0.4663 + (n-400)*0.5663))

# list1 = list(map(int,input().split()))
# high = int(input())
# list1.sort()
# for i in list1:
#     if i > high+30:
#         print(list1.index(i))
#         break

# list1 = list(map(int,input().split()))
# step = input()                      
# list1.sort()
# for i in step:
#     if i == 'A':
#         print(list1[0],end=" ")
#     if i == 'B':
#         print(list1[1],end=" ")
#     if i == 'C':
#         print(list1[2],end=" ")

# n = input()
# total = 0
# new_n = ""
# for i in n:
#     if i.isdigit():
#         new_n += i
# for i in range(1,10):
#     total += int(new_n[i-1]) * i
# id = total % 11
# if id == 10:
#     id = 'X'
# if str(id) == n[-1] :
#     print('Right')
# else:
#     n = n[:-1] + str(id)
#     print(n)



# n = int(input())
# a = n
# t = 0
# for i in range(n):
#     for j in range(a):
#         t += 1
#         print(f'{t:02}',end='')
#     print()
#     a -= 1
# n = int(input())
# s = "".join([f'{i:02d}' for i in range(1, n * (n + 1) // 2 + 1)])
# row = n
# index = 0
# while row > 0:
#     for _ in range(row):
#         print(s[index:index + 2], end='')
#         index += 2
#     print()
#     row -= 1

# import math
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += math.factorial(i)
# print(sum)

# n,x = map(int,input().split())
# sum = 0
# for i in range(1,n+1):
#     if str(x) in str(i):
#         sum += str(i).count(str(x))
# print(sum)

# k = int(input())
# sum = 0
# a = 0
# while sum < k:
#     a += 1
#     sum += 1/a
# print(a)





























