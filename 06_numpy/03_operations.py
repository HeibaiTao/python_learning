"""03 - NumPy 数组运算

学习目标:
    - 掌握逐元素运算与广播机制
    - 了解通用函数(ufunc)
    - 理解向量化计算的优势
"""

import numpy as np                                # 导入 numpy 模块

# ===== 1. 逐元素运算 =====
print("--- 逐元素运算 ---")                        # 打印标题
a = np.array([1, 2, 3, 4])                        # 创建数组 a
b = np.array([10, 20, 30, 40])                    # 创建数组 b

print("a + b:", a + b)                            # 逐元素相加 → [11 22 33 44]
print("a - b:", a - b)                            # 逐元素相减
print("a * b:", a * b)                            # 逐元素相乘（不是矩阵乘法！）
print("b / a:", b / a)                            # 逐元素相除
print("b ** 2:", b ** 2)                          # 每个元素的平方

# 标量运算（数组与单个数字）
print("a + 10:", a + 10)                          # 每个元素加10
print("a * 2:", a * 2)                            # 每个元素乘2

# ===== 2. 通用函数(ufunc) =====
print("\n--- 通用函数 ---")                        # 打印标题
arr = np.array([0, np.pi/2, np.pi])               # 创建角度数组（弧度制）

print("sin:", np.sin(arr))                        # 正弦函数
print("cos:", np.cos(arr))                        # 余弦函数
print("sqrt:", np.sqrt(a))                        # 开平方
print("exp:", np.exp(a))                          # e的指数 e^x
print("log:", np.log(np.array([1, np.e, np.e**2])))  # 自然对数

# ===== 3. 广播机制 =====
print("\n--- 广播机制 ---")                        # 打印标题
# 广播：不同形状的数组运算时，自动扩展小数组
matrix = np.array([[1, 2, 3],                     # 2×3 矩阵
                   [4, 5, 6]])
row = np.array([10, 20, 30])                      # 1×3 行向量

print("矩阵 + 行向量:\n", matrix + row)           # 行向量自动广播到每一行
# [[11 22 33]
#  [14 25 36]]

col = np.array([[100], [200]])                    # 2×1 列向量
print("矩阵 + 列向量:\n", matrix + col)           # 列向量自动广播到每一列
# [[101 102 103]
#  [204 205 206]]

# ===== 4. 矩阵运算 =====
print("\n--- 矩阵运算 ---")                        # 打印标题
A = np.array([[1, 2], [3, 4]])                    # 创建2×2矩阵 A
B = np.array([[5, 6], [7, 8]])                    # 创建2×2矩阵 B

print("A @ B (矩阵乘法):\n", A @ B)               # @ 是矩阵乘法（点积）
print("A.dot(B):\n", A.dot(B))                    # 等价写法
print("A.T (转置):\n", A.T)                       # 转置矩阵（行列互换）

# ===== 5. 聚合运算 =====
print("\n--- 聚合运算 ---")                        # 打印标题
data = np.array([[1, 2, 3], [4, 5, 6]])           # 创建2×3数组

print("总和:", data.sum())                        # 所有元素求和 → 21
print("按列求和:", data.sum(axis=0))              # axis=0 沿列方向求和 → [5 7 9]
print("按行求和:", data.sum(axis=1))              # axis=1 沿行方向求和 → [6 15]

print("最大值:", data.max())                      # 全局最大值 → 6
print("每列最大:", data.max(axis=0))              # 每列最大值 → [4 5 6]
print("最小值:", data.min())                      # 全局最小值 → 1
print("平均值:", data.mean())                     # 全局平均值 → 3.5
print("标准差:", data.std())                      # 标准差

# argmax/argmin 返回索引
flat = np.array([3, 7, 2, 9, 1])                  # 创建一维数组
print("最大值索引:", flat.argmax())               # 返回最大值的索引 → 3
print("最小值索引:", flat.argmin())               # 返回最小值的索引 → 4

# ===== 6. 向量化 vs 循环对比 =====
print("\n--- 向量化优势 ---")                      # 打印标题
big_arr = np.arange(1000000)                      # 创建100万元素数组

# 用循环求平方（慢）
import time                                       # 导入时间模块
start = time.time()                               # 记录开始时间
result_loop = np.zeros(1000000)                   # 预分配结果数组
for i in range(1000000):                          # 循环100万次
    result_loop[i] = big_arr[i] ** 2              # 逐个求平方
loop_time = time.time() - start                   # 计算耗时

# 用向量化求平方（快）
start = time.time()                               # 记录开始时间
result_vec = big_arr ** 2                         # 一行搞定，底层用C加速
vec_time = time.time() - start                    # 计算耗时

print(f"循环耗时: {loop_time:.4f}秒")             # 打印循环耗时
print(f"向量化耗时: {vec_time:.6f}秒")            # 打印向量化耗时
print(f"向量化快 {loop_time/vec_time:.0f} 倍")    # 打印加速倍数


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 用广播机制将矩阵每列减去该列的均值")  # 练习1：数据标准化
    print("2. 计算 3×3 矩阵的行列式和逆矩阵")      # 练习2：线性代数
    print("3. 对比 for 循环和向量化计算 100万数的平方")  # 练习3：性能对比
