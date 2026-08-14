"""05 - Pandas 分组与聚合

学习目标:
    - 掌握 groupby 分组操作
    - 理解聚合函数与多级聚合
    - 了解数据合并(merge/concat)
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 创建员工数据
df = pd.DataFrame({                               # 创建示例 DataFrame
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"],
    "部门": ["技术", "销售", "技术", "管理", "销售", "技术", "管理", "销售"],
    "职级": ["P5", "P6", "P6", "P7", "P5", "P7", "P6", "P5"],
    "工资": [8000, 12000, 10000, 15000, 6000, 14000, 13000, 7000],
    "年龄": [25, 30, 28, 35, 22, 32, 29, 24],
})
print("原始数据:\n", df)                           # 打印原始数据

# ===== 1. 基本分组 =====
print("\n--- 基本分组 ---")                        # 打印标题
grouped = df.groupby("部门")                      # 按部门分组（返回 GroupBy 对象）
print("按部门分组后的均值:\n", grouped.mean(numeric_only=True))  # 每组的数值列均值

print("\n按部门分组求和:\n", grouped[["工资", "年龄"]].sum())  # 指定列求和

# ===== 2. 聚合函数 =====
print("\n--- 聚合函数 ---")                        # 打印标题
print("每组工资统计:\n", df.groupby("部门")["工资"].agg(["mean", "max", "min", "count"]))
# agg 一次应用多个聚合函数

# 自定义聚合
print("\n工资中位数:\n", df.groupby("部门")["工资"].median())  # median 中位数
print("\n工资标准差:\n", df.groupby("部门")["工资"].std())     # std 标准差

# ===== 3. 多列聚合 =====
print("\n--- 多列聚合 ---")                        # 打印标题
print("不同列用不同聚合:\n", df.groupby("部门").agg({
    "工资": ["mean", "max"],                      # 工资列：均值和最大值
    "年龄": "mean",                               # 年龄列：均值
    "姓名": "count",                              # 姓名列：计数
}))

# ===== 4. 多级分组 =====
print("\n--- 多级分组 ---")                        # 打印标题
multi_group = df.groupby(["部门", "职级"])["工资"].mean()  # 先按部门再按职级分组
print("按部门+职级分组:\n", multi_group)           # 打印多级分组结果

# ===== 5. 遍历分组 =====
print("\n--- 遍历分组 ---")                        # 打印标题
for name, group in df.groupby("部门"):            # 遍历每个分组
    print(f"\n部门: {name} ({len(group)}人)")     # 打印部门名和人数
    print(group[["姓名", "工资"]])                # 打印该组详细信息

# ===== 6. 数据合并 merge =====
print("\n--- merge 合并 ---")                      # 打印标题
employees = pd.DataFrame({                        # 创建员工表
    "emp_id": [1, 2, 3, 4],
    "姓名": ["张三", "李四", "王五", "赵六"],
    "部门ID": [101, 102, 101, 103],
})
departments = pd.DataFrame({                      # 创建部门表
    "dept_id": [101, 102, 103],
    "部门名": ["技术部", "销售部", "管理部"],
    "地点": ["北京", "上海", "广州"],
})

merged = pd.merge(employees, departments, left_on="部门ID", right_on="dept_id")  # 按不同列名关联
print("合并结果:\n", merged)                       # 打印合并结果

# ===== 7. 数据拼接 concat =====
print("\n--- concat 拼接 ---")                     # 打印标题
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})    # 创建 df1
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})    # 创建 df2

vertical = pd.concat([df1, df2], ignore_index=True)  # 纵向拼接（上下）
print("纵向拼接:\n", vertical)                     # 打印纵向拼接结果

df3 = pd.DataFrame({"C": [10, 20]})               # 创建 df3（不同列名）
horizontal = pd.concat([df1, df3], axis=1)        # 横向拼接（左右）
print("\n横向拼接:\n", horizontal)                 # 打印横向拼接结果

# ===== 8. 透视表 pivot_table =====
print("\n--- 透视表 ---")                          # 打印标题
pivot = pd.pivot_table(df, values="工资", index="部门", columns="职级", aggfunc="mean")  # 创建透视表
print("工资透视表:\n", pivot)                      # 打印透视表（行=部门，列=职级，值=平均工资）


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 按部门分组，计算每组的平均工资和平均年龄")  # 练习1
    print("2. 用 merge 合并员工表和部门表")        # 练习2
    print("3. 用 pivot_table 制作各部门各职级的工资透视表")  # 练习3
