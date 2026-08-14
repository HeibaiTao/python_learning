"""02 - 常用图表类型

学习目标:
    - 掌握柱状图、饼图、直方图、箱线图
    - 理解不同图表的适用场景
    - 了解堆积图与水平柱状图
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# ===== 1. 柱状图 =====
print("--- 柱状图 ---")                            # 打印标题
products = ["手机", "电脑", "平板", "耳机"]        # 产品名称
sales = [150, 80, 60, 120]                        # 销量数据

plt.figure(figsize=(8, 4))                        # 创建画布
plt.bar(products, sales, color=["#4CAF50", "#2196F3", "#FF9800", "#F44336"])  # bar 画柱状图
plt.title("各产品销量对比")                        # 设置标题
plt.xlabel("产品")                                # x 轴标签
plt.ylabel("销量（台）")                           # y 轴标签

# 在柱子上标注数值
for i, v in enumerate(sales):                     # 遍历每个柱子
    plt.text(i, v + 2, str(v), ha="center", fontsize=12)  # text 在柱子上方标注数值

plt.savefig("08_matplotlib/data/06_bar.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("柱状图已保存")                              # 打印提示

# ===== 2. 水平柱状图 =====
print("\n--- 水平柱状图 ---")                      # 打印标题
plt.figure(figsize=(8, 4))                        # 创建画布
plt.barh(products, sales, color="steelblue")      # barh 画水平柱状图
plt.title("各产品销量（水平）")                     # 设置标题
plt.xlabel("销量（台）")                           # x 轴标签
plt.ylabel("产品")                                # y 轴标签
plt.savefig("08_matplotlib/data/07_barh.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("水平柱状图已保存")                          # 打印提示

# ===== 3. 堆积柱状图 =====
print("\n--- 堆积柱状图 ---")                      # 打印标题
q1 = [40, 20, 15, 30]                             # Q1 季度销量
q2 = [50, 30, 20, 35]                             # Q2 季度销量
q3 = [60, 30, 25, 55]                             # Q3 季度销量

plt.figure(figsize=(8, 5))                        # 创建画布
plt.bar(products, q1, label="Q1", color="#2196F3")                # 第一层
plt.bar(products, q2, bottom=q1, label="Q2", color="#4CAF50")     # 第二层（bottom=下面那层）
plt.bar(products, q3, bottom=np.array(q1)+np.array(q2), label="Q3", color="#FF9800")  # 第三层
plt.title("各产品季度销量（堆积）")                 # 设置标题
plt.xlabel("产品")                                # x 轴标签
plt.ylabel("销量")                                # y 轴标签
plt.legend()                                      # 显示图例
plt.savefig("08_matplotlib/data/08_stacked_bar.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("堆积柱状图已保存")                          # 打印提示

# ===== 4. 饼图 =====
print("\n--- 饼图 ---")                            # 打印标题
labels = ["手机", "电脑", "平板", "耳机"]          # 标签
sizes = [150, 80, 60, 120]                        # 数据
colors = ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]  # 颜色
explode = (0.05, 0, 0, 0)                         # 突出第一块（手机）

plt.figure(figsize=(6, 6))                        # 创建画布（正方形适合饼图）
plt.pie(sizes, explode=explode, labels=labels, colors=colors,  # pie 画饼图
        autopct="%1.1f%%", shadow=True, startangle=90)  # autopct 显示百分比，shadow 阴影
plt.title("产品销量占比")                          # 设置标题
plt.axis("equal")                                 # equal 让饼图为正圆
plt.savefig("08_matplotlib/data/09_pie.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("饼图已保存")                                # 打印提示

# ===== 5. 直方图 =====
print("\n--- 直方图 ---")                          # 打印标题
np.random.seed(42)                                # 设置随机种子
scores = np.random.normal(75, 15, 200)            # 生成200个正态分布成绩（均值75，标准差15）

plt.figure(figsize=(8, 4))                        # 创建画布
plt.hist(scores, bins=20, color="steelblue", edgecolor="white", alpha=0.8)  # hist 画直方图
plt.title("考试成绩分布直方图")                     # 设置标题
plt.xlabel("分数")                                # x 轴标签
plt.ylabel("人数")                                # y 轴标签
plt.axvline(scores.mean(), color="red", linestyle="--", label=f"均值={scores.mean():.1f}")  # axvline 画垂直参考线
plt.legend()                                      # 显示图例
plt.savefig("08_matplotlib/data/10_hist.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("直方图已保存")                              # 打印提示

# ===== 6. 箱线图 =====
print("\n--- 箱线图 ---")                          # 打印标题
group_a = np.random.normal(70, 10, 50)            # A组成绩
group_b = np.random.normal(75, 15, 50)            # B组成绩
group_c = np.random.normal(80, 8, 50)             # C组成绩

plt.figure(figsize=(8, 4))                        # 创建画布
plt.boxplot([group_a, group_b, group_c],          # boxplot 画箱线图
            labels=["A组", "B组", "C组"],
            patch_artist=True,                    # patch_artist 填充颜色
            boxprops=dict(facecolor="lightblue"))  # 设置箱子颜色
plt.title("三组成绩箱线图对比")                     # 设置标题
plt.ylabel("分数")                                # y 轴标签
plt.savefig("08_matplotlib/data/11_box.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("箱线图已保存")                              # 打印提示

# ===== 7. 图表选择指南 =====
print("\n--- 图表选择指南 ---")                    # 打印标题
guide = """                                       # 定义图表选择指南文本
┌────────────┬──────────────────────────────┐
│ 图表类型    │ 适用场景                      │
├────────────┼──────────────────────────────┤
│ 折线图      │ 趋势变化（时间序列）           │
│ 散点图      │ 两个变量的关系                 │
│ 柱状图      │ 分类数据对比                   │
│ 饼图        │ 占比/比例                     │
│ 直方图      │ 数据分布                      │
│ 箱线图      │ 分布对比 + 异常值检测          │
└────────────┴──────────────────────────────┘
"""
print(guide)                                      # 打印指南


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 画一个柱状图，展示你一周的学习时间")  # 练习1
    print("2. 生成正态分布数据，画直方图+均值线")   # 练习2
    print("3. 用箱线图对比3组随机数据的分布")       # 练习3
