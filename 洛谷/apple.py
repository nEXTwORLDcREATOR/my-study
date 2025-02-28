# n = int(input())
# if n == 0 or n == 1:
#     print(f'Today, I ate {n} apple.')
# else:
#     print(f'Today, I ate {n} apples.')
# # 上面是正确版本
#
# n = int(input())
# if n == 0 or 1:
#     print(f'Today, I ate {n} apple.')
# else:
#     print(f'Today, I ate {n} apples.')
# #这是错误版本
#


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 读取 n 和 m
    n = int(data[0])
    m = int(data[1])

    # 初始化并查集
    p = [i for i in range(n + 1)]  # 父节点数组，从 1 到 n
    rank = [1] * (n + 1)  # 按秩合并的秩数组

    # 并查集的 find 函数
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    # 并查集的 union 函数（按秩合并）
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                p[root_y] = root_x
                rank[root_x] += rank[root_y]
            else:
                p[root_x] = root_y
                rank[root_y] += rank[root_x]

    # 读取每个岛屿的宝藏价值
    island_v = []
    index = 2
    max1 = 0
    for i in range(1, n + 1):
        island_value = int(data[index])
        island_v.append((i, island_value))
        if island_value > max1:
            max1 = island_value
        index += 1

    # 读取 m 条路，进行 union 操作
    for _ in range(m):
        x = int(data[index])
        y = int(data[index + 1])
        union(x, y)
        index += 2

    # 统计每个连通分量的权重和
    group_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        group_sum[find(i)] += island_v[i - 1][1]

    # 找到最大权重和
    max_sum = 0
    for i in range(1, n + 1):
        if group_sum[i] > max_sum:
            max_sum = group_sum[i]

    # 输出结果
    print(max(max_sum, max1))


if __name__ == "__main__":
    main()


