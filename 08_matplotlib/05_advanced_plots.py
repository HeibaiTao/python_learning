"""05 - 高级图表

学习目标:
    - 掌握热力图、面积图
    - 了解3D绘图基础
    - 了解等高线图
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# ===== 1. 热力图 =====
print("--- 热力图 ---")                            # 打印标题
np.random.seed(42)                                # 设置随机种子
data = np.random.randint(0, 100, size=(5, 5))     # 生成5×5随机数据矩阵
labels = ["周一", "周二", "周三", "周四", "周五"]   # 行标签
products = ["手机", "电脑", "平板", "耳机", "配件"]  # 列标签

fig, ax = plt.subplots(figsize=(8, 6))            # 创建画布
im = ax.imshow(data, cmap="YlOrRd")               # imshow 画热力图，cmap 设置颜色映射

# 设置刻度标签
ax.set_xticks(np.arange(len(products)))           # 设置 x 刻度位置
ax.set_yticks(np.arange(len(labels)))             # 设置 y 刻度位置
ax.set_xticklabels(products)                      # 设置 x 刻度标签
ax.set_yticklabels(labels)                        # 设置 y 刻度标签

# 在每个格子中标注数值
for i in range(len(labels)):                      # 遍历行
    for j in range(len(products)):                # 遍历列
        ax.text(j, i, data[i, j], ha="center", va="center", fontsize=14)  # text 标注数值

plt.colorbar(im, ax=ax, label="销量")             # colorbar 添加颜色条
plt.title("各产品每日销量热力图")                   # 设置标题
plt.savefig("08_matplotlib/data/22_heatmap.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("热力图已保存")                              # 打印提示

# ===== 2. 面积图 =====
print("\n--- 面积图 ---")                          # 打印标题
months = ["1月", "2月", "3月", "4月", "5月", "6月"]  # 月份
product_a = [10, 15, 20, 25, 30, 35]             # 产品A销量
product_b = [5, 8, 12, 15, 18, 22]               # 产品B销量
product_c = [3, 5, 8, 10, 12, 15]                # 产品C销量

plt.figure(figsize=(10, 4))                       # 创建画布
plt.stackplot(months, product_a, product_b, product_c,  # stackplot 画堆积面积图
              labels=["产品A", "产品B", "产品C"],
              colors=["#2196F3", "#4CAF50", "#FF9800"],
              alpha=0.8)                          # alpha 透明度
plt.title("各产品月度销量（面积图）")               # 设置标题
plt.xlabel("月份")                                # x 轴标签
plt.ylabel("销量")                                # y 轴标签
plt.legend(loc="upper left")                      # 显示图例
plt.savefig("08_matplotlib/data/23_area.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("面积图已保存")                              # 打印提示

# ===== 3. 3D 散点图 =====
print("\n--- 3D散点图 ---")                        # 打印标题
np.random.seed(42)                                # 设置随机种子
fig = plt.figure(figsize=(8, 6))                  # 创建画布
ax = fig.add_subplot(111, projection="3d")        # projection="3d" 创建3D坐标轴

n = 100                                           # 点的数量
x = np.random.rand(n) * 10                        # 随机 x 坐标
y = np.random.rand(n) * 10                        # 随机 y 坐标
z = np.random.rand(n) * 10                        # 随机 z 坐标
colors = z                                        # 颜色随 z 值变化

scatter = ax.scatter(x, y, z, c=colors, cmap="viridis", alpha=0.6)  # 3D散点图
ax.set_xlabel("X轴")                              # 设置 x 轴标签
ax.set_ylabel("Y轴")                              # 设置 y 轴标签
ax.set_zlabel("Z轴")                              # 设置 z 轴标签
plt.title("3D散点图")                              # 设置标题
plt.colorbar(scatter, ax=ax, label="Z值", shrink=0.5)  # 添加颜色条，shrink 缩小
plt.savefig("08_matplotlib/data/24_3d_scatter.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("3D散点图已保存")                            # 打印提示

# ===== 4. 3D 曲面图 =====
print("\n--- 3D曲面图 ---")                        # 打印标题
fig = plt.figure(figsize=(8, 6))                  # 创建画布
ax = fig.add_subplot(111, projection="3d")        # 创建3D坐标轴

x = np.linspace(-5, 5, 50)                        # x 轴数据
y = np.linspace(-5, 5, 50)                        # y 轴数据
X, Y = np.meshgrid(x, y)                          # meshgrid 生成网格坐标
Z = np.sin(np.sqrt(X**2 + Y**2))                  # 计算 z = sin(√(x²+y²))

surf = ax.plot_surface(X, Y, Z, cmap="coolwarm")  # plot_surface 画3D曲面
ax.set_xlabel("X")                                # 设置 x 轴标签
ax.set_ylabel("Y")                                # 设置 y 轴标签
ax.set_zlabel("Z")                                # 设置 z 轴标签
plt.title("z = sin(√(x²+y²))")                    # 设置标题
plt.colorbar(surf, ax=ax, shrink=0.5)             # 添加颜色条
plt.savefig("08_matplotlib/data/25_3d_surface.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("3D曲面图已保存")                            # 打印提示

# ===== 5. 等高线图 =====
print("\n--- 等高线图 ---")                        # 打印标题
fig, ax = plt.subplots(figsize=(8, 6))            # 创建画布

x = np.linspace(-3, 3, 100)                       # x 数据
y = np.linspace(-3, 3, 100)                       # y 数据
X, Y = np.meshgrid(x, y)                          # 生成网格
Z = X**2 + Y**2                                   # z = x² + y²（抛物面）

contour = ax.contourf(X, Y, Z, levels=20, cmap="RdYlBu_r")  # contourf 填充等高线
ax.contour(X, Y, Z, levels=10, colors="black", linewidths=0.5)  # contour 画等高线（线条）
plt.colorbar(contour, ax=ax, label="Z值")         # 添加颜色条
plt.title("等高线图: z = x² + y²")                # 设置标题
plt.xlabel("X")                                   # x 轴标签
plt.ylabel("Y")                                   # y 轴标签
plt.savefig("08_matplotlib/data/26_contour.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("等高线图已保存")                            # 打印提示

# ===== 6. 雷达图 =====
print("\n--- 雷达图 ---")                          # 打印标题
categories = ["速度", "力量", "技巧", "耐力", "智力"]  # 评估维度
values = [8, 6, 7, 5, 9]                          # 各维度得分（0-10）
N = len(categories)                               # 维度数

# 计算角度
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()  # 均分圆周
values_plot = values + values[:1]                 # 闭合雷达图（首尾相连）
angles_plot = angles + angles[:1]                 # 角度也闭合

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))  # polar=True 极坐标
ax.plot(angles_plot, values_plot, "o-", linewidth=2)  # 画雷达线
ax.fill(angles_plot, values_plot, alpha=0.25)     # fill 填充
ax.set_xticks(angles)                             # 设置刻度位置
ax.set_xticklabels(categories)                    # 设置刻度标签
ax.set_ylim(0, 10)                                # 设置范围
ax.set_title("能力雷达图", fontsize=14)           # 设置标题
plt.savefig("08_matplotlib/data/27_radar.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("雷达图已保存")                              # 打印提示


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 用热力图展示一个5×5的相关系数矩阵")  # 练习1
    print("2. 画一个3D曲面图 z = sin(x)*cos(y)")  # 练习2
    print("3. 画一个能力雷达图（5个维度）")         # 练习3
