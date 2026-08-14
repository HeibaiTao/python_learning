"""04 - 子图与布局

学习目标:
    - 掌握 subplot / subplots 创建子图
    - 理解 figure / axes 面向对象绘图
    - 了解子图共享坐标轴
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# ===== 1. subplot（旧式写法）=====
print("--- subplot ---")                           # 打印标题
plt.figure(figsize=(12, 4))                       # 创建画布

plt.subplot(1, 3, 1)                              # subplot(行, 列, 编号) → 1行3列第1个
plt.plot([1, 2, 3], [1, 4, 2], "r-")              # 画折线
plt.title("子图1")                                 # 设置标题

plt.subplot(1, 3, 2)                              # 第2个子图
plt.bar(["A", "B", "C"], [3, 7, 2])               # 画柱状图
plt.title("子图2")                                 # 设置标题

plt.subplot(1, 3, 3)                              # 第3个子图
plt.scatter([1, 2, 3], [3, 1, 4])                 # 画散点图
plt.title("子图3")                                 # 设置标题

plt.tight_layout()                                # tight_layout 自动调整间距，防止重叠
plt.savefig("08_matplotlib/data/17_subplots.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("子图已保存")                                # 打印提示

# ===== 2. subplots（推荐写法）=====
print("\n--- subplots（推荐）---")                  # 打印标题
fig, axes = plt.subplots(2, 2, figsize=(10, 8))   # subplots 一次创建2×2的4个子图，返回 fig 和 axes
# fig 是整个画布，axes 是子图数组的集合

x = np.linspace(0, 5, 50)                         # 生成共享数据

# axes[行, 列] 访问每个子图
axes[0, 0].plot(x, x, color="blue")               # 左上：y=x
axes[0, 0].set_title("y = x")                     # set_title 设置子图标题

axes[0, 1].plot(x, x**2, color="red")             # 右上：y=x²
axes[0, 1].set_title("y = x²")

axes[1, 0].plot(x, x**3, color="green")           # 左下：y=x³
axes[1, 0].set_title("y = x³")

axes[1, 1].plot(x, np.sin(x), color="purple")     # 右下：y=sin(x)
axes[1, 1].set_title("y = sin(x)")

# 统一设置
for ax in axes.flat:                              # axes.flat 把2D数组展平为1D遍历
    ax.set_xlabel("x")                            # 每个子图设置 x 轴标签
    ax.set_ylabel("y")                            # 每个子图设置 y 轴标签
    ax.grid(True, alpha=0.3)                      # 每个子图显示网格

fig.suptitle("四种函数图像", fontsize=14, fontweight="bold")  # suptitle 设置总标题
plt.tight_layout()                                # 自动调整间距
plt.savefig("08_matplotlib/data/18_subplots_oo.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("面向对象子图已保存")                        # 打印提示

# ===== 3. 共享坐标轴 =====
print("\n--- 共享坐标轴 ---")                      # 打印标题
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)  # sharex=True 共享 x 轴

x = np.linspace(0, 10, 100)                       # 生成数据
axes[0].plot(x, np.sin(x), color="blue")          # 上图：sin
axes[0].set_title("sin(x)")                       # 设置标题
axes[0].set_ylabel("振幅")                        # 设置 y 轴标签

axes[1].plot(x, np.cos(x), color="red")           # 下图：cos
axes[1].set_title("cos(x)")                       # 设置标题
axes[1].set_xlabel("x")                           # 只需在下面的子图设 x 标签（共享）
axes[1].set_ylabel("振幅")                        # 设置 y 轴标签

fig.suptitle("共享X轴的子图", fontsize=14)        # 设置总标题
plt.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/19_share_axis.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("共享轴子图已保存")                          # 打印提示

# ===== 4. 不规则布局 =====
print("\n--- 不规则布局 ---")                      # 打印标题
fig = plt.figure(figsize=(10, 6))                 # 创建画布

# add_subplot 用3位数字：行数+列数+编号
ax1 = fig.add_subplot(2, 3, 1)                    # 2行3列第1个
ax1.set_title("位置1")
ax1.plot([1, 2, 3], [1, 2, 1])

ax2 = fig.add_subplot(2, 3, 2)                    # 第2个
ax2.set_title("位置2")
ax2.bar(["A", "B"], [3, 5])

ax3 = fig.add_subplot(2, 3, (3, 6))               # 第3-6个合并（跨2行）
ax3.set_title("位置3-6（跨行）")
ax3.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)))

ax4 = fig.add_subplot(2, 3, 4)                    # 第4个
ax4.set_title("位置4")
ax4.hist(np.random.randn(50), bins=10)

ax5 = fig.add_subplot(2, 3, 5)                    # 第5个
ax5.set_title("位置5")
ax5.scatter(np.random.rand(20), np.random.rand(20))

plt.tight_layout()                                # 自动调整间距
plt.savefig("08_matplotlib/data/20_irregular.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("不规则布局图已保存")                        # 打印提示

# ===== 5. 双Y轴 =====
print("\n--- 双Y轴 ---")                           # 打印标题
fig, ax1 = plt.subplots(figsize=(10, 4))          # 创建画布和主坐标轴

x = np.arange(1, 13)                              # 1-12月
sales = [30, 35, 40, 38, 45, 50, 55, 52, 48, 42, 35, 32]  # 销售额
temp = [5, 8, 13, 18, 23, 28, 32, 31, 26, 20, 12, 6]      # 温度

color1 = "tab:blue"                               # 第一条线的颜色
ax1.bar(x, sales, color=color1, alpha=0.7, label="销售额")  # 左Y轴画柱状图
ax1.set_xlabel("月份")                            # x 轴标签
ax1.set_ylabel("销售额（万元）", color=color1)     # 左Y轴标签
ax1.tick_params(axis="y", labelcolor=color1)      # 左Y轴刻度颜色

ax2 = ax1.twinx()                                 # twinx 创建共享X轴的第二Y轴
color2 = "tab:red"                                # 第二条线的颜色
ax2.plot(x, temp, color=color2, marker="o", linewidth=2, label="温度")  # 右Y轴画折线
ax2.set_ylabel("温度（℃）", color=color2)         # 右Y轴标签
ax2.tick_params(axis="y", labelcolor=color2)      # 右Y轴刻度颜色

plt.title("销售额与温度关系（双Y轴）")              # 设置标题
fig.tight_layout()                                # 自动调整
plt.savefig("08_matplotlib/data/21_twinx.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("双Y轴图已保存")                             # 打印提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 用 subplots 创建 2×2 子图，画4种函数")  # 练习1
    print("2. 画一个双Y轴图：左轴柱状图，右轴折线图")  # 练习2
    print("3. 用 add_subplot 创建不规则布局")       # 练习3
