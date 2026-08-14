"""练习2: 勾股定理可视化

用动画演示勾股定理: a² + b² = c²
    - 画直角三角形
    - 在三边上画正方形
    - 标注面积
    - 动画演示面积相等

运行方式:
    manim -pql ex02_pythagorean.py PythagoreanTheorem
"""

from manim import *                               # 导入 manim 库
import numpy as np                                # 导入 numpy 模块


class PythagoreanTheorem(Scene):                  # 定义勾股定理场景
    """勾股定理可视化动画"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        # === 第1步: 画直角三角形 ===
        # 定义三角形三个顶点: A(直角), B, C
        A = np.array([0, 0, 0])                   # 直角顶点在原点
        B = np.array([3, 0, 0])                   # B在x轴上，距离3
        C = np.array([0, 4, 0])                   # C在y轴上，距离4

        # 用 Polygon 画三角形
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0.2)  # 三角形，半透明
        triangle.shift(LEFT * 3 + DOWN * 1)      # 左移下移留出空间

        # 标注顶点
        label_a = Text("A", font_size=24).next_to(triangle, DOWN + LEFT, buff=0.1)  # A标注
        label_b = Text("B", font_size=24).next_to(triangle, DOWN + RIGHT, buff=0.1)  # B标注
        label_c = Text("C", font_size=24).next_to(triangle, UP + LEFT, buff=0.1)  # C标注

        # 标注边长
        a_label = MathTex("a=3", font_size=24).next_to(triangle, DOWN, buff=0.2)  # 底边标注
        b_label = MathTex("b=4", font_size=24).next_to(triangle, LEFT, buff=0.2)  # 左边标注
        c_label = MathTex("c=5", font_size=24).next_to(triangle, UP + RIGHT, buff=0.2)  # 斜边标注

        self.play(Create(triangle))               # 画出三角形
        self.play(Write(label_a), Write(label_b), Write(label_c))  # 写出顶点标注
        self.play(Write(a_label), Write(b_label), Write(c_label))  # 写出边长标注
        self.wait(1)                              # 暂停1秒

        # === 第2步: 在三边上画正方形 ===
        # 底边正方形 a²=9
        sq_a = Square(side_length=3, color=BLUE, fill_opacity=0.3)  # 蓝色正方形
        sq_a.next_to(triangle, DOWN, buff=0)      # 放在三角形下方

        # 左边正方形 b²=16
        sq_b = Square(side_length=4, color=GREEN, fill_opacity=0.3)  # 绿色正方形
        sq_b.next_to(triangle, LEFT, buff=0)      # 放在三角形左侧

        # 标注面积
        area_a = MathTex("a^2=9", font_size=24, color=BLUE).move_to(sq_a.get_center())  # a²=9
        area_b = MathTex("b^2=16", font_size=24, color=GREEN).move_to(sq_b.get_center())  # b²=16

        self.play(Create(sq_a), Write(area_a))    # 画底边正方形
        self.play(Create(sq_b), Write(area_b))    # 画左边正方形
        self.wait(1)                              # 暂停1秒

        # === 第3步: 公式推导 ===
        formula_title = Text("勾股定理", font_size=36, color=YELLOW)  # 标题
        formula_title.to_edge(UP, buff=0.5)       # 移到顶部
        self.play(Write(formula_title))           # 写出标题

        # 公式逐步推导
        step1 = MathTex(r"a^2 + b^2 = c^2")       # 基本公式
        step1.next_to(formula_title, DOWN, buff=0.5)  # 放在标题下方
        self.play(Write(step1))                   # 写出公式
        self.wait(0.5)                            # 暂停0.5秒

        step2 = MathTex(r"3^2 + 4^2 = c^2")        # 代入数值
        step2.next_to(step1, DOWN, buff=0.5)      # 放在step1下方
        self.play(TransformMatchingTex(step1.copy(), step2))  # 变换动画
        self.wait(0.5)                            # 暂停0.5秒

        step3 = MathTex(r"9 + 16 = c^2")           # 计算平方
        step3.next_to(step2, DOWN, buff=0.5)      # 放在step2下方
        self.play(TransformMatchingTex(step2.copy(), step3))  # 变换动画
        self.wait(0.5)                            # 暂停0.5秒

        step4 = MathTex(r"25 = c^2", color=GREEN)  # 求和
        step4.next_to(step3, DOWN, buff=0.5)      # 放在step3下方
        self.play(TransformMatchingTex(step3.copy(), step4))  # 变换动画
        self.wait(0.5)                            # 暂停0.5秒

        step5 = MathTex(r"c = 5", color=RED)       # 最终结果
        step5.next_to(step4, DOWN, buff=0.5)      # 放在step4下方
        step5.scale(1.5)                          # 放大1.5倍强调
        self.play(TransformMatchingTex(step4.copy(), step5))  # 变换动画
        self.wait(2)                              # 暂停2秒

        # === 第4步: 整体淡出 ===
        all_objects = VGroup(                     # 创建包含所有对象的组
            triangle, label_a, label_b, label_c,  # 三角形和标注
            a_label, b_label, c_label,            # 边长标注
            sq_a, area_a, sq_b, area_b,            # 正方形
            formula_title, step1, step2, step3, step4, step5,  # 公式
        )
        self.play(FadeOut(all_objects))           # 全部淡出
        self.wait()                               # 暂停1秒
