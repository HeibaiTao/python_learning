"""03 - Pandas 索引与数据选择

学习目标:
    - 掌握 loc / iloc 的区别与用法
    - 理解条件筛选与多条件组合
    - 了解 set_index / reset_index
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 创建示例数据
df = pd.DataFrame({                               # 创建示例 DataFrame
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [25, 30, 28, 35, 22],
    "工资": [8000, 12000, 10000, 15000, 6000],
    "部门": ["技术", "销售", "技术", "管理", "销售"],
})
print("原数据:\n", df)                            # 打印原数据

# ===== 1. loc：按标签索引 =====
print("\n--- loc（标签索引）---")                  # 打印标题
print("单行 loc[0]:\n", df.loc[0])                # loc 按行标签取行（返回 Series）
print("\n多行 loc[0:2]:\n", df.loc[0:2])          # loc 切片（包含两端！）

# 行列同时选择
print("\nloc[0:2, '姓名','工资']:\n", df.loc[0:2, ["姓名", "工资"]])  # 选行+选列

# 布尔条件
print("\nloc[工资>10000]:\n", df.loc[df["工资"] > 10000])  # 用 loc 筛选行

# ===== 2. iloc：按位置索引 =====
print("\n--- iloc（位置索引）---")                 # 打印标题
print("单行 iloc[0]:\n", df.iloc[0])              # iloc 按位置取第0行
print("\n多行 iloc[0:2]:\n", df.iloc[0:2])        # iloc 切片（不含末端！与 loc 不同）

# 行列同时选择
print("\niloc[0:3, 0:2]:\n", df.iloc[0:3, 0:2])   # 用位置选前3行、前2列

# ===== 3. loc vs iloc 对比 =====
print("\n--- loc vs iloc ---")                    # 打印标题
print("loc[0:2] 包含第2行:\n", df.loc[0:2].shape)  # loc 切片含末端 → 3行
print("iloc[0:2] 不含第2行:\n", df.iloc[0:2].shape)  # iloc 切片不含末端 → 2行

# ===== 4. 条件筛选 =====
print("\n--- 条件筛选 ---")                        # 打印标题
print("年龄>25:\n", df[df["年龄"] > 25])          # 单条件筛选

print("\n技术部:\n", df[df["部门"] == "技术"])     # 等于条件

# 多条件组合（& 表示且，| 表示或，每个条件要加括号）
print("\n年龄>25且工资>9000:\n", df[(df["年龄"] > 25) & (df["工资"] > 9000)])  # 且
print("\n技术部或管理部:\n", df[(df["部门"] == "技术") | (df["部门"] == "管理")])  # 或

# isin 判断是否在列表中
print("\n部门在[技术,管理]:\n", df[df["部门"].isin(["技术", "管理"])])  # isin 筛选

# between 范围筛选
print("\n年龄在25-30:\n", df[df["年龄"].between(25, 30)])  # between 范围筛选

# ===== 5. 修改数据 =====
print("\n--- 修改数据 ---")                        # 打印标题
df_mod = df.copy()                                # 复制一份
df_mod.loc[0, "工资"] = 9000                      # loc 修改单个值
print("修改第0行工资:", df_mod.loc[0, "工资"])    # 打印修改后的值

df_mod.loc[df_mod["部门"] == "销售", "工资"] += 1000  # 给销售部所有人加工资
print("\n销售部加工资:\n", df_mod)                # 打印修改后的 DataFrame

# ===== 6. 索引操作 =====
print("\n--- 索引操作 ---")                        # 打印标题
df_idx = df.copy()                                # 复制一份
df_idx.set_index("姓名", inplace=True)            # set_index 将某列设为行索引
print("set_index后:\n", df_idx)                   # 打印设置索引后的结果
print("\n用姓名取行 loc['张三']:\n", df_idx.loc["张三"])  # 用姓名索引取行

df_idx.reset_index(inplace=True)                  # reset_index 恢复默认数字索引
print("\nreset_index后:\n", df_idx)               # 打印恢复后的结果

# ===== 7. 排序 =====
print("\n--- 排序 ---")                            # 打印标题
print("按工资降序:\n", df.sort_values("工资", ascending=False))  # 按工资降序
print("\n按年龄升序:\n", df.sort_values("年龄"))   # 按年龄升序（默认）
print("\n按部门+工资排序:\n", df.sort_values(["部门", "工资"], ascending=[True, False]))  # 多列排序


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 用 loc 和 iloc 分别取第2-3行的姓名和工资")  # 练习1
    print("2. 筛选年龄在25-30之间且工资>8000的员工")  # 练习2
    print("3. 将姓名设为索引，然后用 loc 按姓名查询")  # 练习3
