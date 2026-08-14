"""04 - Pandas 数据清洗

学习目标:
    - 掌握缺失值处理（检测/填充/删除）
    - 了解重复值处理
    - 掌握数据类型转换与替换
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 创建含缺失值的示例数据
df = pd.DataFrame({                               # 创建示例 DataFrame
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "张三"],
    "年龄": [25, np.nan, 28, 35, 22, 25],         # np.nan 表示缺失值
    "工资": [8000, 12000, np.nan, 15000, None, 8000],
    "城市": ["北京", "上海", "广州", None, "深圳", "北京"],
})
print("原始数据:\n", df)                           # 打印原始数据

# ===== 1. 检测缺失值 =====
print("\n--- 检测缺失值 ---")                      # 打印标题
print("isnull():\n", df.isnull())                 # isnull 返回布尔矩阵，True 表示缺失
print("\n每列缺失数:\n", df.isnull().sum())        # sum 统计每列缺失值数量
print("总缺失数:", df.isnull().sum().sum())        # 总缺失值数量

# ===== 2. 删除缺失值 =====
print("\n--- 删除缺失值 ---")                      # 打印标题
dropped = df.dropna()                             # dropna 删除任何含缺失值的行
print("dropna():\n", dropped)                     # 打印删除后的结果

dropped_all = df.dropna(how="all")                # how="all" 只删除全部为缺失的行
print("\nhow='all':\n", dropped_all)              # 打印结果（本例没有整行缺失）

dropped_col = df.dropna(axis=1)                   # axis=1 删除含缺失值的列
print("\n删除缺失列:\n", dropped_col)              # 打印删除列后的结果

# ===== 3. 填充缺失值 =====
print("\n--- 填充缺失值 ---")                      # 打印标题
filled = df.copy()                                # 复制一份

# 用固定值填充
filled["年龄"].fillna(0, inplace=True)            # 用0填充年龄的缺失值
filled["城市"].fillna("未知", inplace=True)        # 用"未知"填充城市
print("固定值填充:\n", filled)                     # 打印填充后的结果

# 用均值填充
filled2 = df.copy()                               # 再复制一份
mean_salary = filled2["工资"].mean()              # 计算工资均值
filled2["工资"].fillna(mean_salary, inplace=True)  # 用均值填充工资
print("\n均值填充工资:", f"均值={mean_salary:.0f}")  # 打印均值

# 用前一个值填充（前向填充）
filled3 = df.copy()                               # 再复制一份
filled3["工资"] = filled3["工资"].ffill()          # ffill 用上一个有效值填充
print("\n前向填充:\n", filled3)                    # 打印前向填充结果

# ===== 4. 重复值处理 =====
print("\n--- 重复值处理 ---")                      # 打印标题
print("重复行:\n", df.duplicated())               # duplicated 标记重复行（第二次出现为True）
print("\n重复行数:", df.duplicated().sum())        # 统计重复行数量

deduped = df.drop_duplicates()                    # drop_duplicates 删除重复行
print("\n去重后:\n", deduped)                      # 打印去重结果

# 按指定列去重
deduped_name = df.drop_duplicates(subset=["姓名"])  # 只按姓名去重，保留第一次出现
print("\n按姓名去重:\n", deduped_name)             # 打印按列去重结果

# ===== 5. 数据类型转换 =====
print("\n--- 类型转换 ---")                        # 打印标题
df_type = pd.DataFrame({                          # 创建新数据
    "价格": ["12.5", "25.0", "8.3"],              # 字符串形式的数字
    "数量": ["1", "3", "2"],
    "日期": ["2024-01-01", "2024-01-02", "2024-01-03"],
})
print("原始类型:\n", df_type.dtypes)              # 打印数据类型（全是 object 即字符串）

df_type["价格"] = df_type["价格"].astype(float)   # astype 转为浮点数
df_type["数量"] = df_type["数量"].astype(int)      # astype 转为整数
df_type["日期"] = pd.to_datetime(df_type["日期"])  # to_datetime 转为日期类型
print("\n转换后类型:\n", df_type.dtypes)           # 打印转换后的类型

# ===== 6. 替换值 =====
print("\n--- 替换值 ---")                          # 打印标题
df_rep = pd.DataFrame({                           # 创建示例数据
    "评分": [5, 4, -1, 3, 0, -1],
    "性别": ["M", "F", "M", "F", "M", "F"],
})
print("替换前:\n", df_rep)                         # 打印替换前

df_rep["评分"] = df_rep["评分"].replace(-1, np.nan)  # replace 将-1替换为缺失值
df_rep["性别"] = df_rep["性别"].replace({"M": "男", "F": "女"})  # 用字典批量替换
print("\n替换后:\n", df_rep)                       # 打印替换后

# ===== 7. apply 自定义函数 =====
print("\n--- apply ---")                           # 打印标题
df_apply = pd.DataFrame({                         # 创建示例数据
    "温度": [35.6, 28.3, 22.1, 18.5, 30.0],
})

def temp_level(temp):                             # 定义温度等级函数
    if temp >= 30:                                # 30度以上
        return "炎热"
    elif temp >= 25:                              # 25-30度
        return "温暖"
    else:                                         # 25度以下
        return "凉爽"

df_apply["等级"] = df_apply["温度"].apply(temp_level)  # apply 对每行应用函数
print(df_apply)                                   # 打印结果


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建一个含缺失值的 DataFrame，分别用均值和众数填充")  # 练习1
    print("2. 对一列数据用 apply 实现分段评级")     # 练习2
    print("3. 检测并删除完全重复的行")              # 练习3
