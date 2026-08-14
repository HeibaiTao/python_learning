"""05 - NumPy 统计与排序

学习目标:
    - 掌握常用统计方法
    - 理解排序与去重
    - 了解文件读写
"""

import numpy as np                                # 导入 numpy 模块

# ===== 1. 基本统计 =====
print("--- 基本统计 ---")                          # 打印标题
data = np.array([23, 45, 12, 67, 34, 89, 56, 78, 90, 11])  # 创建成绩数组

print("数据:", data)                              # 打印数据
print("总和:", data.sum())                        # 求和
print("均值:", data.mean())                       # 平均值
print("中位数:", np.median(data))                 # 中位数
print("方差:", data.var())                        # 方差（每个点与均值差的平方的均值）
print("标准差:", data.std())                      # 标准差（方差的平方根）
print("最小值:", data.min())                      # 最小值
print("最大值:", data.max())                      # 最大值
print("极差:", data.max() - data.min())           # 极差（最大值减最小值）

# ===== 2. 百分位数 =====
print("\n--- 百分位数 ---")                        # 打印标题
print("25%分位:", np.percentile(data, 25))        # 第25百分位数（下四分位数）
print("50%分位:", np.percentile(data, 50))        # 第50百分位数（等于中位数）
print("75%分位:", np.percentile(data, 75))        # 第75百分位数（上四分位数）

# ===== 3. 累积运算 =====
print("\n--- 累积运算 ---")                        # 打印标题
arr = np.array([1, 2, 3, 4, 5])                   # 创建数组
print("累积和:", np.cumsum(arr))                   # 累积求和 → [1 3 6 10 15]
print("累积积:", np.cumprod(arr))                  # 累积求积 → [1 2 6 24 120]

# ===== 4. 排序 =====
print("\n--- 排序 ---")                            # 打印标题
unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])    # 创建未排序数组

sorted_arr = np.sort(unsorted)                    # np.sort() 返回排序后的副本
print("排序后:", sorted_arr)                       # 打印 [1 1 2 3 4 5 6 9]
print("原数组不变:", unsorted)                     # 原数组未被修改

# 原地排序
unsorted2 = np.array([3, 1, 4, 1, 5])             # 创建新数组
unsorted2.sort()                                  # .sort() 原地排序（修改原数组）
print("原地排序后:", unsorted2)                    # 原数组已被排序

# 排序索引
unsorted3 = np.array([30, 10, 40, 20])            # 创建数组
indices = np.argsort(unsorted3)                   # argsort 返回排序后的索引顺序
print("排序索引:", indices)                        # 打印 [1 3 0 2]（10在索引1，20在索引3...）
print("按索引取值:", unsorted3[indices])           # 用索引重排 → [10 20 30 40]

# ===== 5. 去重与计数 =====
print("\n--- 去重与计数 ---")                      # 打印标题
dup = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])   # 创建有重复元素的数组

unique = np.unique(dup)                           # 去重，返回唯一值
print("去重:", unique)                             # 打印 [1 2 3 4]

unique, counts = np.unique(dup, return_counts=True)  # 去重并统计每个值出现次数
print("各值次数:", dict(zip(unique, counts)))      # 打印 {1:1, 2:2, 3:3, 4:4}

# ===== 6. 二维统计 =====
print("\n--- 二维统计 ---")                        # 打印标题
matrix = np.array([[85, 90, 78],                  # 学生成绩：3人×3科
                   [72, 88, 95],
                   [90, 85, 82]])

print("成绩矩阵:\n", matrix)                      # 打印矩阵
print("每人总分:", matrix.sum(axis=1))            # 沿行求和（每人的总分）
print("每科平均:", matrix.mean(axis=0))           # 沿列求均值（每科平均分）
print("每人最高分:", matrix.max(axis=1))          # 每人三科中的最高分
print("最高分在哪个科目:", matrix.argmax(axis=1))  # 每人最高分的列索引

# ===== 7. 文件读写 =====
print("\n--- 文件读写 ---")                        # 打印标题
save_data = np.array([[1, 2, 3], [4, 5, 6]])      # 创建要保存的数组

np.save("06_numpy/data/save.npy", save_data)      # 保存为 .npy 二进制文件
loaded = np.load("06_numpy/data/save.npy")        # 读取 .npy 文件
print("读取的数组:\n", loaded)                    # 打印读取的数组

np.savez("06_numpy/data/multi.npz", a=save_data, b=np.array([10, 20]))  # 保存多个数组
multi = np.load("06_numpy/data/multi.npz")        # 读取 .npz 文件
print("多数组文件:", multi["a"], multi["b"])       # 通过键名访问各数组

# 保存为文本文件
np.savetxt("06_numpy/data/save.csv", save_data, delimiter=",", fmt="%d")  # 保存为CSV
text_loaded = np.loadtxt("06_numpy/data/save.csv", delimiter=",", dtype=int)  # 读取CSV
print("CSV读取:\n", text_loaded)                  # 打印读取结果

# 清理示例文件
from pathlib import Path                          # 导入路径处理模块
for f in ["save.npy", "multi.npz", "save.csv"]:   # 遍历要清理的文件
    p = Path("06_numpy/data") / f                 # 构建文件路径
    if p.exists():                                # 如果文件存在
        p.unlink()                                # 删除文件
print("清理完成")                                 # 打印清理提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 生成10个随机成绩，计算均值/中位数/标准差")  # 练习1
    print("2. 对二维数组按某列排序")               # 练习2
    print("3. 统计一组数据中各值出现频率")          # 练习3
