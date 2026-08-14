"""练习3: 排序算法可视化

用动画展示冒泡排序的执行过程:
    - 柱状图表示数组
    - 每次比较和交换都有动画
    - 颜色标记当前比较的元素

运行方式:
    manim -pql ex03_sorting.py BubbleSort
"""

from manim import *                               # 导入 manim 库
import numpy as np                                # 导入 numpy 模块


class BubbleSort(Scene):                          # 定义冒泡排序场景
    """冒泡排序可视化动画"""                      # 类的说明文档

    def construct(self):                          # 场景入口
        # === 第1步: 准备数据 ===
        np.random.seed(42)                        # 设置随机种子，保证每次相同
        data = np.random.randint(1, 10, 6).tolist()  # 生成6个随机数(1-9)
        n = len(data)                             # 数据长度

        # 创建柱状图
        title = Text("冒泡排序", font_size=36, color=BLUE).to_edge(UP)  # 标题
        self.play(Write(title))                   # 写出标题

        # 创建柱子（每个数字一个矩形）
        bars = VGroup()                           # 创建空组
        max_val = max(data)                       # 最大值用于归一化高度
        bar_width = 0.8                           # 每根柱子宽度
        bar_gap = 0.2                             # 柱子间距

        for i, val in enumerate(data):            # 遍历每个数据
            height = val / max_val * 3            # 归一化高度（最大3单位）
            bar = Rectangle(                      # Rectangle 矩形
                width=bar_width,                  # 宽度
                height=height,                    # 高度
                fill_opacity=0.7,                 # 填充透明度
                color=BLUE,                       # 蓝色
            )
            # 让柱子底部对齐
            bar.shift(UP * height / 2)            # 将柱子中心移到正确高度

            # 在柱子上方显示数值
            num_label = Text(str(val), font_size=20)  # 创建数值标签
            num_label.next_to(bar, UP, buff=0.1)  # 放在柱子上方

            bar_group = VGroup(bar, num_label)    # 组合柱子和标签
            bars.add(bar_group)                   # 添加到组

        # 排列柱子
        total_width = n * bar_width + (n - 1) * bar_gap  # 计算总宽度
        bars.arrange(RIGHT, buff=bar_gap)         # 水平排列
        bars.shift(DOWN * 0.5)                    # 整体下移

        # 显示初始状态
        self.play(FadeIn(bars))                   # 淡入所有柱子
        self.wait(1)                              # 暂停1秒

        # === 第2步: 执行冒泡排序 ===
        # 创建一个颜色提示器
        compare_text = Text("", font_size=24).to_edge(DOWN)  # 底部状态文字
        self.add(compare_text)                    # 添加状态文字

        for i in range(n - 1):                    # 外层循环: n-1轮
            for j in range(n - 1 - i):            # 内层循环: 每轮比较次数递减
                # 高亮当前比较的两个柱子
                bars[j][0].set_color(YELLOW)      # 第j根变黄
                bars[j + 1][0].set_color(YELLOW)  # 第j+1根变黄
                compare_text.become(Text(         # 更新状态文字
                    f"比较 {data[j]} 和 {data[j+1]}", font_size=24
                ).to_edge(DOWN))                  # 移到底部
                self.wait(0.5)                    # 暂停0.5秒

                if data[j] > data[j + 1]:         # 如果需要交换
                    # 标记为红色表示要交换
                    bars[j][0].set_color(RED)     # 变红
                    bars[j + 1][0].set_color(RED)  # 变红
                    compare_text.become(Text(      # 更新状态
                        f"交换 {data[j]} 和 {data[j+1]}", font_size=24, color=RED
                    ).to_edge(DOWN))              # 移到底部
                    self.wait(0.3)                # 暂停0.3秒

                    # 交换数据
                    data[j], data[j + 1] = data[j + 1], data[j]  # 交换数据值

                    # 动画: 交换两根柱子的位置
                    self.play(                    # 播放交换动画
                        bars[j].animate.move_to(bars[j + 1].get_center()),  # j移到j+1位置
                        bars[j + 1].animate.move_to(bars[j].get_center()),  # j+1移到j位置
                    )
                    # 交换 VGroup 中的引用
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]  # 交换引用

                # 恢复颜色
                bars[j][0].set_color(BLUE)        # 恢复蓝色
                bars[j + 1][0].set_color(BLUE)    # 恢复蓝色

            # 每轮结束后，最大的已就位，标记为绿色
            bars[n - 1 - i][0].set_color(GREEN)   # 已排序的变绿

        # 第一根也是排序好的
        bars[0][0].set_color(GREEN)               # 最后一根变绿
        compare_text.become(Text(                  # 更新状态
            "排序完成!", font_size=28, color=GREEN
        ).to_edge(DOWN))                          # 移到底部
        self.wait(2)                              # 暂停2秒

        # === 第3步: 结束动画 ===
        self.play(                                # 全部淡出
            FadeOut(bars),
            FadeOut(title),
            FadeOut(compare_text),
        )
        self.wait()                               # 暂停1秒
