"""04 - NumPy 形状操作

学习目标:
    - 掌握 reshape / flatten / transpose
    - 了解数组拼接与拆分
    - 理解拷贝(copy)与视图(view)
"""

import numpy as np                                # 导入 numpy 模块

# ===== 1. 改变形状 =====
print("--- 改变形状 ---")                          # 打印标题
arr = np.arange(12)                               # 创建 0-11 的一维数组
print("原数组:", arr)                             # 打印原数组

reshaped = arr.reshape(3, 4)                      # 改为3行4列（元素总数必须匹配）
print("reshape(3,4):\n", reshaped)                # 打印重塑后的数组

reshaped2 = arr.reshape(2, -1)                    # -1 表示自动计算该维度
print("reshape(2,-1):\n", reshaped2)              # 2行，列数自动算出为6

# ===== 2. 展平数组 =====
print("\n--- 展平 ---")                            # 打印标题
mat = np.array([[1, 2, 3], [4, 5, 6]])            # 创建2×3矩阵
print("原矩阵:\n", mat)                           # 打印原矩阵

flat1 = mat.flatten()                             # flatten() 返回一份副本
print("flatten:", flat1)                          # 打印 [1 2 3 4 5 6]

flat2 = mat.ravel()                               # ravel() 返回视图（不复制，更高效）
print("ravel:", flat2)                            # 打印结果相同

# ===== 3. 转置 =====
print("\n--- 转置 ---")                            # 打印标题
print("原矩阵形状:", mat.shape)                   # 打印 (2, 3)
transposed = mat.T                                # T 属性返回转置（行列互换）
print("转置后:\n", transposed)                    # 打印转置矩阵，形状变为 (3, 2)
print("转置形状:", transposed.shape)              # 打印 (3, 2)

# ===== 4. 数组拼接 =====
print("\n--- 拼接 ---")                            # 打印标题
a = np.array([[1, 2], [3, 4]])                    # 创建2×2矩阵 a
b = np.array([[5, 6]])                            # 创建1×2矩阵 b

vstack = np.vstack([a, b])                        # 垂直拼接（上下堆叠）
print("vstack:\n", vstack)                        # 结果为3×2矩阵

c = np.array([[7], [8]])                          # 创建2×1矩阵 c
hstack = np.hstack([a, c])                        # 水平拼接（左右拼接）
print("hstack:\n", hstack)                        # 结果为2×3矩阵

concat = np.concatenate([a, b], axis=0)           # axis=0 沿行方向拼接（等价 vstack）
print("concatenate(axis=0):\n", concat)           # 打印拼接结果

# ===== 5. 数组拆分 =====
print("\n--- 拆分 ---")                            # 打印标题
big = np.arange(12).reshape(2, 6)                 # 创建2×6数组
print("原数组:\n", big)                           # 打印原数组

split_arr = np.split(big, 3, axis=1)              # 沿列方向均分为3份
print("拆分结果:")                                # 打印提示
for i, part in enumerate(split_arr):              # 遍历拆分后的数组
    print(f"  第{i}块:\n", part)                  # 打印每一块

hsplit = np.hsplit(big, 2)                        # 水平拆分为2份（等价 split axis=1）
print("hsplit结果:", [p.shape for p in hsplit])   # 打印每块的形状

# ===== 6. 拷贝与视图 =====
print("\n--- 拷贝与视图 ---")                      # 打印标题
original = np.array([1, 2, 3, 4, 5])              # 创建原数组

# 视图：共享数据，修改一个会影响另一个
view = original.view()                            # view() 创建视图（共享内存）
view[0] = 99                                     # 修改视图
print("修改视图后原数组:", original)               # 原数组也变了 → [99 2 3 4 5]

# 深拷贝：独立数据，互不影响
original2 = np.array([1, 2, 3, 4, 5])             # 重新创建原数组
copy = original2.copy()                           # copy() 创建深拷贝（独立内存）
copy[0] = 99                                     # 修改副本
print("修改副本后原数组:", original2)              # 原数组不变 → [1 2 3 4 5]

# 切片默认返回视图
arr = np.array([1, 2, 3, 4, 5])                   # 创建数组
sub = arr[1:4]                                   # 切片得到视图
sub[0] = 99                                      # 修改切片
print("切片修改后原数组:", arr)                    # 原数组也变了 → [1 99 3 4 5]

# 想要独立副本，需要显式 copy()
arr2 = np.array([1, 2, 3, 4, 5])                  # 创建数组
sub2 = arr2[1:4].copy()                           # 切片后立即 copy()
sub2[0] = 99                                     # 修改副本
print("copy后原数组不变:", arr2)                   # 原数组不变 → [1 2 3 4 5]


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 把一维数组 reshape 成 3×3，再转置")   # 练习1
    print("2. 把两个 3×3 矩阵水平拼接成 3×6")      # 练习2
    print("3. 验证切片是视图还是副本（修改后看原数组）")  # 练习3
