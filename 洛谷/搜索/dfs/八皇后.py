# def is_vaild(board,raw,col):
#     for i in range(raw):
#         if board[i][col] == 1:
#             return False
#
#     i = raw-1
#     j = col-1
#     while i >= 0 and j >=0:
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j -= 1
#
#     i = raw-1
#     j = col+1
#     while i >= 0 and j < len(board):
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j += 1
#     return True
# def backtrack(board,raw):
#     if raw == len(board):
#         result = []
#         for r in board:
#             queen_col = r.index(1) + 1
#             result.append(queen_col)
#         result_sum.append(result)
#     for col in range(n):
#         if is_vaild(board,raw,col):
#             board[raw][col] = 1
#             backtrack(board,raw+1)
#             board[raw][col] = 0
#
# n = int(input())
# board = [[0]*n for i in range(n)]
# result_sum = []
# backtrack(board,0)
# result_sum.sort()
# j=0
# for i in result_sum:
#     if j <= 2:
#         j+=1
#         print(*i)
# print(len(result_sum))
#
# n = int(input())
# result = []

def backtrack(row=0, cols=0, diag1=0, diag2=0, queens=[]):
    if row == n:
        # 生成解：queens中的每个元素+1（列从1开始编号）
        result.append([col + 1 for col in queens])
        return
    # 计算当前行所有可用的列（二进制位为1表示可用）
    available = ~(cols | diag1 | diag2) & ((1 << n) - 1)
    while available:
        # 取最低位的1（快速定位可放置的位置）
        col = available & -available
        # 将该位置从available中移除
        available ^= col
        # 将col转换为列索引（例如0b100对应col=2）
        col_idx = (col).bit_length() - 1
        # 递归下一行，更新cols、diag1、diag2的状态
        backtrack(
            row + 1,
            cols | col,
            (diag1 | col) << 1,
            (diag2 | col) >> 1,
            queens + [col_idx]
        )

backtrack()
# 按字典序输出
for solution in result:
    print(' '.join(map(str, solution)))