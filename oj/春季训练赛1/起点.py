n,m = map(int,input().split())
list_in = [input().strip() for i in range(m)]
for i in list_in:
    if i == "A":
        A = [_ for _ in range(1,2*n,2)]
        print(*A)
    elif i == "B":
        B = [_ for _ in range(2,2*n+1,2)]
        print(*B)
    elif i == "C":
        C = [15*p for p in range(1,n+1)]
        print(*C)
    else:
        D = []
        m = 0
        for _ in range(15*n):
            if m < n and _ % 5 != 0 and _ % 3 != 0:
                D.append(_)
                m += 1
        print(*D)