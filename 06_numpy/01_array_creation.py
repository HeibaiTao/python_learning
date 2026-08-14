"""01 - NumPy 数组创建

学习目标:
    - 理解 ndarray 与 list 的区别
    - 掌握多种创建数组的方式
    - 了解数组属性(shape/dtype/ndim/size)
"""

import numpy as np                                # 导入 numpy 模块，约定俗成缩写为 np

# ===== 1. 从列表创建数组 =====
print("--- 从列表创建 ---")                         # 打印标题
arr1 = np.array([1, 2, 3, 4, 5])                  # 把 Python 列表转为 NumPy 一维数组
print(arr1)                                       # 打印数组内容
print(type(arr1))                                 # 打印类型：<class 'numpy.ndarray'>

arr2 = np.array([[1, 2, 3], [4, 5, 6]])           # 嵌套列表转为二维数组（矩阵）
print(arr2)                                       # 打印二维数组

# ===== 2. 数组属性 =====
print("\n--- 数组属性 ---")                        # 打印标题
print("形状 shape:", arr2.shape)                  # shape 返回数组的维度，如 (2, 3) 表示 2行3列
print("维度 ndim:", arr2.ndim)                    # ndim 返回数组的维数，二维数组为 2
print("元素个数 size:", arr2.size)                # size 返回元素总数，2×3=6
print("数据类型 dtype:", arr2.dtype)              # dtype 返回元素的数据类型，如 int64

# ===== 3. 创建特殊数组 =====
print("\n--- 特殊数组 ---")                        # 打印标题
zeros = np.zeros(5)                               # 创建长度为5的全零数组，默认浮点型
print("全零:", zeros)                             # 打印全零数组

ones = np.ones((2, 3))                            # 创建2行3列的全一数组
print("全一:\n", ones)                            # 打印全一数组

full = np.full((2, 2), 7)                         # 创建2行2列、全部填充7的数组
print("全填充:\n", full)                          # 打印全填充数组

eye = np.eye(3)                                   # 创建3×3的单位矩阵（对角线为1，其余为0）
print("单位矩阵:\n", eye)                         # 打印单位矩阵

# ===== 4. 创建序列数组 =====
print("\n--- 序列数组 ---")                        # 打印标题
range_arr = np.arange(0, 10, 2)                   # 类似 range()，从0到10（不含），步长2
print("arange:", range_arr)                       # 打印 [0 2 4 6 8]

linspace = np.linspace(0, 1, 5)                   # 在0到1之间均匀取5个数（含两端）
print("linspace:", linspace)                      # 打印 [0.   0.25 0.5  0.75 1.  ]

# ===== 5. 创建随机数组 =====
print("\n--- 随机数组 ---")                        # 打印标题
rand_arr = np.random.rand(3)                      # 生成3个[0,1)之间的均匀随机数
print("均匀随机:", rand_arr)                      # 打印随机数组

randn_arr = np.random.randn(2, 2)                 # 生成2×2的标准正态分布随机数（均值0，方差1）
print("正态随机:\n", randn_arr)                   # 打印正态分布随机数组

randint_arr = np.random.randint(0, 10, size=5)    # 生成5个[0,10)之间的随机整数
print("随机整数:", randint_arr)                   # 打印随机整数数组

# ===== 6. 指定数据类型 =====
print("\n--- 数据类型 ---")                        # 打印标题
float_arr = np.array([1, 2, 3], dtype=np.float64)  # 创建数组时指定为浮点型
print("浮点型:", float_arr, float_arr.dtype)      # 打印数组和类型

int_arr = np.array([1.9, 2.7, 3.2], dtype=np.int32)  # 创建数组时指定为整型（会截断小数）
print("整型:", int_arr, int_arr.dtype)            # 打印 [1 2 3] int32

converted = float_arr.astype(np.int32)            # astype() 转换数据类型
print("转换后:", converted, converted.dtype)      # 打印转换后的数组


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建一个 3×3 的随机整数矩阵(0-9)")   # 练习1
    print("2. 用 arange 创建 10-100 的偶数数组")    # 练习2
    print("3. 创建一个 5×5 的单位矩阵")             # 练习3
