"""练习1: 城市气温变化可视化

用 Matplotlib 可视化多个城市的气温变化:
    - 读取/生成气温数据
    - 画多条折线图对比
    - 标注最高温和最低温
    - 添加参考线
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# 生成模拟数据：3个城市12个月的平均气温
np.random.seed(42)                                # 设置随机种子
months = [f"{i}月" for i in range(1, 13)]         # 月份标签
beijing = [-3, 0, 6, 14, 20, 25, 27, 26, 21, 14, 5, -1]      # 北京月均温
shanghai = [4, 6, 10, 16, 21, 25, 29, 29, 25, 19, 13, 7]      # 上海月均温
guangzhou = [14, 15, 18, 22, 26, 28, 30, 30, 29, 25, 20, 16]  # 广州月均温

# 创建画布
plt.figure(figsize=(12, 5))                       # 创建画布

# 画三条折线
plt.plot(months, beijing, "o-", color="blue", linewidth=2, label="北京")    # 北京
plt.plot(months, shanghai, "s-", color="red", linewidth=2, label="上海")    # 上海
plt.plot(months, guangzhou, "^-", color="green", linewidth=2, label="广州")  # 广州

# 标注北京最高温和最低温
max_idx = beijing.index(max(beijing))             # 北京最高温的月份索引
min_idx = beijing.index(min(beijing))             # 北京最低温的月份索引
plt.annotate(f"最高{max(beijing)}℃",               # annotate 标注最高温
             xy=(max_idx, max(beijing)),          # 箭头指向
             xytext=(max_idx - 1, max(beijing) + 3),  # 文字位置
             arrowprops=dict(arrowstyle="->", color="blue"),  # 箭头样式
             fontsize=11, color="blue")
plt.annotate(f"最低{min(beijing)}℃",               # annotate 标注最低温
             xy=(min_idx, min(beijing)),
             xytext=(min_idx + 0.5, min(beijing) - 4),
             arrowprops=dict(arrowstyle="->", color="blue"),
             fontsize=11, color="blue")

# 添加参考线
plt.axhline(y=0, color="gray", linestyle="--", alpha=0.5, label="0℃冰点")  # 冰点线
plt.axhline(y=30, color="orange", linestyle="--", alpha=0.5, label="30℃高温线")  # 高温线

# 设置图表元素
plt.title("2024年三城市月均气温对比", fontsize=16, fontweight="bold")  # 标题
plt.xlabel("月份", fontsize=12)                   # x 轴标签
plt.ylabel("温度（℃）", fontsize=12)              # y 轴标签
plt.ylim(-8, 38)                                  # y 轴范围
plt.legend(loc="upper left")                      # 图例
plt.grid(True, alpha=0.3)                         # 网格
plt.tight_layout()                                # 自动调整

plt.savefig("08_matplotlib/data/ex01_temperature.png", dpi=150, bbox_inches="tight")  # 保存
plt.close()                                       # 关闭画布
print("气温对比图已保存到 data/ex01_temperature.png")  # 打印提示
