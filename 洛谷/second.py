
# b,c = map(int,input().split())
# t = int(input())
# a = 0
# while b >= 2 and t >=4:
#     b-=2
#     a+=1
#     t-=4
# if c >= 4 and b==1 and t>=6:
#     a+=1
#     b-=1
#     c-=4
#     t-=6
# while c >=8 and t>=8:
#     c-=8
#     a+=1
#     t-=8
# print(a)

# l = int(input())
# total = 0
# count = 0
# num = 2
# while total < l:
#     zhi = True
#     for j in range(2,num):
#         if num % j == 0:
#             zhi = False
#             break
#     if zhi:
#         if l >= total + num:
#             print(num)
#             total += num
#             count += 1
#         else:
#             break
#     num += 1
# print(count)

# import math
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     zhi = True
#     if str(i) == str(i)[::-1] and i % 2 != 0:
#         for j in range(2,int(math.sqrt(i)+1)):
#             if i % j == 0 :
#                 zhi = False
#                 break
#             else:
#                 continue
#         if zhi:
#             print(i)

# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#
#     p = 2
#     while p * p <= n:
#         if is_prime[p]:
#             i = p * p
#             while i <= n:
#                 is_prime[i] = False
#                 i += p
#         p += 1
#
#     return [i for i in range(2, n + 1) if is_prime[i]]
#
#
# a, b = map(int, input().split())
# primes = sieve_of_eratosthenes(b)
#
# for prime in primes:
#     if prime >= a and str(prime) == str(prime)[::-1]:
#         print(prime)


# import math
# a,b = map(int,input().split())
# list1 = [0] * (b-a)
# for i in range(a,int(math.sqrt(b))):
#     if list1[i-a] == 0:
#         for j in range(i,b+1,i):
#             if list1[j] == 0 and j != i:
#                 list1[j] = 1
# for each in list1:
#     if each == 1:
#         print()


# on = input()
# if on == "-0" :
#     print("-0")
# else:
#     n = int(on)
#     if n >= 0 :
#         print(str(n)[::-1])
#     else:
#         n_n = "-" + str(n)[::-1][:-1].lstrip("0")
#         print(n_n)
#
#
# n = int(input())
# if n >= 0 :
#     print(str(n)[::-1])
# else:
#     n_n = "-" + str(n)[::-1][:-1].lstrip("0")
#     print(n_n)


# n = int(input())
#
# if n >= 0:
#     reversed_num = int(str(n)[::-1])
#     print(reversed_num)
# else:
#     reversed_negative_num = int("-" + str(abs(n))[::-1].lstrip("0"))
#     print(reversed_negative_num)

# n = int(input())
# a = (((1+(5**0.5))/2)**n - ((1-(5**0.5))/2)**n)/5**0.5
# print(f'{a:.2f}')

# n = int(input())
# if n == 1:
#     print(1)
# else:
#     for i in range(2,n):
#         for j in range(2,int((i**0.5)+1):
#             if i % j == 0:

# n = int(input())
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         print(n // i)
#         break

# n = int(input())
# list1 = [i for i in map(int,input().split())]
# max_g = max(list1)
# min_g = min(list1)
# list1.remove(max_g)
# list1.remove(min_g)
# total = 0
# for j in list1:
#     total += j
# total_s = total/(n-2)
# print(f'{total_s:.2f}')

# n = int(input())
# list1 = [i for i in map(int,input().split())]
# tot = 0
# while tot <= n-1:
#     count = 0
#     va_tot = 0
#     for j in list1:
#         if j < list1[tot] and va_tot < tot:
#             count += 1
#             va_tot += 1
#         else:
#             if j >= list1[tot] and va_tot < tot:
#                 va_tot += 1
#                 continue
#             elif va_tot >= tot:
#                 break
#     print(count,end=" ")
#     if tot + 1 > n-1:
#         break
#     else:
#         tot += 1


# list1 = [i for i in map(int,input().split())]
# list1.pop()
# list1.reverse()
# print(*list1)

















































































































