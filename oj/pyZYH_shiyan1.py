# import math
# up = math.pow(1+0.001,365)
# down = math.pow(1-0.001,365)
# gap = up - down
# print('向上:{:.4f},虚度:{:.4f}'.format(up,down))
# print('好好学习与虚度光阴一年能量差值为：{:.4f}'.format(gap))
from pickle import PROTO

# pm = int(input('请输入PM2.5指数：\n'))
# if pm<35:
#     print('空气优，适合户外活动')
# elif pm<75:
#     print('空气良，可适度户外活动！')
# else:
#     print('空气差，请注意！')

# n = eval(input('请输入买了几箱苹果：'))
# price = 0
# cost = 55
# if n == 1:
#     price=55
# elif n == 2:
#     price = cost * n * 0.8
# else:
#     price = cost * n * 0.7
# print('消费金额为：',price)

# n = int(input("请输入一个整数："))
# s = 0
# for i in range(2,n+1,2):
#     s = s + i
# print("1~n之间的偶数之和是{}".format(s))

# n = int(input("请输入项数："))
# a,b = 1,2
# s = 1.0
# for i in range(1,n):
#     s = s + a/b
#     b = a + b
#     a = i + 1
# print("和是{:.2f}".format(s))

# f1 = 0
# f2 = 1
# while f1 <= 200:
#     print(f1,end=" ")
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3）
# nubs = int(input())
# a = nubs // 100
# b = (nubs // 10) % 10
# c = nubs % 10
# if a**3 + b**3 + c**3 == 100*a + b*10 + c:
#     print("该三位数是水仙花数")
# else:
#     print("该三位数不是水仙花数")

# while True:
#     score = int(input("请输入学生成绩（输入负值结束程序）："))
#     if score < 0:
#         break
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'E'
#     print(f"成绩等级为：{grade}")


n = 0
a = 0
b = 1
while n <25:
    print(f"{a:5}",end=" ")
    n += 1
    if n % 5 == 0:
        print()
    a = b
    b = a + b



















