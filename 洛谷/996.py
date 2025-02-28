def count_and_list_combinations(n):
    results = []

    def backtrack(remaining, path, index):
        # 如果剩余美味程度为0，且已经分配了所有10种调料
        if remaining == 0 and index == 10:
            results.append(path.copy())
            return
        # 如果已经分配完所有调料但仍有剩余，或者剩余小于0，剪枝
        if index == 10 or remaining < 0:
            return
        # 尝试为当前调料分配1到3克
        for weight in range(1, 4):
            path[index] = weight
            backtrack(remaining - weight, path, index + 1)
            path[index] = 0  # 回溯

    # 如果总美味程度小于10，则无法满足每种调料至少1克
    if n < 10:
        return results

    backtrack(n, [0] * 10, 0)
    return results


# 读取输入
n = int(input())

# 计算所有组合
combinations = count_and_list_combinations(n)

# 输出结果
print(len(combinations))
for combo in combinations:
    print(' '.join(map(str, combo)))