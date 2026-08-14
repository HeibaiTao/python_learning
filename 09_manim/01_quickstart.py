"""01 - Manim 快速入门

学习目标:
    - 理解 Scene / Mobject / Animation 三个核心概念
    - 掌握基本图形创建与动画播放
    - 了解 .animate 语法

运行方式（在终端中执行）:
    manim -pql 01_quickstart.py CreateCircle       # 低质量预览
    manim -pqh 01_quickstart.py CreateCircle       # 高质量渲染
    manim -pql 01_quickstart.py SquareToCircle      # 渲染指定 Scene

参数说明:
    -p  渲染完成后自动播放
    -ql 低质量（快速预览）
    -qh 高质量（最终输出）
    -qm 中等质量
"""

from manim import *                               # 导入 manim 库的所有内容（官方推荐写法）


# ===== 1. 创建一个圆形 =====
class CreateCircle(Scene):                        # 每个 Scene 类就是一个动画场景
    """画一个粉色圆形"""                          # 类的说明文档

    def construct(self):                          # construct 是场景的入口方法，所有动画写在这里
        circle = Circle()                         # 创建一个圆形 Mobject（数学对象）
        circle.set_fill(PINK, opacity=0.5)        # 设置填充颜色为粉色，透明度0.5（半透明）
        self.play(Create(circle))                 # play 播放动画：Create 动画会"画出"圆形
        self.wait()                               # wait 暂停1秒（让画面停留一下）


# ===== 2. 正方形变圆形 =====
class SquareToCircle(Scene):                      # 定义第二个场景
    """正方形变换为圆形"""                        # 类的说明文档

    def construct(self):                          # 场景入口
        circle = Circle()                         # 先创建一个圆形（目标形状）
        circle.set_fill(PINK, opacity=0.5)        # 设置圆形颜色和透明度

        square = Square()                         # 创建一个正方形（起始形状）
        square.rotate(PI / 4)                     # 旋转45度（PI/4 弧度 = 45度）

        self.play(Create(square))                 # 动画1：画出正方形
        self.play(Transform(square, circle))      # 动画2：将正方形变形为圆形（Transform 变换动画）
        self.play(FadeOut(square))                # 动画3：让正方形（已变圆形）淡出消失


# ===== 3. 定位多个对象 =====
class Positioning(Scene):                         # 定义第三个场景
    """定位和排列多个图形"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        circle = Circle(radius=1.0, color=BLUE)   # 创建蓝色圆形，半径1.0
        square = Square(side_length=1.5, color=GREEN)  # 创建绿色正方形，边长1.5
        triangle = Triangle(color=RED)            # 创建红色三角形

        # next_to 将对象放在另一个对象的旁边
        circle.to_edge(LEFT, buff=0.5)            # 圆形移到屏幕左侧，buff 是与边缘的距离
        triangle.to_edge(RIGHT, buff=0.5)         # 三角形移到屏幕右侧

        # 用 Group 组合多个对象
        shapes = VGroup(circle, square, triangle)  # VGroup 是可变对象组，把三个图形组合
        shapes.arrange(buff=1.0)                  # arrange 自动排列组内对象，buff 是间距
        shapes.move_to(ORIGIN)                    # move_to 将整组移到原点（屏幕中心）

        self.play(Write(shapes))                  # Write 动画：像写字一样逐个显现
        self.wait()                               # 暂停1秒


# ===== 4. .animate 语法（核心特性）=====
class AnimateSyntax(Scene):                       # 定义第四个场景
    """演示 .animate 动画语法"""                  # 类的说明文档

    def construct(self):                          # 场景入口
        square = Square(color=BLUE, fill_opacity=0.5)  # 创建蓝色半透明正方形

        # .animate 可以把对象的"修改操作"变成动画
        # 语法: 对象.animate.方法(参数)
        self.play(square.animate.rotate(PI / 4))  # 旋转动画：旋转45度
        self.play(square.animate.scale(2))        # 放大动画：放大到2倍
        self.play(square.animate.set_fill(RED, opacity=0.8))  # 变色动画：变红
        self.play(square.animate.shift(2 * RIGHT))  # 移动动画：向右移动2个单位
        self.play(square.animate.shift(2 * UP))   # 向上移动2个单位

        # 可以一条 play 同时执行多个动画
        self.play(                                # 同时执行多个动画
            square.animate.rotate(-PI / 4),       # 逆时针旋转45度
            square.animate.scale(0.5),            # 缩小到一半
            run_time=2,                           # run_time 设置动画时长（秒）
        )
        self.wait()                               # 暂停1秒


# ===== 5. 多种动画类型 =====
class AnimationTypes(Scene):                      # 定义第五个场景
    """展示常用动画类型"""                        # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建4个不同颜色的圆
        c1 = Circle(color=BLUE, fill_opacity=0.8).shift(3 * LEFT)   # 蓝圆在左
        c2 = Circle(color=GREEN, fill_opacity=0.8).shift(LEFT)      # 绿圆
        c3 = Circle(color=YELLOW, fill_opacity=0.8).shift(RIGHT)    # 黄圆
        c4 = Circle(color=RED, fill_opacity=0.8).shift(3 * RIGHT)   # 红圆在右

        # Create: 逐步画出
        self.play(Create(c1))                     # Create 从无到有"画出"形状
        self.wait(0.5)                            # 暂停0.5秒

        # Write: 像写字一样显现
        self.play(Write(c2))                      # Write 从左到右"写出来"
        self.wait(0.5)                            # 暂停0.5秒

        # FadeIn: 淡入
        self.play(FadeIn(c3))                     # FadeIn 从透明渐变为不透明
        self.wait(0.5)                            # 暂停0.5秒

        # GrowFromCenter: 从中心放大
        self.play(GrowFromCenter(c4))             # GrowFromCenter 从中心点逐渐放大
        self.wait(0.5)                            # 暂停0.5秒

        # 消失动画
        self.play(FadeOut(c1))                    # FadeOut 淡出消失
        self.play(ShrinkToCenter(c2))             # ShrinkToCenter 缩小到中心消失
        self.play(Unwrite(c3))                    # Unwrite 反向擦除
        self.play(c4.animate.scale(0))            # scale(0) 缩到0也相当于消失
        self.wait()                               # 暂停1秒


# ===== 6. 文字与排列 =====
class TextAndArrangement(Scene):                  # 定义第六个场景
    """文字显示与自动排列"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建文字对象
        title = Text("Manim 动画入门", font_size=48, color=BLUE)  # 创建标题文字
        subtitle = Text("从零开始学动画", font_size=28, color=YELLOW)  # 创建副标题

        # 用 VGroup 组合并排列
        group = VGroup(title, subtitle)           # 组合标题和副标题
        group.arrange(DOWN, buff=0.5)             # 竖向排列（DOWN = 从上到下），间距0.5

        self.play(Write(title))                   # 写出标题
        self.play(FadeIn(subtitle, shift=UP))     # 副标题从下方淡入
        self.wait()                               # 暂停1秒

        # 让整组移到屏幕上方
        self.play(group.animate.to_edge(UP))      # 移到屏幕顶部
        self.wait()                               # 暂停1秒
