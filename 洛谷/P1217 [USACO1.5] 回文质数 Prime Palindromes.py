import math
a,b = map(int,input().split())
for i in range(a,b+1):
    zhi = True
    if str(i) == str(i)[::-1] and i % 2 != 0:
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0 :
                zhi = False
                break
            else:
                continue
        if zhi:
            print(i)
# TLE emmm........