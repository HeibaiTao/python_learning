"""05 - 高级场景

学习目标:
    - 掌握 3D 场景基础
    - 了解图形布尔运算
    - 理解更新动画（Update）

运行方式:
    manim -pql 05_advanced_scene.py ThreeDDemo
    manim -pql 05_advanced_scene.py BooleanOps
    manim -pql 05_advanced_scene.py UpdateAnimation
"""

from manim import *                               # 导入 manim 库
import numpy as np                                # 导入 numpy 模块


# ===== 1. 3D 场景基础 =====
class ThreeDDemo(ThreeDScene):                    # 继承 ThreeDScene 而非 Scene
    """3D 场景基础演示"""                         # 类的说明文档

    def construct(self):                          # 场景入口
        # 设置相机视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)  # phi倾斜角, theta方位角

        # 创建 3D 坐标轴
        axes = ThreeDAxes(                        # ThreeDAxes 创建3D坐标轴
            x_range=[-3, 3, 1],                   # x 轴范围
            y_range=[-3, 3, 1],                   # y 轴范围
            z_range=[-3, 3, 1],                   # z 轴范围
            x_length=6,                           # x 轴长度
            y_length=6,                           # y 轴长度
            z_length=6,                           # z 轴长度
        )

        # 创建 3D 曲面: z = sin(x)*cos(y)
        surface = Surface(                        # Surface 创建3D曲面
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),  # 参数方程
            u_range=[-PI, PI],                    # u 参数范围
            v_range=[-PI, PI],                    # v 参数范围
            resolution=30,                        # 网格分辨率（越大越精细）
        )
        surface.set_color_by_gradient(BLUE, GREEN, YELLOW)  # 渐变色填充

        # 添加坐标轴和曲面
        self.add(axes)                            # 直接添加坐标轴（不需要动画）
        self.play(Create(surface), run_time=3)    # 用3秒画出曲面

        # 旋转相机
        self.begin_ambient_camera_rotation(rate=0.15)  # 开始自动旋转相机
        self.wait(5)                              # 旋转5秒
        self.stop_ambient_camera_rotation()       # 停止旋转

        # 俯视视角
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.5)  # 切换到俯视
        self.wait()                               # 暂停1秒


# ===== 2. 图形布尔运算 =====
class BooleanOps(Scene):                          # 定义布尔运算场景（基于官方示例）
    """图形的交/并/差运算"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建两个椭圆
        ellipse1 = Ellipse(                       # 创建第一个椭圆
            width=4.0, height=5.0,                # 宽4高5
            fill_opacity=0.5, color=BLUE,         # 半透明蓝色
            stroke_width=10,                      # 边框宽度
        ).move_to(LEFT)                           # 移到左侧

        ellipse2 = ellipse1.copy().set_color(RED).move_to(RIGHT)  # 复制并改为红色，移到右侧

        # 标题
        title = MarkupText("<u>布尔运算</u>").next_to(ellipse1, UP * 3)  # 带下划线的标题
        group = Group(title, ellipse1, ellipse2).move_to(LEFT * 3)  # 组合并左移
        self.play(FadeIn(group))                  # 淡入

        # 交集 Intersection
        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)  # 两个椭圆的重叠部分
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))  # 缩小并移到右上
        i_text = Text("交集", font_size=23).next_to(i, UP)  # 标注"交集"
        self.play(FadeIn(i_text))                 # 淡入标注

        # 并集 Union
        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)  # 两个椭圆的合并
        u_text = Text("并集", font_size=23)       # 标注
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=u_text.height * 3))  # 缩小移到下方
        u_text.next_to(u, UP)                     # 标注放在上方
        self.play(FadeIn(u_text))                 # 淡入标注

        # 差集 Difference
        d = Difference(ellipse1, ellipse2, color=PURPLE, fill_opacity=0.5)  # 椭圆1减去椭圆2
        d_text = Text("差集", font_size=23)       # 标注
        self.play(d.animate.scale(0.3).next_to(i, RIGHT, buff=u_text.height * 3))  # 缩小移到右侧
        d_text.next_to(d, UP)                     # 标注放在上方
        self.play(FadeIn(d_text))                 # 淡入标注
        self.wait()                               # 暂停1秒


# ===== 3. 更新动画（Updaters）=====
class UpdateAnimation(Scene):                     # 定义更新动画场景
    """用 updater 让对象随时间变化"""             # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建一个正方形
        square = Square(color=BLUE, fill_opacity=0.7)  # 蓝色半透明正方形

        # 方式1: 用 add_updater 添加更新函数
        def rotate_and_color(mob, dt):            # mob 是被更新的对象, dt 是时间步长
            mob.rotate(0.5 * dt)                  # 每帧旋转（dt 自动传入）
            # 根据旋转角度改变颜色
            angle = mob.angle % (2 * PI)          # 获取当前角度（取模）
            ratio = angle / (2 * PI)              # 转为 0-1 比例
            mob.set_color(interpolate_color(BLUE, RED, ratio))  # 在蓝红之间插值

        square.add_updater(rotate_and_color)      # add_updater 注册更新函数
        self.add(square)                          # add 直接添加到场景（不用 play）
        self.wait(4)                              # 等待4秒，updater 会自动运行
        square.remove_updater(rotate_and_color)   # remove_updater 移除更新函数
        self.wait()                               # 暂停1秒


# ===== 4. 路径动画 =====
class PathAnimation(Scene):                       # 定义路径动画场景
    """让对象沿路径移动"""                        # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建一条曲线路径
        path = ParametricFunction(                # ParametricFunction 创建参数曲线
            lambda t: np.array([                   # 参数方程
                np.sin(2 * t),                    # x = sin(2t)
                np.sin(3 * t),                    # y = sin(3t)
                0,                                # z = 0（2D）
            ]),
            t_range=[0, TAU],                     # 参数范围 0 到 2π
            color=YELLOW,                         # 黄色路径
        )
        path.set_stroke(width=3)                  # 线宽3

        # 创建移动的点
        dot = Dot(color=RED, radius=0.1)          # 红色小点

        # 让点沿路径移动（MoveAlongPath）
        self.play(Create(path))                   # 先画出路径
        self.play(MoveAlongPath(dot, path, run_time=4))  # 点沿路径移动4秒
        self.wait()                               # 暂停1秒
