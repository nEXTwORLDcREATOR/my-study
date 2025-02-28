#模拟竖式加法
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

