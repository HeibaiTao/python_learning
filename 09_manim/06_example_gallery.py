"""06 - 官方示例精选

学习目标:
    - 通过官方示例综合运用所学知识
    - 理解 Manim CE Logo 的构建方式
    - 了解向量箭头与坐标系的结合

运行方式:
    manim -pql 06_example_gallery.py ManimLogo
    manim -pql 06_example_gallery.py VectorArrow
    manim -pql 06_example_gallery.py GraphArea
"""

from manim import *                               # 导入 manim 库
import numpy as np                                # 导入 numpy 模块


# ===== 1. Manim CE Logo（官方示例）=====
class ManimLogo(Scene):                           # 定义 Logo 场景
    """用基本图形拼出 Manim CE Logo"""            # 类的说明文档

    def construct(self):                          # 场景入口
        self.camera.background_color = "#ece6e2"  # 设置背景色为浅灰

        # 定义 Logo 配色
        logo_green = "#87c2a5"                     # 绿色
        logo_blue = "#525893"                      # 蓝色
        logo_red = "#e07a5f"                       # 红色
        logo_black = "#343434"                     # 黑色

        # 创建数学符号 M
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)  # 放大7倍
        ds_m.shift(2.25 * LEFT + 1.5 * UP)        # 移到左上方

        # 创建三个基本图形
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)    # 绿色圆在左
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)       # 蓝色方在上
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)  # 红色三角在右

        # 用 VGroup 组合（顺序很重要，后面的覆盖前面的）
        logo = VGroup(triangle, square, circle, ds_m)  # 按 三角→方→圆→M 的顺序组合
        logo.move_to(ORIGIN)                      # 整体移到中心

        self.add(logo)                            # 直接添加（不需动画）
        self.wait()                               # 暂停1秒


# ===== 2. 向量箭头（官方示例）=====
class VectorArrow(Scene):                         # 定义向量箭头场景
    """在坐标平面上展示向量"""                    # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建坐标平面
        numberplane = NumberPlane(                # NumberPlane 坐标平面
            x_range=[-5, 5, 1],                   # x 轴范围
            y_range=[-5, 5, 1],                   # y 轴范围
        )

        # 原点
        dot = Dot(ORIGIN)                         # 原点圆点

        # 从原点到(2,2)的箭头
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)  # buff=0 箭头紧贴起点

        # 坐标标注
        origin_text = Text("(0, 0)", font_size=24).next_to(dot, DOWN)  # 原点标注
        tip_text = Text("(2, 2)", font_size=24).next_to(arrow.get_end(), RIGHT)  # 箭头终点标注

        self.add(numberplane, dot, arrow, origin_text, tip_text)  # 一次性添加所有对象
        self.wait()                               # 暂停1秒


# ===== 3. 函数面积积分（经典教学动画）=====
class GraphArea(Scene):                           # 定义面积积分场景
    """用阴影区域表示函数积分面积"""              # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建坐标平面
        plane = NumberPlane(                      # 坐标平面
            x_range=[0, 5, 1],                    # x 轴 0到5
            y_range=[0, 10, 2],                   # y 轴 0到10
            x_length=8,                           # x 轴长度
            y_length=6,                           # y 轴长度
        ).shift(DOWN * 0.5)                       # 整体下移一点
        plane.add_coordinates()                   # 添加刻度

        # 绘制函数 y = x²
        graph = plane.plot(                       # plot 画函数曲线
            lambda x: x ** 2,                     # y = x²
            x_range=[0, 3],                       # x 范围 0到3
            color=BLUE,                           # 蓝色曲线
        )

        # 填充曲线下方的面积
        area = plane.get_area(                    # get_area 获取曲线下方的区域
            graph,                                # 要填充的曲线
            x_range=[0, 3],                       # 填充的 x 范围
            color=BLUE,                           # 蓝色填充
            opacity=0.3,                          # 透明度0.3
        )

        # 标注
        formula = MathTex(r"\int_0^3 x^2 \, dx = 9").to_edge(UP)  # 积分公式放在上方

        self.play(Create(plane))                  # 画出坐标平面
        self.play(Create(graph), Write(formula))  # 画曲线和公式
        self.play(FadeIn(area))                   # 淡入面积填充
        self.wait()                               # 暂停1秒


# ===== 4. 曼德博集合（进阶示例）=====
class MandelbrotSet(Scene):                       # 定义曼德博集合场景
    """用图像渲染曼德博集合分形"""                # 类的说明文档

    def construct(self):                          # 场景入口
        # 曼德博集合: 对每个点 c，迭代 z = z² + c，看是否发散
        def mandelbrot(x, y, max_iter=50):        # 定义曼德博计算函数
            c = complex(x, y)                     # 将坐标转为复数
            z = 0                                 # 初始 z = 0
            for i in range(max_iter):             # 迭代最多 max_iter 次
                z = z ** 2 + c                    # 迭代公式: z = z² + c
                if abs(z) > 2:                    # 如果 |z| > 2，说明发散
                    return i / max_iter           # 返回归一化的迭代次数（用于着色）
            return 1.0                            # 没发散返回1（黑色）

        # 生成图像数据
        width, height = 200, 150                  # 图像分辨率
        image_array = np.zeros((height, width, 3), dtype=np.uint8)  # 创建RGB图像数组

        for py in range(height):                  # 遍历每个像素
            for px in range(width):               # 遍历每列
                # 将像素坐标映射到复平面
                x = (px - width * 0.7) / (width * 0.35)  # x 映射到 [-2, 1]
                y = (py - height * 0.5) / (height * 0.5)  # y 映射到 [-1, 1]
                val = mandelbrot(x, y)            # 计算曼德博值
                # 根据值设置颜色
                image_array[py, px] = [           # 设置RGB值
                    int(val * 255 * 0.3),         # R
                    int(val * 255 * 0.7),         # G
                    int(val * 255),               # B
                ]

        # 将数组转为图像对象
        image = ImageMobject(image_array).scale(3)  # ImageMobject 从数组创建图像，放大3倍
        self.add(image)                           # 直接添加图像
        self.wait()                               # 暂停1秒
