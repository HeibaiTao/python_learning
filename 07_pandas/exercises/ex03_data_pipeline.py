"""练习3: 数据清洗与处理流水线

模拟一份脏数据，完成完整的清洗流程:
    - 缺失值检测与处理
    - 重复值删除
    - 数据类型转换
    - 异常值检测
    - 数据标准化
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 创建一份"脏数据"（包含缺失值、重复值、异常值、错误类型）
dirty_data = pd.DataFrame({                       # 创建脏数据 DataFrame
    "用户ID": [1001, 1002, 1003, 1004, 1005, 1001, 1006, 1007],
    "姓名": ["张三", "李四", "王五", "赵六", None, "张三", "钱七", "孙八"],
    "年龄": [25, 30, 200, 35, 22, 25, -5, 28],   # 含异常值: 200和-5
    "工资": ["8000", "12000", None, "15000", "6000", "8000", "7000", "invalid"],  # 含缺失和错误值
    "注册日期": ["2024-01-01", "2024-01-02", "2024-01-03", None, "2024-01-05", "2024-01-01", "2024-01-06", "2024-01-07"],
})
print("=== 原始脏数据 ===")                        # 打印标题
print(dirty_data)                                # 打印原始数据
print(f"\n数据概览: {dirty_data.shape[0]}行 × {dirty_data.shape[1]}列")  # 打印数据维度

# 第一步: 删除重复行
print("\n=== 第一步: 删除重复行 ===")              # 打印标题
print("重复行数量:", dirty_data.duplicated().sum())  # 检查重复行
df = dirty_data.drop_duplicates()                 # 删除重复行
print(f"删除重复后: {df.shape[0]}行")             # 打印删除后行数

# 第二步: 处理缺失值
print("\n=== 第二步: 处理缺失值 ===")              # 打印标题
print("各列缺失数:")                              # 打印提示
print(df.isnull().sum())                          # 统计每列缺失值
df["姓名"].fillna("未知用户", inplace=True)       # 姓名缺失填"未知用户"
df["注册日期"].fillna("2024-01-01", inplace=True)  # 日期缺失填默认值

# 第三步: 数据类型转换
print("\n=== 第三步: 类型转换 ===")                # 打印标题
# 工资列含 "invalid"，先用 to_numeric 转换，无效变 NaN
df["工资"] = pd.to_numeric(df["工资"], errors="coerce")  # errors="coerce" 无效值变 NaN
print("转换后缺失:", df["工资"].isnull().sum())    # 打印无效值数量
mean_salary = df["工资"].mean()                   # 计算工资均值
df["工资"].fillna(mean_salary, inplace=True)      # 用均值填充缺失
df["工资"] = df["工资"].astype(int)               # 转为整数
df["年龄"] = pd.to_numeric(df["年龄"], errors="coerce")  # 年龄也转数字
df["注册日期"] = pd.to_datetime(df["注册日期"])   # 转为日期类型

# 第四步: 处理异常值
print("\n=== 第四步: 异常值处理 ===")              # 打印标题
print("年龄统计:")                                # 打印提示
print(df["年龄"].describe())                      # 查看年龄分布
# 年龄应在 0-120 之间，超出视为异常
age_mask = (df["年龄"] < 0) | (df["年龄"] > 120)  # 创建异常值掩码
print(f"异常年龄数量: {age_mask.sum()}")          # 打印异常数量
df.loc[age_mask, "年龄"] = df["年龄"][(df["年龄"] >= 0) & (df["年龄"] <= 120)].median()  # 用中位数替换异常值
print("处理后年龄:", df["年龄"].tolist())         # 打印处理后的年龄

# 第五步: 数据标准化（Z-score标准化）
print("\n=== 第五步: 数据标准化 ===")              # 打印标题
df["工资_zscore"] = (df["工资"] - df["工资"].mean()) / df["工资"].std()  # Z-score 标准化
df["年龄_zscore"] = (df["年龄"] - df["年龄"].mean()) / df["年龄"].std()
print(df[["姓名", "工资", "工资_zscore", "年龄", "年龄_zscore"]])  # 打印标准化结果

# 最终结果
print("\n=== 清洗完成 ===")                        # 打印标题
print(df)                                         # 打印最终数据
print(f"\n最终数据: {df.shape[0]}行 × {df.shape[1]}列")  # 打印最终维度
print("数据类型:")                                # 打印提示
print(df.dtypes)                                  # 打印各列类型
