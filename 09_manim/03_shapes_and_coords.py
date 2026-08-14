"""03 - 图形与坐标系

学习目标:
    - 掌握基本图形（圆/方/三角/线条/箭头）
    - 理解 NumberPlane 坐标系
    - 了解函数图像绘制

运行方式:
    manim -pql 03_shapes_and_coords.py ShapesDemo
    manim -pql 03_shapes_and_coords.py FunctionGraph
"""

from manim import *                               # 导入 manim 库


# ===== 1. 基本图形 =====
class ShapesDemo(Scene):                          # 定义图形展示场景
    """展示 Manim 中的基本图形"""                 # 类的说明文档

    def construct(self):                          # 场景入口
        # 圆形
        circle = Circle(radius=1.0, color=BLUE, fill_opacity=0.5)  # 蓝色半透明圆
        circle.shift(3 * LEFT)                    # 移到左侧

        # 正方形
        square = Square(side_length=1.5, color=GREEN, fill_opacity=0.5)  # 绿色半透明方
        square.shift(LEFT)                        # 移到偏左

        # 三角形
        triangle = Triangle(color=RED, fill_opacity=0.5)  # 红色半透明三角
        triangle.shift(RIGHT)                     # 移到偏右

        # 椭圆
        ellipse = Ellipse(width=2.0, height=1.0, color=YELLOW, fill_opacity=0.5)  # 黄色椭圆
        ellipse.shift(3 * RIGHT)                  # 移到右侧

        # 一次性创建所有图形
        self.play(                                # 同时播放多个创建动画
            Create(circle),
            Create(square),
            Create(triangle),
            Create(ellipse),
            run_time=2,                           # 动画时长2秒
        )
        self.wait()                               # 暂停1秒


# ===== 2. 线条与箭头 =====
class LinesAndArrows(Scene):                      # 定义线条箭头场景
    """展示线条、箭头和点"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        # 点（Dot）
        dot1 = Dot(LEFT * 3 + UP, color=RED, radius=0.1)   # 红色点在左上
        dot2 = Dot(RIGHT * 3 + DOWN, color=BLUE, radius=0.1)  # 蓝色点在右下

        # 线条（Line）
        line = Line(dot1.get_center(), dot2.get_center(), color=YELLOW)  # 连接两点的线
        line.set_stroke(width=4)                  # 设置线宽为4

        # 箭头（Arrow）
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0, color=GREEN)  # 从原点到(2,2)的箭头

        # 双箭头（DoubleArrow）
        darrow = DoubleArrow(LEFT * 3, RIGHT * 3, color=PINK)  # 水平双箭头

        # 标注文字
        label = Text("对角线", font_size=24).next_to(line, UP, buff=0.2)  # 线条上方标注

        self.play(FadeIn(dot1), FadeIn(dot2))     # 淡入两个点
        self.play(Create(line))                   # 画出线条
        self.play(Write(label))                   # 写出标注
        self.play(GrowArrow(arrow))               # 长出箭头
        self.play(GrowArrow(darrow))              # 长出双箭头
        self.wait()                               # 暂停1秒


# ===== 3. 坐标系 NumberPlane =====
class CoordinateSystem(Scene):                    # 定义坐标系场景
    """展示 NumberPlane 坐标系"""                 # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建坐标平面
        plane = NumberPlane(                      # NumberPlane 创建带网格的坐标平面
            x_range=[-4, 4, 1],                   # x 轴范围 -4到4，刻度间隔1
            y_range=[-3, 3, 1],                   # y 轴范围 -3到3，刻度间隔1
            x_length=8,                           # x 轴显示长度
            y_length=6,                           # y 轴显示长度
        )
        plane.add_coordinates()                   # 添加坐标刻度数字

        # 标记原点和特定点
        origin_dot = Dot(ORIGIN, color=RED, radius=0.08)  # 原点红点
        point_dot = Dot([2, 1, 0], color=YELLOW, radius=0.08)  # 点(2,1)黄点

        # 标注
        origin_label = Text("(0,0)", font_size=20).next_to(origin_dot, DOWN + LEFT, buff=0.1)  # 原点标注
        point_label = Text("(2,1)", font_size=20).next_to(point_dot, UP + RIGHT, buff=0.1)  # 点标注

        self.play(Create(plane))                  # 画出坐标平面
        self.play(FadeIn(origin_dot), Write(origin_label))  # 显示原点
        self.play(FadeIn(point_dot), Write(point_label))    # 显示特定点
        self.wait()                               # 暂停1秒


# ===== 4. 函数图像 =====
class FunctionGraph(Scene):                       # 定义函数图像场景
    """在坐标系上绘制函数图像"""                  # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建坐标平面
        plane = NumberPlane(                      # 创建坐标平面
            x_range=[-3, 3, 1],                   # x 轴范围
            y_range=[-5, 5, 1],                   # y 轴范围
            x_length=7,                           # x 轴长度
            y_length=7,                           # y 轴长度
        )
        plane.add_coordinates()                   # 添加坐标刻度

        # 绘制 sin(x) 函数图像
        sin_graph = plane.plot(                   # plot 在坐标平面上画函数
            lambda x: np.sin(x),                  # lambda 定义函数: y = sin(x)
            x_range=[-3, 3],                      # x 的取值范围
            color=BLUE,                           # 线条颜色
        )
        sin_label = MathTex(r"y = \sin(x)").next_to(sin_graph, UP, buff=0.2)  # 公式标签

        # 绘制 x² 函数图像
        parabola = plane.plot(                    # 画抛物线
            lambda x: x ** 2,                     # 函数: y = x²
            x_range=[-2, 2],                      # x 的取值范围
            color=RED,                            # 红色
        )
        parabola_label = MathTex(r"y = x^2").next_to(parabola, UP, buff=0.2)  # 公式标签

        self.play(Create(plane))                  # 画出坐标平面
        self.play(Create(sin_graph), Write(sin_label))  # 画sin曲线
        self.wait(0.5)                            # 暂停0.5秒
        self.play(Create(parabola), Write(parabola_label))  # 画抛物线
        self.wait()                               # 暂停1秒


# ===== 5. 图形标注 =====
class BraceAnnotation(Scene):                     # 定义标注场景（基于官方示例）
    """用 Brace（大括号）标注图形"""              # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建两个点和连线
        dot = Dot([-2, -1, 0])                    # 左下方的点
        dot2 = Dot([2, 1, 0])                     # 右上方的点
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)  # 橙色连线

        # 用大括号标注水平距离
        b1 = Brace(line)                          # Brace 创建大括号标注
        b1text = b1.get_text("水平距离")          # get_text 获取标注文字

        # 垂直方向的大括号
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())  # 旋转90度的大括号
        b2text = b2.get_tex("x-x_1")              # get_tex 获取 LaTeX 标注

        self.play(Create(line), FadeIn(dot), FadeIn(dot2))  # 画线和点
        self.play(GrowFromCenter(b1), Write(b1text))  # 长出第一个大括号
        self.play(GrowFromCenter(b2), Write(b2text))  # 长出第二个大括号
        self.wait()                               # 暂停1秒
