def matrix_chain_order(P):
    n = len(P) - 1  # 鏈中的矩陣數量

    # 創建並初始化數組
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i - 1][j - 1] = float('inf')
            for k in range(i, j):
                temp_cost = m[i - 1][k - 1] + m[k][j - 1] + P[i - 1] * P[k] * P[j]
                if temp_cost < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = temp_cost
                    s[i - 1][j - 1] = k

    return m[0][n - 1], s


def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i - 1][j - 1])
        print_optimal_parenthesization(s, s[i - 1][j - 1] + 1, j)
        print(")", end="")


# 範例使用
matrix_chain_dimensions = [5, 10, 3, 12, 5, 50]  # 鏈中各個矩陣的尺寸
min_scalar_mult, s = matrix_chain_order(matrix_chain_dimensions)
print("最小純量乘法次數：", min_scalar_mult)
print("最佳括號化方式：", end="")
print_optimal_parenthesization(s, 1, len(matrix_chain_dimensions) - 1)
