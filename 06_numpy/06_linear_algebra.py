"""06 - NumPy 线性代数

学习目标:
    - 掌握矩阵乘法与行列式
    - 了解逆矩阵与方程求解
    - 理解特征值与特征向量
"""

import numpy as np                                # 导入 numpy 模块

# ===== 1. 矩阵乘法 =====
print("--- 矩阵乘法 ---")                          # 打印标题
A = np.array([[1, 2], [3, 4]])                    # 创建2×2矩阵 A
B = np.array([[5, 6], [7, 8]])                    # 创建2×2矩阵 B

result = A @ B                                    # @ 运算符：矩阵乘法（推荐写法）
print("A @ B =\n", result)                        # 打印矩阵乘积

result2 = np.dot(A, B)                            # np.dot() 等价于 @
print("np.dot(A, B) =\n", result2)                # 打印结果（相同）

# 矩阵乘向量
v = np.array([1, 2])                              # 创建向量
print("A @ v =", A @ v)                           # 矩阵乘向量 → [5 11]

# ===== 2. 行列式与迹 =====
print("\n--- 行列式与迹 ---")                      # 打印标题
det = np.linalg.det(A)                            # 计算行列式（determinant）
print(f"行列式 det(A) = {det:.1f}")               # 打印行列式值 → -2.0

trace = np.trace(A)                               # 计算矩阵的迹（对角线元素之和）
print(f"迹 trace(A) = {trace}")                   # 打印迹 → 5 (1+4)

# ===== 3. 逆矩阵 =====
print("\n--- 逆矩阵 ---")                          # 打印标题
inv = np.linalg.inv(A)                            # 计算逆矩阵
print("逆矩阵 A⁻¹ =\n", inv)                      # 打印逆矩阵

# 验证：A @ A⁻¹ = 单位矩阵
identity = A @ inv                                # 矩阵乘以逆矩阵
print("A @ A⁻¹ =\n", np.round(identity, 10))      # round 四舍五入，应接近单位矩阵

# ===== 4. 解线性方程组 =====
print("\n--- 解线性方程组 ---")                    # 打印标题
# 解方程组: 2x + y = 5
#           x + 3y = 10
coeffs = np.array([[2, 1], [1, 3]])               # 系数矩阵
constants = np.array([5, 10])                     # 常数项向量
solution = np.linalg.solve(coeffs, constants)     # 求解方程组
print("解 x, y =", solution)                       # 打印解 → [1. 3.]
# 验证: 2×1 + 3 = 5 ✓, 1 + 3×3 = 10 ✓
print("验证:", coeffs @ solution)                 # 应等于 [5, 10]

# ===== 5. 特征值与特征向量 =====
print("\n--- 特征值与特征向量 ---")                # 打印标题
M = np.array([[2, 1], [1, 3]])                    # 创建对称矩阵
eigenvalues, eigenvectors = np.linalg.eig(M)      # 计算特征值和特征向量
print("特征值:", eigenvalues)                      # 打印特征值
print("特征向量:\n", eigenvectors)                 # 打印特征向量（每列对应一个特征向量）

# ===== 6. 常用线性代数函数 =====
print("\n--- 其他线性代数 ---")                    # 打印标题
C = np.array([[1, 2, 3], [4, 5, 6]])              # 创建2×3矩阵

print("矩阵的秩:", np.linalg.matrix_rank(C))      # 矩阵的秩（线性无关的行/列数）
print("Frobenius范数:", np.linalg.norm(C))        # 矩阵的F范数（所有元素平方和再开根号）

# 奇异值分解(SVD)
U, S, Vt = np.linalg.svd(C)                       # 奇异值分解：A = U @ Σ @ V^T
print("奇异值:", S)                               # 打印奇异值
print("U:\n", U)                                  # 打印左奇异向量
print("Vt:\n", Vt)                                # 打印右奇异向量的转置

# ===== 7. 实战: 最小二乘法拟合直线 =====
print("\n--- 最小二乘拟合 ---")                    # 打印标题
x = np.array([1, 2, 3, 4, 5])                     # x 坐标数据
y = np.array([2.1, 3.9, 6.2, 8.1, 10.0])          # y 坐标数据（约等于 y=2x）

# 用最小二乘法拟合 y = k*x + b
A_fit = np.vstack([x, np.ones(len(x))]).T         # 构造系数矩阵 [[1,1],[2,1],...]
k, b = np.linalg.lstsq(A_fit, y, rcond=None)[0]   # 最小二乘求解
print(f"拟合直线: y = {k:.2f}x + {b:.2f}")         # 打印拟合结果

# 预测
x_new = 6                                         # 新的 x 值
y_pred = k * x_new + b                            # 预测 y 值
print(f"预测 x={x_new} 时 y={y_pred:.2f}")        # 打印预测结果


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 验证矩阵乘法不满足交换律: A@B ≠ B@A")  # 练习1
    print("2. 解方程组 3x+2y=7, x-y=1")            # 练习2
    print("3. 用最小二乘法拟合一组数据的直线方程")    # 练习3
