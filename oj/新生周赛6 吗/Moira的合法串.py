t = int(input())

for _ in range(t):
    str_input = input()
    cnt = 0
    flag = 1

    for char in str_input:
        if char == '(':
            cnt += 1
        else:
            if cnt:
                cnt -= 1
            else:
                flag = 0
                break

    if flag and not cnt:
        print("Yes")
    else:
        print("No")
# 栈 优雅无需多言