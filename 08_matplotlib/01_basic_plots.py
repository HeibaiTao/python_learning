"""01 - Matplotlib 基础绘图

学习目标:
    - 理解 figure / axes 的概念
    - 掌握折线图与散点图
    - 了解基本图表元素（标题、标签、图例）
"""

import matplotlib.pyplot as plt                   # 导入 matplotlib 的 pyplot 模块，缩写为 plt
import numpy as np                                # 导入 numpy 模块

# 设置中文字体（Windows 用 SimHei，macOS 用 Arial Unicode MS）
plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体为黑体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示问题

# ===== 1. 最简单的折线图 =====
print("--- 折线图 ---")                            # 打印标题
x = np.array([1, 2, 3, 4, 5])                     # x 轴数据
y = np.array([2, 4, 1, 5, 3])                     # y 轴数据

plt.figure(figsize=(8, 4))                        # 创建画布，figsize 设置宽高（英寸）
plt.plot(x, y)                                    # plot 画折线图
plt.title("简单折线图")                            # 设置标题
plt.xlabel("X轴")                                 # 设置 x 轴标签
plt.ylabel("Y轴")                                 # 设置 y 轴标签
plt.savefig("08_matplotlib/data/01_line.png", dpi=100, bbox_inches="tight")  # 保存图片，dpi 分辨率
plt.close()                                       # 关闭画布，释放内存
print("折线图已保存")                              # 打印提示

# ===== 2. 多条折线 =====
print("\n--- 多条折线 ---")                        # 打印标题
x = np.linspace(0, 10, 50)                        # 生成0-10之间50个均匀点
plt.figure(figsize=(8, 4))                        # 创建画布
plt.plot(x, np.sin(x), label="sin(x)", color="blue", linewidth=2)   # 画 sin 曲线
plt.plot(x, np.cos(x), label="cos(x)", color="red", linewidth=2, linestyle="--")  # 画 cos 曲线（虚线）
plt.title("正弦与余弦曲线")                         # 设置标题
plt.xlabel("x")                                   # x 轴标签
plt.ylabel("y")                                   # y 轴标签
plt.legend()                                      # 显示图例（根据 label 自动生成）
plt.grid(True, alpha=0.3)                         # grid 显示网格线，alpha 透明度
plt.savefig("08_matplotlib/data/02_multi_line.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("多线图已保存")                              # 打印提示

# ===== 3. 散点图 =====
print("\n--- 散点图 ---")                          # 打印标题
np.random.seed(42)                                # 设置随机种子
x_scatter = np.random.rand(50) * 10               # 50个随机 x 值（0-10）
y_scatter = x_scatter * 2 + np.random.randn(50) * 3  # y 与 x 线性相关，加噪声

plt.figure(figsize=(8, 5))                        # 创建画布
plt.scatter(x_scatter, y_scatter, c="green", alpha=0.6, edgecolors="black")  # scatter 画散点图
plt.title("散点图：x 与 y 的关系")                 # 设置标题
plt.xlabel("X值")                                 # x 轴标签
plt.ylabel("Y值")                                 # y 轴标签
plt.savefig("08_matplotlib/data/03_scatter.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("散点图已保存")                              # 打印提示

# ===== 4. plot 常用参数 =====
print("\n--- plot 参数详解 ---")                   # 打印标题
x = np.linspace(0, 5, 20)                         # 生成数据
plt.figure(figsize=(10, 4))                       # 创建画布
plt.plot(x, x, color="red", linestyle="-", marker="o", label="y=x")       # 实线+圆点
plt.plot(x, x**2, color="blue", linestyle="--", marker="s", label="y=x²")  # 虚线+方块
plt.plot(x, x**3, color="green", linestyle=":", marker="^", label="y=x³")  # 点线+三角
plt.title("不同线型和标记")                        # 设置标题
plt.xlabel("x")                                   # x 轴标签
plt.ylabel("y")                                   # y 轴标签
plt.legend()                                      # 显示图例
plt.grid(True, alpha=0.3)                         # 显示网格

# 线型说明:
# linestyle="-"  实线      marker="o" 圆点
# linestyle="--" 虚线      marker="s" 方块
# linestyle=":"  点线      marker="^" 三角
# linestyle="-." 点划线     marker="D" 菱形

plt.savefig("08_matplotlib/data/04_styles.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("样式图已保存")                              # 打印提示

# ===== 5. 简便写法（格式字符串）=====
print("\n--- 格式字符串简写 ---")                   # 打印标题
plt.figure(figsize=(8, 4))                        # 创建画布
plt.plot([1, 2, 3, 4], [1, 4, 2, 3], "ro-")       # "ro-" = 红色+圆点+实线
plt.plot([1, 2, 3, 4], [3, 2, 4, 1], "g--s")      # "g--s" = 绿色+虚线+方块
plt.title("格式字符串简写")                        # 设置标题
plt.savefig("08_matplotlib/data/05_format.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("格式字符串图已保存")                        # 打印提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 画出 y=x² 在 -5到5 的曲线")          # 练习1
    print("2. 在同一张图上画3条不同颜色的折线")      # 练习2
    print("3. 画一个散点图，点的颜色随 y 值变化")    # 练习3
