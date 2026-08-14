"""02 - Pandas DataFrame 基础

学习目标:
    - 理解 DataFrame 是二维表格数据结构
    - 掌握 DataFrame 的创建与属性
    - 了解行列操作基础
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# ===== 1. 创建 DataFrame =====
print("--- 创建 DataFrame ---")                    # 打印标题

# 从字典创建（最常用）
df1 = pd.DataFrame({                              # 用字典创建 DataFrame
    "姓名": ["张三", "李四", "王五"],              # 列1: 姓名
    "年龄": [25, 30, 28],                         # 列2: 年龄
    "城市": ["北京", "上海", "广州"],              # 列3: 城市
})
print("从字典创建:\n", df1)                        # 打印 DataFrame

# 从列表创建
data = [                                          # 定义嵌套列表
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"],
]
df2 = pd.DataFrame(data, columns=["姓名", "年龄", "城市"])  # 指定列名
print("\n从列表创建:\n", df2)                      # 打印 DataFrame

# 从 NumPy 数组创建
arr = np.random.randint(60, 100, size=(3, 3))     # 生成3×3随机分数（60-99）
df3 = pd.DataFrame(arr, columns=["语文", "数学", "英语"], index=["学生1", "学生2", "学生3"])  # 指定列名和行索引
print("\n从数组创建:\n", df3)                      # 打印 DataFrame

# ===== 2. DataFrame 属性 =====
print("\n--- DataFrame 属性 ---")                  # 打印标题
print("形状 shape:", df1.shape)                   # (3, 3) → 3行3列
print("列名 columns:", list(df1.columns))         # 列名列表
print("行索引 index:", list(df1.index))           # 行索引列表
print("数据类型 dtypes:\n", df1.dtypes)           # 每列的数据类型
print("元素个数 size:", df1.size)                 # 总元素数 = 9
print("维度 ndim:", df1.ndim)                     # 维度 → 2

# ===== 3. 查看数据 =====
print("\n--- 查看数据 ---")                        # 打印标题
big_df = pd.DataFrame({                           # 创建较大数据用于演示
    "A": range(1, 11),                            # 列A: 1-10
    "B": np.random.rand(10),                      # 列B: 10个随机数
    "C": ["类型1"] * 5 + ["类型2"] * 5,           # 列C: 前5个类型1，后5个类型2
})
print("前3行 head(3):\n", big_df.head(3))         # head() 查看前几行，默认5行
print("\n后3行 tail(3):\n", big_df.tail(3))       # tail() 查看后几行
print("\n随机2行 sample(2):\n", big_df.sample(2))  # sample() 随机抽取行

# ===== 4. 选择列 =====
print("\n--- 选择列 ---")                          # 打印标题
print("单列:\n", df1["姓名"])                      # 用列名取一列（返回 Series）
print("\n多列:\n", df1[["姓名", "城市"]])          # 用列表取多列（返回 DataFrame）

# ===== 5. 添加/删除列 =====
print("\n--- 添加/删除列 ---")                     # 打印标题
df = df1.copy()                                   # 复制一份避免修改原数据
df["工资"] = [8000, 12000, 10000]                 # 新增列：直接赋值
print("新增列:\n", df)                             # 打印新增列后的 DataFrame

df["年薪"] = df["工资"] * 12                      # 基于已有列计算新列
print("\n计算列:\n", df)                           # 打印计算列后的 DataFrame

df.drop("工资", axis=1, inplace=True)             # drop 删除列，axis=1 表示列方向
print("\n删除工资列:\n", df)                       # 打印删除列后的 DataFrame

# ===== 6. 添加/删除行 =====
print("\n--- 添加/删除行 ---")                     # 打印标题
df.loc[3] = ["赵六", 26, "深圳", 132000]          # loc 添加新行
print("新增行:\n", df)                             # 打印新增行后的 DataFrame

df.drop(0, axis=0, inplace=True)                 # drop 删除行，axis=0 表示行方向
print("\n删除第0行:\n", df)                        # 打印删除行后的 DataFrame

# ===== 7. 转置 =====
print("\n--- 转置 ---")                            # 打印标题
print("转置 T:\n", df1.T)                         # .T 属性：行列互换


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建一个包含5人信息的 DataFrame（姓名/年龄/成绩）")  # 练习1
    print("2. 添加一列'等级'，根据成绩是否>=60填'及格'/'不及格'")  # 练习2
    print("3. 删除年龄列，并查看转置结果")          # 练习3
