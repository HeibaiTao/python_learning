"""03 - 样式与自定义

学习目标:
    - 掌握颜色、字体、线型的自定义
    - 理解坐标轴范围与刻度设置
    - 了解注释、箭头与文本标注
"""

import matplotlib.pyplot as plt                   # 导入 pyplot 模块
import numpy as np                                # 导入 numpy 模块

plt.rcParams["font.sans-serif"] = ["SimHei"]      # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False        # 解决负号显示

# ===== 1. 颜色设置 =====
print("--- 颜色设置 ---")                          # 打印标题
x = np.linspace(0, 5, 30)                         # 生成 x 数据
plt.figure(figsize=(10, 4))                       # 创建画布

# 颜色多种写法
plt.plot(x, x, color="red", label="颜色名")        # 用颜色英文名
plt.plot(x, x+1, color="#2196F3", label="十六进制")  # 用十六进制码
plt.plot(x, x+2, color=(0.2, 0.6, 0.3), label="RGB元组")  # 用 RGB 元组（0-1范围）
plt.plot(x, x+3, color="C0", label="默认色环C0")   # 用色环索引 C0-C9
plt.plot(x, x+4, color="purple", alpha=0.5, label="半透明")  # alpha 透明度

plt.title("颜色设置方式")                          # 设置标题
plt.legend()                                      # 显示图例
plt.savefig("08_matplotlib/data/12_colors.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("颜色图已保存")                              # 打印提示

# ===== 2. 坐标轴设置 =====
print("\n--- 坐标轴设置 ---")                      # 打印标题
x = np.linspace(-3, 3, 100)                       # 生成 -3到3 的数据
plt.figure(figsize=(8, 5))                        # 创建画布
plt.plot(x, x**2, color="blue", linewidth=2)     # 画 y=x²

plt.title("y = x²", fontsize=16, fontweight="bold")  # fontsize 字号，fontweight 粗细
plt.xlabel("X轴", fontsize=12)                    # x 轴标签
plt.ylabel("Y轴", fontsize=12)                    # y 轴标签

# 设置坐标轴范围
plt.xlim(-3, 3)                                   # xlim 设置 x 轴范围
plt.ylim(-1, 10)                                  # ylim 设置 y 轴范围

# 设置刻度
plt.xticks(np.arange(-3, 4, 1))                   # xticks 设置 x 轴刻度
plt.yticks(np.arange(0, 11, 2))                   # yticks 设置 y 轴刻度

# 网格
plt.grid(True, linestyle="--", alpha=0.5)         # 设置网格样式

plt.savefig("08_matplotlib/data/13_axis.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("坐标轴图已保存")                            # 打印提示

# ===== 3. 注释与箭头 =====
print("\n--- 注释与箭头 ---")                      # 打印标题
x = np.linspace(0, 10, 100)                       # 生成数据
y = np.sin(x)                                     # 计算 sin

plt.figure(figsize=(10, 4))                       # 创建画布
plt.plot(x, y, color="blue", linewidth=2)        # 画曲线
plt.title("注释示例", fontsize=14)                # 设置标题

# 标注最大值点
max_x = np.pi / 2                                 # sin 最大值的 x 坐标
max_y = 1                                         # sin 最大值
plt.plot(max_x, max_y, "ro", markersize=10)       # 用红圆点标记最大值
plt.annotate("最大值 (π/2, 1)",                    # annotate 添加注释
             xy=(max_x, max_y),                   # xy 箭头指向的坐标
             xytext=(max_x + 1, 0.5),             # xytext 文字位置
             fontsize=12,                         # 字号
             arrowprops=dict(arrowstyle="->", color="red"))  # arrowprops 箭头样式

# 水平参考线
plt.axhline(y=0, color="gray", linestyle="-", alpha=0.5)  # axhline 水平线

plt.xlabel("x")                                   # x 轴标签
plt.ylabel("sin(x)")                              # y 轴标签
plt.grid(True, alpha=0.3)                         # 显示网格
plt.savefig("08_matplotlib/data/14_annotate.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("注释图已保存")                              # 打印提示

# ===== 4. 图例位置 =====
print("\n--- 图例位置 ---")                        # 打印标题
plt.figure(figsize=(8, 4))                        # 创建画布
for i in range(4):                                # 画4条线
    plt.plot(np.linspace(0, 5, 20), np.linspace(0, 5, 20) + i, label=f"线{i+1}")

plt.legend(loc="upper left", fontsize=10, framealpha=0.9)  # loc 设置位置：upper/lower + left/right/center
plt.title("图例位置设置")                          # 设置标题
plt.savefig("08_matplotlib/data/15_legend.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
print("图例图已保存")                              # 打印提示

# ===== 5. 内置样式 =====
print("\n--- 内置样式 ---")                        # 打印标题
styles = plt.style.available                      # 获取所有可用样式
print("可用样式:", styles[:8], "...")             # 打印前8个样式

x = np.linspace(0, 10, 50)                        # 生成数据
plt.style.use("ggplot")                           # use 使用 ggplot 样式（类似R语言风格）
plt.figure(figsize=(8, 4))                        # 创建画布
plt.plot(x, np.sin(x), label="sin")               # 画 sin
plt.plot(x, np.cos(x), label="cos")               # 画 cos
plt.title("ggplot 样式")                           # 设置标题
plt.legend()                                      # 显示图例
plt.savefig("08_matplotlib/data/16_style.png", dpi=100, bbox_inches="tight")
plt.close()                                       # 关闭画布
plt.style.use("default")                          # 恢复默认样式
print("样式图已保存")                              # 打印提示

# ===== 6. 保存图片参数 =====
print("\n--- 保存参数 ---")                        # 打印标题
print("""
savefig 常用参数:
  dpi=100/300        分辨率（300适合印刷）
  bbox_inches="tight" 自动裁剪空白
  facecolor="white"   背景色
  transparent=True    透明背景
""")


if __name__ == "__main__":                        # 判断是否直接运行此脚本
    print("\n[练习] 请尝试:")                      # 打印练习提示
    print("1. 画一条曲线，标注最大值和最小值点")     # 练习1
    print("2. 尝试3种不同的 plt.style.use 样式")   # 练习2
    print("3. 自定义坐标轴范围、刻度和网格")        # 练习3
