n, m = map(int, input().split())
m -= 1
str_list = []
for i in range(n):
    str_list.append(chr(97 + m % 26))
    m //= 26
print("".join(str_list)[::-1])
# 神他妈的 26 进制