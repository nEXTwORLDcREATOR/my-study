# list1 = []
# while True:
#     n = input()
#     if n:
#         list1.extend(i for i in n)
#     else:
#         break

# s = []
# n,m = 10,10
# for i in range(n):
#     s.append([i for i in input()])
#
# directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
# total = 0
# for j in range(n):
#     for k in range(m):
#         a = s[j][k]
#         if a == '*':
#             total += 1
#         if a == '0':
#             count = 0
#             for direction in directions:
#                 new_j = j + direction[0]
#                 new_k = k + direction[1]
#                 if 0 <= new_j < n and 0 <= new_k < m:
#                     if s[new_j][new_k] == '*':
#                         count += 1
#             s[j][k] = str(count)
# print(total)
# for _ in s:
#     print(*_,sep="")
# def animal(a,b,c):
#     while True:
#         animal(a,c,b)

# a,b = map(eval,input().split())
# a_multiplied = int(a * 10)
# b_multiplied = int(b * 10)
# result_multiplied = a_multiplied + b_multiplied
# result = result_multiplied / 10
# print(result)
'''
模拟竖式加法
a = input()
b = input()

# 确保a的长度不小于b的长度，如果不是则交换
if len(a) < len(b):
    a, b = b, a

result = ""
carry = 0  # 进位

# 从个位开始逐位相加
for i in range(-1, -len(a) - 1, -1):
    digit_a = int(a[i])
    digit_b = int(b[i]) if abs(i) <= len(b) else 0

    sum_digits = digit_a + digit_b + carry
    carry = sum_digits // 10
    result += str(sum_digits % 10)

# 如果最高位还有进位，添加进位
if carry:
    result += str(carry)

print(result[::-1])
'''





















