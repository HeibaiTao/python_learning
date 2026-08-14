"""06 - 与 Pandas/NumPy 结合绘图

学习目标:
    - 掌握 Pandas 内置绘图方法
    - 理解时间序列可视化
    - 了解数据可视化完整流程
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# ===== 1. Pandas 直接绘图 =====
print("--- Pandas 绘图 ---")                       # 打印标题
df = pd.DataFrame({                               # 创建 DataFrame
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "销售额": [120, 150, 180, 165, 200, 220],
    "成本": [80, 95, 110, 100, 125, 140],
})
df.set_index("月份", inplace=True)                # 设置月份为索引

# df.plot() 直接绘图（一行搞定）
df.plot(kind="line", figsize=(10, 4), marker="o")  # kind="line" 折线图
plt.title("月度销售额与成本趋势")                   # 设置标题
plt.ylabel("金额（万元）")                         # y 轴标签
plt.grid(True, alpha=0.3)                         # 显示网格
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/28_pandas_line.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("Pandas折线图已保存")                        # 打印提示

# ===== 2. Pandas 柱状图 =====
print("\n--- Pandas 柱状图 ---")                   # 打印标题
df.plot(kind="bar", figsize=(10, 4), width=0.6)   # kind="bar" 柱状图
plt.title("月度销售额与成本对比")                   # 设置标题
plt.ylabel("金额（万元）")                         # y 轴标签
plt.xticks(rotation=0)                            # rotation=0 x轴标签水平显示
plt.legend(loc="upper left")                      # 图例位置
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/29_pandas_bar.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("Pandas柱状图已保存")                        # 打印提示

# ===== 3. Pandas 直方图 =====
print("\n--- Pandas 直方图 ---")                   # 打印标题
np.random.seed(42)                                # 设置随机种子
df_scores = pd.DataFrame({                        # 创建成绩数据
    "语文": np.random.normal(75, 10, 100),
    "数学": np.random.normal(80, 15, 100),
    "英语": np.random.normal(70, 12, 100),
})

df_scores.plot(kind="hist", alpha=0.6, bins=20, figsize=(10, 4))  # kind="hist" 直方图
plt.title("三科成绩分布对比")                      # 设置标题
plt.xlabel("分数")                                # x 轴标签
plt.ylabel("人数")                                # y 轴标签
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/30_pandas_hist.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("Pandas直方图已保存")                        # 打印提示

# ===== 4. Pandas 箱线图 =====
print("\n--- Pandas 箱线图 ---")                   # 打印标题
df_scores.plot(kind="box", figsize=(8, 5))        # kind="box" 箱线图
plt.title("三科成绩箱线图")                        # 设置标题
plt.ylabel("分数")                                # y 轴标签
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/31_pandas_box.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("Pandas箱线图已保存")                        # 打印提示

# ===== 5. 时间序列可视化 =====
print("\n--- 时间序列 ---")                        # 打印标题
dates = pd.date_range("2024-01-01", periods=90, freq="D")  # 生成90天日期
np.random.seed(42)                                # 设置随机种子
stock_price = 100 + np.cumsum(np.random.randn(90) * 2)  # 模拟股价（随机游走）

ts = pd.Series(stock_price, index=dates)          # 创建时间序列

fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)  # 创建2行1列子图

# 上图：股价走势
axes[0].plot(ts.index, ts.values, color="blue", linewidth=1.5)  # 画股价线
axes[0].set_title("模拟股价90天走势")              # 设置标题
axes[0].set_ylabel("价格")                        # y 轴标签
axes[0].grid(True, alpha=0.3)                     # 显示网格

# 下图：7日滑动平均
ma7 = ts.rolling(window=7).mean()                 # 计算7日滑动平均
axes[1].plot(ts.index, ts.values, color="lightblue", label="每日价格")  # 原始数据
axes[1].plot(ma7.index, ma7.values, color="red", linewidth=2, label="7日均线")  # 均线
axes[1].set_title("7日滑动平均")                   # 设置标题
axes[1].set_ylabel("价格")                        # y 轴标签
axes[1].legend()                                  # 显示图例
axes[1].grid(True, alpha=0.3)                     # 显示网格

plt.xlabel("日期")                                # 共享 x 轴标签
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/32_timeseries.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("时间序列图已保存")                          # 打印提示

# ===== 6. 完整数据分析可视化流程 =====
print("\n--- 完整流程示例 ---")                    # 打印标题
# 第1步：生成数据
np.random.seed(42)                                # 设置随机种子
data = pd.DataFrame({                             # 创建数据集
    "产品": np.random.choice(["A", "B", "C", "D"], 200),
    "地区": np.random.choice(["华北", "华东", "华南"], 200),
    "销售额": np.random.exponential(1000, 200),    # 指数分布模拟销售额
})

# 第2步：分组聚合
region_sales = data.groupby("地区")["销售额"].sum()  # 按地区汇总
product_sales = data.groupby("产品")["销售额"].agg(["mean", "std"])  # 按产品统计

# 第3步：可视化（2×2子图）
fig, axes = plt.subplots(2, 2, figsize=(12, 8))   # 创建2×2子图

# 左上：各地区销售额柱状图
region_sales.plot(kind="bar", ax=axes[0, 0], color="steelblue")  # ax 参数指定子图
axes[0, 0].set_title("各地区总销售额")             # 设置标题
axes[0, 0].set_xticklabels(region_sales.index, rotation=0)  # x标签水平

# 右上：各产品平均销售额
product_sales["mean"].plot(kind="bar", ax=axes[0, 1], color="coral")  # 指定子图
axes[0, 1].set_title("各产品平均销售额")           # 设置标题
axes[0, 1].set_xticklabels(product_sales.index, rotation=0)  # x标签水平

# 左下：销售额分布直方图
axes[1, 0].hist(data["销售额"], bins=30, color="green", alpha=0.7)  # 直方图
axes[1, 0].set_title("销售额分布")                 # 设置标题
axes[1, 0].set_xlabel("销售额")                    # x 轴标签

# 右下：各地区箱线图
data.boxplot(column="销售额", by="地区", ax=axes[1, 1])  # Pandas箱线图
axes[1, 1].set_title("各地区销售额分布")           # 设置标题
plt.suptitle("")                                  # 去掉自动生成的总标题

plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/33_dashboard.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("综合仪表盘已保存")                          # 打印提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 用 Pandas 的 plot 方法画一个折线图")  # 练习1
    print("2. 生成时间序列数据，画原图+滑动平均")    # 练习2
    print("3. 完整流程：生成数据→分组→画4个子图")   # 练习3
