"""06 - Pandas 数据读写

学习目标:
    - 掌握 CSV / Excel 读写
    - 了解 JSON / SQL 数据读取
    - 理解时间序列处理基础
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块
from pathlib import Path                          # 导入路径处理模块

# 准备数据目录
DATA_DIR = Path(__file__).parent / "data"         # 定义数据目录路径
DATA_DIR.mkdir(exist_ok=True)                     # 创建目录（已存在不报错）

# 创建示例数据
df = pd.DataFrame({                               # 创建示例 DataFrame
    "日期": pd.date_range("2024-01-01", periods=5),  # 生成5个连续日期
    "产品": ["苹果", "香蕉", "橙子", "苹果", "香蕉"],
    "数量": [100, 150, 80, 120, 90],
    "单价": [5.0, 3.5, 4.0, 5.0, 3.5],
})
df["总价"] = df["数量"] * df["单价"]              # 计算总价列
print("原始数据:\n", df)                           # 打印原始数据

# ===== 1. CSV 读写 =====
print("\n--- CSV 读写 ---")                        # 打印标题
csv_path = DATA_DIR / "sales.csv"                 # 定义 CSV 文件路径
df.to_csv(csv_path, index=False, encoding="utf-8-sig")  # 写入 CSV，index=False 不写行索引，utf-8-sig 支持中文
print("已保存 CSV")                                # 打印提示

df_csv = pd.read_csv(csv_path, encoding="utf-8-sig")  # 读取 CSV
print("读取 CSV:\n", df_csv)                      # 打印读取结果

# ===== 2. Excel 读写 =====
print("\n--- Excel 读写 ---")                      # 打印标题
excel_path = DATA_DIR / "sales.xlsx"              # 定义 Excel 文件路径
df.to_excel(excel_path, index=False, sheet_name="销售数据")  # 写入 Excel，指定工作表名
print("已保存 Excel")                              # 打印提示

df_excel = pd.read_excel(excel_path, sheet_name="销售数据")  # 读取 Excel
print("读取 Excel:\n", df_excel)                  # 打印读取结果

# ===== 3. JSON 读写 =====
print("\n--- JSON 读写 ---")                       # 打印标题
json_path = DATA_DIR / "sales.json"               # 定义 JSON 文件路径
df.to_json(json_path, orient="records", force_ascii=False, indent=2)  # 写入 JSON，records 格式
print("已保存 JSON")                               # 打印提示

df_json = pd.read_json(json_path)                 # 读取 JSON
print("读取 JSON:\n", df_json)                    # 打印读取结果

# ===== 4. 读取多个文件 =====
print("\n--- 读取多个文件 ---")                    # 打印标题
# 创建多个 CSV
for i in range(3):                                # 循环创建3个CSV文件
    temp_df = pd.DataFrame({"值": np.random.rand(5)})  # 生成随机数据
    temp_df.to_csv(DATA_DIR / f"part_{i}.csv", index=False)  # 保存

# 用 concat 合并多个文件
parts = []                                        # 创建空列表
for f in DATA_DIR.glob("part_*.csv"):             # glob 匹配所有 part_*.csv
    parts.append(pd.read_csv(f))                  # 读取并添加到列表
combined = pd.concat(parts, ignore_index=True)    # 拼接所有数据
print(f"合并{len(parts)}个文件，共{len(combined)}行")  # 打印合并结果

# ===== 5. 时间序列处理 =====
print("\n--- 时间序列 ---")                        # 打印标题
ts = pd.DataFrame({                               # 创建时间序列数据
    "日期": pd.date_range("2024-01-01", periods=10, freq="D"),  # 10天
    "销售额": np.random.randint(100, 500, 10),
})
ts.set_index("日期", inplace=True)                # 将日期列设为索引
print("时间序列:\n", ts)                           # 打印时间序列

# 按月重采样
monthly = ts.resample("ME").sum()                 # resample 按月末汇总求和
print("\n按月汇总:\n", monthly)                    # 打印月度汇总

# 滑动窗口
rolling = ts.rolling(window=3).mean()             # rolling 3天滑动平均
print("\n3天滑动平均:\n", rolling)                 # 打印滑动平均

# ===== 6. 常用读取参数 =====
print("\n--- 常用读取参数 ---")                    # 打印标题
# read_csv 常用参数示例
df_opt = pd.read_csv(                             # 读取 CSV
    csv_path,                                     # 文件路径
    encoding="utf-8-sig",                         # 编码
    nrows=3,                                      # 只读前3行
    dtype={"数量": float},                        # 指定列类型
)
print("只读3行:\n", df_opt)                       # 打印读取结果

# ===== 清理示例文件 =====
for f in DATA_DIR.glob("*"):                      # 遍历数据目录
    if f.is_file():                               # 如果是文件
        f.unlink()                                # 删除文件
print("\n清理完成")                               # 打印清理提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 创建一个 DataFrame 并保存为 CSV，再读回来验证")  # 练习1
    print("2. 生成30天的随机销售数据，按周汇总")    # 练习2
    print("3. 用 glob 读取多个 CSV 合并成一个 DataFrame")  # 练习3
