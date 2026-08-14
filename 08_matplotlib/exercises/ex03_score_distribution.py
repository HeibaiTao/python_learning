"""练习3: 成绩分布分析可视化

用多种图表分析学生成绩分布:
    - 直方图：整体分布
    - 箱线图：各科对比
    - 散点图：两科关系
    - 饼图：等级占比
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# 生成模拟成绩数据
np.random.seed(42)                                # 设置随机种子
n = 100                                           # 学生人数
chinese = np.clip(np.random.normal(75, 12, n), 0, 100).astype(int)  # 语文（正态分布，截断0-100）
math = np.clip(np.random.normal(72, 15, n), 0, 100).astype(int)     # 数学
english = np.clip(np.random.normal(78, 10, n), 0, 100).astype(int)  # 英语

# 创建 2×2 子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 创建2×2子图
fig.suptitle("学生成绩分布分析", fontsize=16, fontweight="bold")  # 总标题

# === 子图1: 三科成绩直方图 ===
axes[0, 0].hist(chinese, bins=15, alpha=0.6, label="语文", color="#2196F3")  # 语文直方图
axes[0, 0].hist(math, bins=15, alpha=0.6, label="数学", color="#4CAF50")    # 数学直方图
axes[0, 0].hist(english, bins=15, alpha=0.6, label="英语", color="#FF9800")  # 英语直方图
axes[0, 0].set_title("三科成绩分布对比")           # 子图标题
axes[0, 0].set_xlabel("分数")                     # x 轴标签
axes[0, 0].set_ylabel("人数")                     # y 轴标签
axes[0, 0].legend()                               # 图例
axes[0, 0].grid(True, alpha=0.3)                  # 网格

# === 子图2: 箱线图对比 ===
box_data = [chinese, math, english]               # 三科数据
bp = axes[0, 1].boxplot(box_data, labels=["语文", "数学", "英语"],  # 箱线图
                        patch_artist=True, widths=0.5)
colors = ["#2196F3", "#4CAF50", "#FF9800"]        # 定义颜色
for patch, color in zip(bp["boxes"], colors):     # 给每个箱子上色
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
axes[0, 1].set_title("三科成绩箱线图")             # 子图标题
axes[0, 1].set_ylabel("分数")                     # y 轴标签
axes[0, 1].grid(True, alpha=0.3)                  # 网格

# === 子图3: 语文与数学散点图 ===
scatter = axes[1, 0].scatter(chinese, math, c=english, cmap="viridis", alpha=0.7, edgecolors="black")  # 散点图
axes[1, 0].set_title("语文 vs 数学（颜色=英语成绩）")  # 子图标题
axes[1, 0].set_xlabel("语文成绩")                 # x 轴标签
axes[1, 0].set_ylabel("数学成绩")                 # y 轴标签
plt.colorbar(scatter, ax=axes[1, 0], label="英语成绩")  # 颜色条

# 计算相关系数
corr = np.corrcoef(chinese, math)[0, 1]           # 计算相关系数
axes[1, 0].text(0.05, 0.95, f"相关系数={corr:.2f}", transform=axes[1, 0].transAxes,  # text 标注
                fontsize=11, verticalalignment="top", bbox=dict(boxstyle="round", facecolor="wheat"))

# === 子图4: 等级占比饼图 ===
# 计算总分等级
total = (chinese + math + english) / 3            # 三科平均分
grades = []                                       # 等级列表
for score in total:                               # 遍历每个学生
    if score >= 90:                               # 90+ 优秀
        grades.append("优秀")
    elif score >= 80:                             # 80-89 良好
        grades.append("良好")
    elif score >= 60:                             # 60-79 及格
        grades.append("及格")
    else:                                         # 60以下 不及格
        grades.append("不及格")

grade_names = ["优秀", "良好", "及格", "不及格"]   # 等级名称
grade_counts = [grades.count(g) for g in grade_names]  # 统计各等级人数
grade_colors = ["#4CAF50", "#2196F3", "#FF9800", "#F44336"]  # 颜色

axes[1, 1].pie(grade_counts, labels=grade_names, autopct="%1.0f%%",  # 饼图
               colors=grade_colors, startangle=90, explode=(0.05, 0, 0, 0))
axes[1, 1].set_title("成绩等级占比")               # 子图标题

plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/ex03_scores.png", dpi=150, bbox_inches="tight")  # 保存
plt.close()                                       # 关闭画布
print("成绩分布分析图已保存到 data/ex03_scores.png")  # 打印提示
