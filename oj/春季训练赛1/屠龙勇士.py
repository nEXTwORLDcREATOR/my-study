m = int(input())
meaningless = 0
win = 0
for i in range(m):
    num = int(input())
    if num == 0:
        meaningless += 1
    else:
        remain = ""
        while num > 0:
            q = num % 4
            remain = str(q) + remain
            num = num // 4
        if len(remain) == 1:
            remain = "0" + remain
        if "0" in remain:
            meaningless += 1
        elif len(remain) == 2:
            if remain[0] == "1" and remain[1] == "2":
                win += 1
            elif remain[0] == "2" and remain[1] == "3":
                win += 1
            elif remain[0] == "3" and remain[1] == "1":
                win += 1
print(win,meaningless,sep="\n")