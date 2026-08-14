"""练习2: 销售数据分析

模拟一份销售数据，完成:
    - 按产品/地区/月份分组统计
    - 计算环比增长率
    - 找出畅销产品和最佳销售员
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 生成模拟销售数据
np.random.seed(42)                                # 设置随机种子
dates = pd.date_range("2024-01-01", "2024-06-30", freq="D")  # 生成半年日期
products = ["手机", "电脑", "平板", "耳机"]        # 产品列表
regions = ["华北", "华东", "华南", "西部"]         # 地区列表
salespersons = ["张三", "李四", "王五", "赵六", "钱七"]  # 销售员列表

n = 200                                           # 生成200条记录
df = pd.DataFrame({                               # 创建销售 DataFrame
    "日期": np.random.choice(dates, n),            # 随机日期
    "产品": np.random.choice(products, n),          # 随机产品
    "地区": np.random.choice(regions, n),           # 随机地区
    "销售员": np.random.choice(salespersons, n),    # 随机销售员
    "数量": np.random.randint(1, 20, n),            # 随机数量1-19
    "金额": np.random.randint(100, 5000, n),        # 随机金额100-4999
})

print(f"=== 销售数据（共{len(df)}条）===")          # 打印数据概览
print(df.head(10))                                # 查看前10条

# 1. 按产品统计
print("\n=== 按产品统计 ===")                      # 打印标题
product_stats = df.groupby("产品").agg({           # 按产品分组聚合
    "数量": "sum",                                # 总销量
    "金额": ["sum", "mean"],                      # 总金额和平均金额
    "日期": "count",                              # 交易次数
}).round(2)                                       # round 保留2位小数
product_stats.columns = ["总销量", "总金额", "平均金额", "交易次数"]  # 重命名列
product_stats = product_stats.sort_values("总金额", ascending=False)  # 按总金额降序
print(product_stats)                              # 打印产品统计

# 2. 按地区统计
print("\n=== 按地区统计 ===")                      # 打印标题
region_stats = df.groupby("地区")["金额"].agg(["sum", "mean", "count"]).round(2)  # 按地区聚合
region_stats.columns = ["总金额", "平均金额", "交易次数"]  # 重命名列
print(region_stats)                               # 打印地区统计

# 3. 按月统计销售额
df["月份"] = df["日期"].dt.to_period("M")         # dt.to_period 提取年月
monthly = df.groupby("月份")["金额"].sum()        # 按月汇总销售额
print("\n=== 月度销售额 ===")                      # 打印标题
print(monthly)                                    # 打印月度销售额

# 环比增长率
monthly_growth = monthly.pct_change().round(4)    # pct_change 计算环比增长率
print("\n=== 环比增长率 ===")                      # 打印标题
for month, growth in monthly_growth.items():      # 遍历每月
    if pd.notna(growth):                          # 跳过第一个月（无环比）
        print(f"  {month}: {growth:+.2%}")        # 打印增长率（带正负号）

# 4. 最佳销售员
print("\n=== 销售员排行 ===")                      # 打印标题
top_sales = df.groupby("销售员")["金额"].sum().sort_values(ascending=False)  # 按销售员汇总并排序
for rank, (person, amount) in enumerate(top_sales.items(), 1):  # 遍历排名
    print(f"  第{rank}名: {person} - ¥{amount:,}")  # 打印排名和金额

# 5. 畅销产品TOP3
print("\n=== 畅销产品TOP3 ===")                    # 打印标题
top_products = df.groupby("产品")["数量"].sum().nlargest(3)  # nlargest 取最大的3个
for product, qty in top_products.items():         # 遍历畅销产品
    print(f"  {product}: {qty}件")                # 打印产品名和销量
