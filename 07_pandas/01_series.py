"""01 - Pandas Series 基础

学习目标:
    - 理解 Series 与 list/dict 的区别
    - 掌握 Series 的创建与属性
    - 了解 Series 的基本操作
"""

import pandas as pd                               # 导入 pandas 模块，约定缩写为 pd

# ===== 1. 创建 Series =====
print("--- 创建 Series ---")                       # 打印标题

# 从列表创建
s1 = pd.Series([10, 20, 30, 40, 50])              # 从列表创建 Series，自动生成索引 0,1,2...
print("从列表创建:\n", s1)                         # 打印 Series

# 指定索引
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])  # 自定义索引为 a, b, c
print("\n指定索引:\n", s2)                         # 打印带自定义索引的 Series

# 从字典创建（键变成索引）
s3 = pd.Series({"语文": 90, "数学": 85, "英语": 78})  # 字典的键自动成为索引
print("\n从字典创建:\n", s3)                        # 打印字典创建的 Series

# 从标量创建（自动广播）
s4 = pd.Series(5, index=["a", "b", "c"])          # 每个索引位置的值都是5
print("\n标量创建:\n", s4)                          # 打印 [5, 5, 5]

# ===== 2. Series 属性 =====
print("\n--- Series 属性 ---")                     # 打印标题
s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])  # 创建带索引的 Series
print("值 values:", s.values)                     # values 返回数据的 NumPy 数组
print("索引 index:", s.index)                     # index 返回索引列表
print("数据类型 dtype:", s.dtype)                 # dtype 返回数据类型
print("形状 shape:", s.shape)                     # shape 返回形状 (5,)
print("元素个数 size:", s.size)                   # size 返回元素数量

# ===== 3. 索引访问 =====
print("\n--- 索引访问 ---")                        # 打印标题
print("s['a']:", s["a"])                          # 用标签索引取值 → 10
print("s[0]:", s[0])                              # 用位置索引取值 → 10
print("s[['a', 'c']]:\n", s[["a", "c"]])          # 取多个值（花式索引）

# 切片
print("s['a':'c']:\n", s["a":"c"])                # 标签切片（包含两端！）→ a,b,c
print("s[0:3]:\n", s[0:3])                        # 位置切片（不含末端）→ a,b,c

# ===== 4. 基本运算 =====
print("\n--- 基本运算 ---")                        # 打印标题
print("s + 100:\n", s + 100)                      # 每个元素加100（标量运算）
print("s * 2:\n", s * 2)                          # 每个元素乘2

# Series 之间的运算（按索引对齐）
s_a = pd.Series({"a": 1, "b": 2, "c": 3})         # 创建 Series s_a
s_b = pd.Series({"a": 10, "b": 20, "d": 40})      # 创建 Series s_b（注意 d 只在 s_b 中）
print("\ns_a + s_b:\n", s_a + s_b)                # 按索引对齐相加，不匹配的为 NaN

# ===== 5. 常用方法 =====
print("\n--- 常用方法 ---")                        # 打印标题
data = pd.Series([3, 1, 4, 1, 5, 9, 2, 6])        # 创建测试数据
print("总和:", data.sum())                        # 求和
print("均值:", data.mean())                       # 平均值
print("最大值:", data.max())                      # 最大值
print("最小值:", data.min())                      # 最小值
print("中位数:", data.median())                   # 中位数
print("标准差:", data.std())                      # 标准差
print("排序:\n", data.sort_values())              # 按值排序（升序）
print("降序:\n", data.sort_values(ascending=False))  # descending 降序

# ===== 6. 统计描述 =====
print("\n--- 统计描述 ---")                        # 打印标题
print(data.describe())                            # describe() 一键生成统计摘要

# ===== 7. 布尔索引 =====
print("\n--- 布尔索引 ---")                        # 打印标题
scores = pd.Series([55, 80, 90, 45, 70, 85], index=["张三", "李四", "王五", "赵六", "钱七", "孙八"])  # 创建成绩 Series
print("及格的:\n", scores[scores >= 60])          # 筛选及格的同学
print("最高分:", scores.idxmax())                 # idxmax() 返回最大值的索引名
print("最低分:", scores.idxmin())                 # idxmin() 返回最小值的索引名


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建一个 Series 存储5种商品价格，并计算总价和均价")  # 练习1
    print("2. 用布尔索引筛选出价格高于平均值的商品")  # 练习2
    print("3. 对两个 Series 做加法，观察索引对齐现象")  # 练习3
