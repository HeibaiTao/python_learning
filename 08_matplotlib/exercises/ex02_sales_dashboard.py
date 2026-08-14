"""练习2: 销售数据仪表盘

综合练习：用 2×2 子图创建销售数据仪表盘
    - 子图1：月度销售趋势折线图
    - 子图2：各产品销量柱状图
    - 子图3：地区占比饼图
    - 子图4：价格分布直方图
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# 生成模拟销售数据
np.random.seed(42)                                # 设置随机种子
n = 300                                           # 记录数
df = pd.DataFrame({                               # 创建销售 DataFrame
    "月份": np.random.choice(range(1, 7), n),     # 1-6月
    "产品": np.random.choice(["手机", "电脑", "平板", "耳机"], n),
    "地区": np.random.choice(["华北", "华东", "华南", "西部"], n),
    "金额": np.random.exponential(2000, n).astype(int),
})

# 创建 2×2 仪表盘
fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 创建2×2子图
fig.suptitle("2024年上半年销售数据仪表盘", fontsize=16, fontweight="bold")  # 总标题

# === 子图1: 月度销售趋势 ===
monthly = df.groupby("月份")["金额"].sum()        # 按月汇总
axes[0, 0].plot(monthly.index, monthly.values, "o-", color="#2196F3", linewidth=2)  # 折线图
axes[0, 0].fill_between(monthly.index, monthly.values, alpha=0.2, color="#2196F3")  # 填充
axes[0, 0].set_title("月度销售趋势", fontsize=13)  # 子图标题
axes[0, 0].set_xlabel("月份")                     # x 轴标签
axes[0, 0].set_ylabel("销售额（元）")             # y 轴标签
axes[0, 0].set_xticks(range(1, 7))               # 设置刻度
axes[0, 0].grid(True, alpha=0.3)                  # 网格

# === 子图2: 各产品销量柱状图 ===
product_qty = df.groupby("产品")["金额"].sum().sort_values(ascending=False)  # 按产品汇总
colors = ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]  # 定义颜色
bars = axes[0, 1].bar(product_qty.index, product_qty.values, color=colors)  # 柱状图
axes[0, 1].set_title("各产品销售额", fontsize=13)  # 子图标题
axes[0, 1].set_ylabel("销售额（元）")             # y 轴标签
for bar, val in zip(bars, product_qty.values):    # 遍历柱子标注数值
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, val + 5000,  # 位置
                    f"{val/10000:.1f}万", ha="center", fontsize=10)  # 标注（万元）

# === 子图3: 地区占比饼图 ===
region_sales = df.groupby("地区")["金额"].sum()   # 按地区汇总
axes[1, 0].pie(region_sales.values, labels=region_sales.index,  # 饼图
               autopct="%1.1f%%", startangle=90,  # 显示百分比
               colors=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"])  # 颜色
axes[1, 0].set_title("各地区销售占比", fontsize=13)  # 子图标题

# === 子图4: 金额分布直方图 ===
axes[1, 1].hist(df["金额"], bins=30, color="#FF5722", alpha=0.7, edgecolor="white")  # 直方图
mean_val = df["金额"].mean()                      # 计算均值
axes[1, 1].axvline(mean_val, color="black", linestyle="--", linewidth=2, label=f"均值={mean_val:.0f}")  # 均值线
axes[1, 1].set_title("订单金额分布", fontsize=13)  # 子图标题
axes[1, 1].set_xlabel("金额（元）")               # x 轴标签
axes[1, 1].set_ylabel("订单数")                   # y 轴标签
axes[1, 1].legend()                               # 图例

plt.tight_layout()                                # 自动调整间距
plt.savefig("08_matplotlib/data/ex02_dashboard.png", dpi=150, bbox_inches="tight")  # 保存
plt.close()                                       # 关闭画布
print("销售仪表盘已保存到 data/ex02_dashboard.png")  # 打印提示
