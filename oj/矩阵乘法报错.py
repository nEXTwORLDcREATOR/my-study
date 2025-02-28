
m, p, n = map(int, input().split())

A = []
for _ in range(m):
    A.append(list(map(int, input().split())))

B = []
for _ in range(p):
    B.append(list(map(int, input().split())))

result = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        for k in range(p):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(*row)
#矩阵乘法 在计算阶段出现报错 提示A越界