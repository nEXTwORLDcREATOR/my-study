#1058
# a,b = map(int,input().split())
# ji = a * b
# ji2 = str(ji)
# ji3 = ji2[::-1]
# ji4 = ji3.lstrip("0")
# print(ji4)
#
# a,b = map(int,input().split())
# yue = []
# for i in range(2,a+1):
#     if a % i ==0 and b % i == 0:
#         yue.append(i)
# answer = max(yue)
# print(answer)
#
# a,b = map(int,input().split())
# y = 1
# while True:
#     s = a * y
#     if s % b  == 0 :
#         break
#     else:
#         y += 1
# print(s)
from itertools import count
from multiprocessing.connection import answer_challenge

# from Crypto.SelfTest.Cipher.test_DES3 import index
from charset_normalizer.cd import characters_popularity_compare

# a, b = map(int, input().split())
#
# def gcd(x, y):
#     while y!= 0:
#         x, y = y, x % y
#     return abs(x)
#
# print(gcd(a, b))

# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f'{a}*{b}=',a*b,sep="",end=" ")
#     print()

# n = int(input())
# for i in range(n):
#     m = int(input())
#     for each in range(1,m+1):
#         for e in range(each,10):
#             print(f'{each}*{e}=',each*e,sep="",end=" ")
#         print()
#     print()



# s = input ("一行字符，可以包含字母、数字、空格、标点等符号 \n")
# characters = 0
# spaces = 0
# numbers = 0
# others = 0
# for char in s:
#     if char.isalpha ():
#         characters += 1
#     elif char.isspace ():
#         spaces += 1
#     elif char.isdigit ():
#         numbers += 1
#     else:
#         others += 1
# print (f"characters={characters}")
# print (f"spaces={spaces}")
# print (f"numbers={numbers}")
# print (f"others={others}")
#
# s = input()
# characters = 0
# spaces = 0
# numbers = 0
# others = 0
# for char in s:
#     if char.isalpha():
#         characters += 1
#     elif char.isspace():
#         spaces += 1
#     elif char.isdigit():
# #         numbers += 1
#     else:
#         others += 1
# print(f'characters={characters}')
# print(f'spaces={spaces}')
# print(f'numbers={numbers}')
# print(f'others={others}')

#
# sum = 0
# n = int(input())
# for i in range(1,n+1):
#     x = 1
#     for each in range(2,i+1):
#         x *= each
#     sum += x
# print(sum)
# s = 0
# for i in range(1,101):
#     s += i
# l = 0
# for i in range(1,51):
#     l += i * i
# m = 0
# for i in range(1,11):
#     m += 1/i
# sum = s+l+m
# print(f'{sum:.6f}')

# for i in range(100,1000):
#     if ((i % 10)**3 + ((i//10)%10)**3 + ((i//100)%10)**3) == i :
#         print(i)

# while True:
#     x = int(input())
#     if x == 0 :
#         break
#     count = 0
#     for b in range(x+1):
#         a = x - 2*b
#         if a >= 0:
#             count += 1
#     print(count)

# n = int(input())
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n * f(n-1)
# print(f(n))
# z = []
# you = False
# a,b,c = map(int,input().split())
# for i in range(10,101):
#     if i % 3 == a and i % 5 == b and i % 7 == c:
#         z.append(i)
#         you = True
# if you == True:
#     print(min(z))
# else:
#     print('No answer')
# 1069
# n = int(input())
# length = 0
# high = 100
# if n == 1:
#     length = 100
# else:
#     while n > 0:
#         high /= 2
#         length += 2*high
#         n -= 1
# print(f'length={length:.4f}')
# print(f'high={high:.4f}')


# n = int(input())
# if n == 0 :
#     print(0)
# else:
#     binary = ""
#     while n > 0:
#         binary = str(n%2) + binary
#         n //= 2
#     print(binary)

# n = int(input())
# value = list(map(int, input().split()))
# x = int(input())
# value.append(x)
# value.sort()
# for _ in value:
#     print(_,end=" ")

# m = list(map(int,input().split()))
# n = list(map(int,input().split()))
# l = []
# l.extend(m[1:])
# l.extend(n[1:])
# l.sort(reverse=True)
# for each in l:
#     print(each,end=" ")

# n = int(input())
# l = list(map(int,input().split()))
# m = min(l)
# z = l.index(m)
# print(m,z,sep=" ")
# 1075
# vote = []
# while True:
#     x= int(input())
#     if x < 0:
#         break
#     vote.append(x)
# vote_num = {}
# for each in vote :
#     if each in vote_num:
#         vote_num[each] += 1
#     else:
#         vote_num[each] = 1
# max_count = max(vote_num.values())
# most_populer = [k for k,v in vote_num.items() if v == max_count]
# most_populer.sort()
# print(*most_populer,sep=" ")

n = int(input())
numb_list = list(map(int,input().split()))
aim = int(input())
if aim in list:
    print(index(aim))
else:
    print(-1)

































