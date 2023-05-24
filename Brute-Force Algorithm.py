def matrix_chain_mult(P, i, j):
    if i == j:
        return 0

    min_scalar_mult = float('inf')

    for k in range(i, j):
        # 計算左子鏈和右子鏈的純量乘法次數
        left_mult = matrix_chain_mult(P, i, k)
        right_mult = matrix_chain_mult(P, k + 1, j)

        # 計算當前括號化方式的總純量乘法次數
        current_mult = left_mult + right_mult + P[i - 1] * P[k] * P[j]

        # 如果需要，更新最小純量乘法次數
        if current_mult < min_scalar_mult:
            min_scalar_mult = current_mult

    return min_scalar_mult


def matrix_chain_order(P):
    n = len(P) - 1  # 鏈中的矩陣數量
    min_scalar_mult = matrix_chain_mult(P, 1, n)

    return min_scalar_mult


# 範例使用
matrix_chain_dimensions = [5, 10, 3, 12, 5, 50]  # 鏈中各個矩陣的尺寸
min_scalar_mult = matrix_chain_order(matrix_chain_dimensions)
print("最小純量乘法次數：", min_scalar_mult)
