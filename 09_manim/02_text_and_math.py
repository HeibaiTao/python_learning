"""02 - 文本与数学公式

学习目标:
    - 掌握 Text / MarkupText 的使用
    - 理解 MathTex 和 LaTeX 数学公式渲染
    - 了解文字动画效果

运行方式:
    manim -pql 02_text_and_math.py TextBasics
    manim -pql 02_text_and_math.py MathFormula
"""

from manim import *                               # 导入 manim 库


# ===== 1. 基础文字 =====
class TextBasics(Scene):                          # 定义文字基础场景
    """展示 Text 对象的基本用法"""                # 类的说明文档

    def construct(self):                          # 场景入口
        # Text 用于显示普通文字
        t1 = Text("Hello, Manim!", font_size=48)  # 创建文字，font_size 设置字号
        t1.to_edge(UP)                            # 移到屏幕上方
        self.play(Write(t1))                      # Write 动画写出文字
        self.wait(0.5)                            # 暂停0.5秒

        # 设置颜色
        t2 = Text("彩色文字", font_size=36, color=BLUE)  # 蓝色文字
        t2.next_to(t1, DOWN, buff=0.5)            # next_to 放在 t1 下方，间距0.5
        self.play(FadeIn(t2))                     # 淡入
        self.wait(0.5)                            # 暂停0.5秒

        # 逐字设置颜色（t2[0] 取第一个字符）
        t3 = Text("红绿蓝", font_size=48)         # 创建三色文字
        t3[0].set_color(RED)                      # 第一个字"红"设为红色
        t3[1].set_color(GREEN)                    # 第二个字"绿"设为绿色
        t3[2].set_color(BLUE)                     # 第三个字"蓝"设为蓝色
        t3.next_to(t2, DOWN, buff=0.5)            # 放在 t2 下方
        self.play(Write(t3))                      # 写出三色文字
        self.wait()                               # 暂停1秒

        # 淡出所有文字
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3))  # 同时淡出三个文字


# ===== 2. 富文本标记 MarkupText =====
class MarkupTextDemo(Scene):                      # 定义富文本场景
    """用 MarkupText 实现富文本格式"""            # 类的说明文档

    def construct(self):                          # 场景入口
        # MarkupText 支持 Pango 标记语言，类似 HTML
        text = MarkupText(                        # 创建富文本
            '<b>粗体</b> '                        # <b> 粗体
            '<i>斜体</i> '                        # <i> 斜体
            '<u>下划线</u> '                      # <u> 下划线
            '<span foreground="red">红色</span> '  # span 设置颜色
            '<span size="20">小字</span>',         # span 设置字号
            font_size=36,                         # 默认字号
        )
        self.play(Write(text))                    # 写出富文本
        self.wait()                               # 暂停1秒


# ===== 3. 数学公式 MathTex =====
class MathFormula(Scene):                         # 定义数学公式场景
    """用 MathTex 渲染 LaTeX 数学公式"""          # 类的说明文档

    def construct(self):                          # 场景入口
        # MathTex 使用 LaTeX 语法渲染数学公式
        formula1 = MathTex(r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}")  # 求和公式
        formula1.to_edge(UP)                      # 移到上方
        self.play(Write(formula1))                # 写出公式
        self.wait(0.5)                            # 暂停0.5秒

        # 勾股定理
        formula2 = MathTex(r"a^2 + b^2 = c^2")    # 勾股定理
        formula2.next_to(formula1, DOWN, buff=1)  # 放在公式1下方
        self.play(Write(formula2))                # 写出公式
        self.wait(0.5)                            # 暂停0.5秒

        # 欧拉公式
        formula3 = MathTex(r"e^{i\pi} + 1 = 0")   # 欧拉公式（最美公式）
        formula3.next_to(formula2, DOWN, buff=1)  # 放在公式2下方
        formula3.set_color(YELLOW)                # 设为黄色
        self.play(Write(formula3))                # 写出公式
        self.wait()                               # 暂停1秒


# ===== 4. 公式变换动画 =====
class FormulaTransform(Scene):                    # 定义公式变换场景
    """数学公式的逐步推导动画"""                  # 类的说明文档

    def construct(self):                          # 场景入口
        # 步骤1: 原始公式
        step1 = MathTex(r"\frac{1}{2} + \frac{1}{3}")  # 1/2 + 1/3
        step1.to_edge(UP)                         # 移到上方
        self.play(Write(step1))                   # 写出第一步
        self.wait(0.5)                            # 暂停0.5秒

        # 步骤2: 通分
        step2 = MathTex(r"\frac{3}{6} + \frac{2}{6}")  # 3/6 + 2/6
        step2.next_to(step1, DOWN, buff=0.8)      # 放在step1下方
        self.play(TransformMatchingTex(step1.copy(), step2))  # 变换动画（匹配公式部分）
        self.wait(0.5)                            # 暂停0.5秒

        # 步骤3: 合并
        step3 = MathTex(r"\frac{5}{6}")           # 5/6
        step3.next_to(step2, DOWN, buff=0.8)      # 放在step2下方
        step3.set_color(GREEN)                    # 设为绿色表示结果
        self.play(TransformMatchingTex(step2.copy(), step3))  # 变换动画
        self.wait()                               # 暂停1秒


# ===== 5. 文字与公式混排 =====
class TextAndMath(Scene):                         # 定义文字与公式混合场景
    """文字和数学公式混合显示"""                  # 类的说明文档

    def construct(self):                          # 场景入口
        # 创建文字和公式
        text = Text("勾股定理：", font_size=36, color=BLUE)  # 创建文字
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=48)  # 创建公式

        # 横向排列
        group = VGroup(text, formula)             # 组合文字和公式
        group.arrange(RIGHT, buff=0.3)            # 横向排列，间距0.3

        self.play(Write(text))                    # 先写出文字
        self.play(Write(formula))                 # 再写出公式
        self.wait()                               # 暂停1秒

        # 给公式加框
        box = SurroundingRectangle(formula, color=YELLOW, buff=0.2)  # 创建环绕矩形框
        self.play(Create(box))                    # 画出框
        self.wait()                               # 暂停1秒
