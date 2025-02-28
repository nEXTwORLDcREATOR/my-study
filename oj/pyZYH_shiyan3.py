# def area(width,height):
#     return width * height
#
# def print_welcome(name):
#     print('Welcome',name)
#
# print_welcome("Hue")
# w = 4
# h = 5
# print("width =",w,"height =",h,"area =",area(w,h))

# def printme( str ):
#     print(str)
#     return
#
# printme( str = "新手教程")
#
# def printinfo( name, age ):
#     print("名字：",name)
#     print("年龄：",age)
#     return
#
# printinfo( age=18,name="小明" )
# print ("-----------------------------")
# printinfo( name="小明" )


# def fun(n):
#     hundreds_digit = n // 100
#     tens_digit = (n // 10) % 10
#     units_digit = n % 10
#     return n == hundreds_digit ** 3 + tens_digit ** 3 + units_digit ** 3
# n = int(input())
# print(fun(n))

# def isPrime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# n = int(input())
# print(isPrime(n))

# def gcd(a, b):
#     while b!= 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# a,b = map(int,input().split())
# print(gcd(a,b),lcm(a,b))

# fo = open("test.txt","w")
# print("文件名为：",fo.name)
# seq = ['河南工程学院 1\n',"河南工程学院 2"]
# fo.writelines( seq )
#
# fo.close()
#
# fo = open("test.txt","r+")
# print("文件名为：",fo.name)
#
# line = fo.readline()
# print('读取的数据为：%s' % (line))
#
# pos = fo.tell()
# print("当前位置： %d " % (pos))
#
# fo.close()

# import csv
# headers=["工号","姓名","年龄","地址","月薪"]
# rows=[("1001","赵琦","18","桐柏路62号","5000"),("1002","笑笑","19","祥和路1号","6000")]
# with open(r"d:\python\b.csv","w") as b:
#     b_csv=csv.writer(b)
#     b_csv.writerow(heders)
#     b_csv.writerows(rows)
# with open(r"d:\python\b.csv") as a:
#     a_csv=csv.reader(a)
#     heders=next(a_csv)
#     for row in a_csv:
#         print(row)

# import os
# import os.path
# path=os.getcwd()
# file_list=os.listdir(path)
# for filename in file_list:
#     pos=filename.rfind(".")
#     if filename[pos+1]=="py":
#         print(filename,end="\n")
# print("############")
# file_list2=[filename for filename os.listfir(path) if filename.endswith(".py")]
# for filename in file_list2:
#     print(filename,end="\t")

# def calculate(num1, num2, oper="+"):
#     if oper == "+":
#         return num1 + num2
#     elif oper == "-":
#         return num1 - num2
#     elif oper == "*":
#         return num1 * num2
#     elif oper == "/":
#         if num2 == 0:
#             raise ValueError("除数不能为零")
#         return num1 / num2
#     else:
#         raise ValueError("无效的运算符，只能接收'-'、'*'、'/'符号")
#
# def can_be_divided(n):
#     if n % 2 == 0 and n % 7 == 0:
#         return True
#     return False
# a= int(input())
# print(can_be_divided(a))

# def calculate_product():
#     product = 1
#     for i in range(3, 21):
#         product *= i
#     return product
#
# print(calculate_product())

# import os
# def process_data_file(name_initial):
#     # 打开data.txt文件
#     with open(r"E:\pythonProject\data.txt", "r+", encoding="utf-8") as file:
#         content = file.read()
#
#         # 找到“欢迎”所在位置并插入“非常”
#         insert_index = content.find("欢迎")
#         if insert_index!= -1:
#             content = content[:insert_index] + "非常" + content[insert_index:]
#
#         # 将文件指针移到文件末尾追加名言
#         file.seek(0, 2)
#         file.write("\n书籍是人类进步的阶梯。")
#
#         # 保存修改后的内容
#         file.seek(0)
#         file.write(content)
#
#     # 重命名文件
#     os.rename("data.txt", f"data_ZYH.txt")