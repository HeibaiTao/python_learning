"""练习1: 自我介绍动画

制作一个自我介绍动画，综合运用:
    - 文字动画
    - 图形排列
    - 淡入淡出
    - 颜色变化

运行方式:
    manim -pql ex01_intro.py MyIntro
"""

from manim import *                               # 导入 manim 库


class MyIntro(Scene):                             # 定义自我介绍场景
    """自我介绍动画"""                            # 类的说明文档

    def construct(self):                          # 场景入口
        # === 第1步: 标题淡入 ===
        title = Text("Hello, Manim!", font_size=56, color=BLUE)  # 创建标题
        title.to_edge(UP, buff=1)                 # 移到上方
        self.play(Write(title))                   # 写出标题
        self.wait(0.5)                            # 暂停0.5秒

        # === 第2步: 副标题从下方滑入 ===
        subtitle = Text("我的第一个动画作品", font_size=32, color=YELLOW)  # 副标题
        subtitle.next_to(title, DOWN, buff=0.5)   # 放在标题下方
        self.play(FadeIn(subtitle, shift=UP * 0.5))  # 从下方淡入
        self.wait(0.5)                            # 暂停0.5秒

        # === 第3步: 三个特性卡片依次出现 ===
        features = [                              # 定义三个特性
            ("简单易学", GREEN),                   # 特性1
            ("效果精美", BLUE),                    # 特性2
            ("代码驱动", RED),                     # 特性3
        ]

        cards = VGroup()                          # 创建空组用于存放卡片
        for text_str, color in features:          # 遍历特性
            card = RoundedRectangle(              # RoundedRectangle 圆角矩形
                width=3, height=1.5,              # 宽3高1.5
                corner_radius=0.2,                # 圆角半径0.2
                fill_opacity=0.3,                 # 填充透明度
                stroke_color=color,               # 边框颜色
            )
            label = Text(text_str, font_size=24, color=color)  # 卡片文字
            label.move_to(card.get_center())      # 文字放在卡片中心
            card_group = VGroup(card, label)      # 组合卡片和文字
            cards.add(card_group)                 # 添加到组

        cards.arrange(RIGHT, buff=0.5)            # 三个卡片水平排列，间距0.5
        cards.shift(DOWN * 0.5)                   # 整体下移

        # 依次淡入每个卡片（用 lag_ratio 制造依次出现效果）
        self.play(                                # 播放动画
            *[FadeIn(card, shift=UP) for card in cards],  # 每个卡片从下方淡入
            lag_ratio=0.3,                        # 每个卡片比前一个晚0.3倍时长
            run_time=2,                           # 总时长2秒
        )
        self.wait(0.5)                            # 暂停0.5秒

        # === 第4步: 卡片依次变色 ===
        for card in cards:                        # 遍历每个卡片
            self.play(card.animate.scale(1.1), run_time=0.3)  # 放大
            self.play(card.animate.scale(1.0), run_time=0.3)  # 缩回（弹跳效果）
        self.wait(0.5)                            # 暂停0.5秒

        # === 第5步: 整体淡出 ===
        self.play(                                # 同时淡出所有元素
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(cards),
        )

        # === 第6步: 结束语 ===
        bye = Text("谢谢观看!", font_size=48, color=GREEN)  # 结束语
        self.play(Write(bye))                     # 写出结束语
        self.play(bye.animate.scale(1.2))         # 放大一下
        self.wait()                               # 暂停1秒
