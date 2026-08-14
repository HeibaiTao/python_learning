"""04 - 动画进阶

学习目标:
    - 掌握常用动画类型与组合
    - 理解动画时长、速率与延迟
    - 了解移动相机和场景变换

运行方式:
    manim -pql 04_animations.py AnimationChain
    manim -pql 04_animations.py MovingCameraDemo
"""

from manim import *                               # 导入 manim 库


# ===== 1. 动画链（顺序播放）=====
class AnimationChain(Scene):                      # 定义动画链场景
    """多个动画依次播放"""                        # 类的说明文档

    def construct(self):                          # 场景入口
        square = Square(color=BLUE, fill_opacity=0.7)  # 创建蓝色正方形

        # 依次播放动画（每个 play 是一个动画步骤）
        self.play(FadeIn(square))                 # 1. 淡入
        self.play(square.animate.shift(2 * RIGHT))  # 2. 右移
        self.play(square.animate.rotate(PI / 2))  # 3. 旋转90度
        self.play(square.animate.scale(1.5))      # 4. 放大1.5倍
        self.play(square.animate.set_color(RED))  # 5. 变红
        self.play(square.animate.shift(2 * UP))   # 6. 上移
        self.play(FadeOut(square))                # 7. 淡出
        self.wait()                               # 暂停1秒


# ===== 2. 同时播放多个动画 =====
class SimultaneousAnimations(Scene):              # 定义并行动画场景
    """多个动画同时播放"""                        # 类的说明文档

    def construct(self):                          # 场景入口
        c1 = Circle(color=BLUE).shift(2 * LEFT)   # 蓝圆在左
        c2 = Circle(color=RED).shift(2 * RIGHT)   # 红圆在右

        # 方式1: 一个 play 里传多个动画（同时开始）
        self.play(Create(c1), Create(c2))         # 两个圆同时画出
        self.wait(0.5)                            # 暂停0.5秒

        # 方式2: 用 lag_ratio 控制动画间隔
        squares = VGroup(*[Square(color=GREEN).scale(0.5) for _ in range(5)])  # 创建5个绿色小方块
        squares.arrange(RIGHT, buff=0.3)          # 水平排列
        self.play(                                # lag_ratio 控制每个动画的启动间隔
            *[FadeIn(s, shift=UP) for s in squares],  # 每个方块从下方淡入
            lag_ratio=0.2,                        # 每个动画比前一个晚0.2倍时长启动
            run_time=2,                           # 总时长2秒
        )
        self.wait()                               # 暂停1秒


# ===== 3. 动画速率与时长 =====
class RateFunctionsDemo(Scene):                   # 定义速率函数场景
    """展示不同的动画速率曲线"""                  # 类的说明文档

    def construct(self):                          # 场景入口
        # rate_func 控制动画的速度变化曲线
        # linear: 匀速
        # smooth: 平滑（默认，开头慢中间快结尾慢）
        # ease_in_quad: 先慢后快
        # ease_out_quad: 先快后慢
        # there_and_back: 去了又回

        configs = [                               # 定义4种速率配置
            ("linear", linear),                   # 匀速
            ("smooth", smooth),                   # 平滑
            ("ease_in", ease_in_quad),            # 加速
            ("ease_out", ease_out_quad),          # 减速
        ]

        for name, func in configs:                # 遍历每种速率
            dot = Dot(color=YELLOW, radius=0.15)  # 创建黄色圆点
            dot.to_edge(LEFT)                     # 移到左侧

            label = Text(name, font_size=24).to_edge(UP)  # 显示速率名称
            arrow = Arrow(LEFT * 5, RIGHT * 5, color=GRAY)  # 灰色轨道箭头

            self.play(Create(arrow), Write(label))  # 画轨道和标签
            self.play(                            # 用指定速率移动圆点
                dot.animate.move_to(RIGHT * 5),   # 从左移到右
                rate_func=func,                   # rate_func 设置速率函数
                run_time=2,                       # 时长2秒
            )
            self.play(FadeOut(dot), FadeOut(label), FadeOut(arrow))  # 清场


# ===== 4. 移动相机 =====
class MovingCameraDemo(MovingCameraScene):        # 继承 MovingCameraScene 而非 Scene
    """相机跟随移动，放大局部细节"""              # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建一个大图
        title = Text("Manim 动画演示", font_size=48).to_edge(UP)  # 标题在上方
        formula = MathTex(r"\int_0^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")  # 积分公式
        formula.set_color(YELLOW)                 # 公式设为黄色

        self.play(Write(title))                   # 写出标题
        self.play(Write(formula))                 # 写出公式
        self.wait(0.5)                            # 暂停0.5秒

        # 相机放大到公式区域
        self.play(self.camera.frame.animate.move_to(formula).set(width=formula.width * 2))  # 相机移到公式并放大
        self.wait()                               # 暂停1秒

        # 相机回到全局视图
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))  # 回到原点，宽度14
        self.wait()                               # 暂停1秒


# ===== 5. 值动画 ValueTracker =====
class ValueTrackerDemo(Scene):                    # 定义值追踪场景
    """用 ValueTracker 做动态变化的动画"""        # 类的说明文档

    def construct(self):                          # 场景入口
        # ValueTracker 是一个可动画变化的数值
        tracker = ValueTracker(0)                 # 初始值为0

        # 创建坐标平面
        plane = NumberPlane(x_range=[-1, 10, 1], y_range=[-1, 6, 1], x_length=8, y_length=5)  # 坐标平面
        plane.add_coordinates()                   # 添加刻度

        # 动态函数：随 tracker 值变化而移动
        dot = always_redraw(lambda: Dot(           # always_redraw 每帧重新创建对象
            plane.c2p(tracker.get_value(), np.sin(tracker.get_value())),  # 位置随tracker变化
            color=RED, radius=0.1,                 # 红色点
        ))

        # 动态文字：显示当前值
        label = always_redraw(lambda: MathTex(    # 动态更新公式
            f"x = {tracker.get_value():.1f}"       # 显示当前x值
        ).to_edge(UP))                            # 放在上方

        self.play(Create(plane), FadeIn(dot), Write(label))  # 画平面、点和标签
        self.wait(0.5)                            # 暂停0.5秒

        # 让 tracker 从0变到 2*PI，点和标签会跟着动
        self.play(tracker.animate.set_value(2 * PI), run_time=4)  # 4秒内从0到2π
        self.wait()                               # 暂停1秒
