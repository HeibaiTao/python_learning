"""02 - NumPy 索引与切片

学习目标:
    - 掌握一维/多维数组的索引
    - 理解切片与布尔索引
    - 了解花式索引
"""

import numpy as np                                # 导入 numpy 模块

# ===== 1. 一维数组索引 =====
print("--- 一维索引 ---")                          # 打印标题
arr = np.arange(10)                               # 创建 0-9 的一维数组
print("原数组:", arr)                             # 打印原数组

print("arr[0]:", arr[0])                          # 索引第0个元素
print("arr[-1]:", arr[-1])                        # 负索引，取最后一个元素
print("arr[3:7]:", arr[3:7])                      # 切片：取索引3到6（不含7）
print("arr[:5]:", arr[:5])                        # 切片：从头取到索引4
print("arr[5:]:", arr[5:])                        # 切片：从索引5取到末尾
print("arr[::2]:", arr[::2])                      # 切片：步长为2，取偶数索引

# ===== 2. 二维数组索引 =====
print("\n--- 二维索引 ---")                        # 打印标题
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 创建3×3矩阵
print("原矩阵:\n", mat)                           # 打印原矩阵

print("mat[0]:", mat[0])                          # 取第0行 → [1, 2, 3]
print("mat[0][1]:", mat[0][1])                    # 取第0行第1列 → 2
print("mat[0, 1]:", mat[0, 1])                    # 等价写法（推荐）→ 2
print("mat[:, 0]:", mat[:, 0])                    # 取第0列所有行 → [1, 4, 7]
print("mat[1:, :2]:\n", mat[1:, :2])              # 取第1行起、前2列的子矩阵

# ===== 3. 布尔索引 =====
print("\n--- 布尔索引 ---")                        # 打印标题
data = np.array([10, 20, 30, 40, 50])             # 创建一维数组
mask = data > 25                                  # 生成布尔数组：每个元素是否大于25
print("布尔掩码:", mask)                          # 打印 [False False  True  True  True]
print("大于25的:", data[mask])                    # 用布尔数组筛选，返回 [30, 40, 50]
print("直接写:", data[data > 25])                 # 也可以直接写在一起

# 条件组合
print("20~40之间:", data[(data > 20) & (data < 50)])  # & 表示且，() 必须加
print("小于20或大于40:", data[(data < 20) | (data > 40)])  # | 表示或

# 布尔赋值
data2 = data.copy()                               # 复制一份避免修改原数组
data2[data2 > 30] = 0                             # 把大于30的元素全部赋值为0
print("修改后:", data2)                           # 打印 [10 20 30  0  0]

# ===== 4. 花式索引 =====
print("\n--- 花式索引 ---")                        # 打印标题
arr2 = np.arange(20).reshape(4, 5)                # 创建4行5列的数组（0-19）
print("原数组:\n", arr2)                          # 打印原数组

print("取第0,2,3行:\n", arr2[[0, 2, 3]])          # 用列表指定多个行索引
print("取第1,3列:\n", arr2[:, [1, 3]])            # 用列表指定多个列索引

# ===== 5. where 条件 =====
print("\n--- np.where ---")                       # 打印标题
cond = np.array([True, False, True, False])       # 创建条件数组
values = np.array([1, 2, 3, 4])                   # 创建数据数组
result = np.where(cond, values, 0)                # True取values对应值，False取0
print("where结果:", result)                       # 打印 [1 0 3 0]

# where 三元运算示例
scores = np.array([55, 80, 90, 45, 70])           # 创建分数数组
grades = np.where(scores >= 60, "及格", "不及格")  # 大于等于60为"及格"，否则"不及格"
print("成绩:", scores)                            # 打印分数
print("评级:", grades)                            # 打印评级


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建 5×5 矩阵，提取对角线元素")       # 练习1
    print("2. 用布尔索引将数组中所有负数替换为0")    # 练习2
    print("3. 用花式索引打乱数组行的顺序")          # 练习3
