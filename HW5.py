import time

# 暴力算法
def matrix_chain_order_brute(P, i, j):
    if i == j:
        return 0

    min_scalar_mult = float('inf')

    for k in range(i, j):
        count = (matrix_chain_order_brute(P, i, k) +
                 matrix_chain_order_brute(P, k + 1, j) +
                 P[i - 1] * P[k] * P[j])

        if count < min_scalar_mult:
            min_scalar_mult = count

    return min_scalar_mult

# 動態規劃算法
def matrix_chain_order_dp(P):
    n = len(P) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                temp_cost = (m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j])

                if temp_cost < m[i][j]:
                    m[i][j] = temp_cost
                    s[i][j] = k

    return m[1][n], s

# 測試不同輸入規模並比較運行時間
input_sizes = [5, 10, 15, 20, 25]

for size in input_sizes:
    # 生成隨機矩陣維度
    matrix_chain_dimensions = [10] * (size + 1)

    # 測量暴力算法的運行時間
    start_time = time.time()
    min_scalar_mult_brute = matrix_chain_order_brute(matrix_chain_dimensions, 1, size)
    end_time = time.time()
    brute_force_time = end_time - start_time

    # 測量動態規劃算法的運行時間
    start_time = time.time()
    min_scalar_mult_dp, _ = matrix_chain_order_dp(matrix_chain_dimensions)
    end_time = time.time()
    dynamic_programming_time = end_time - start_time

    # 輸出結果
    print("輸入規模:", size)
    print("暴力算法運行時間:", brute_force_time, "秒")
    print("動態規劃算法運行時間:", dynamic_programming_time, "秒")
    print("---")
