"""项目 6:2048 小游戏

功能:
    - 经典 2048 玩法:方向键移动,相同数字合并
    - 随机生成 2 或 4
    - 计分、最高分(保存到文件)
    - 游戏结束判断
    - 撤销上一步

操作:
    w/↑ 上移   s/↓ 下移
    a/← 左移   d/→ 右移
    u   撤销   q   退出

用法:
    python game_2048.py
"""

import random                        # 导入随机数模块,用于随机生成数字和位置
import copy                          # 导入拷贝模块,用于深拷贝棋盘(撤销功能需要)
import os                            # 导入操作系统模块,用于清屏等系统调用
import sys                           # 导入系统模块,用于标准输入输出
from pathlib import Path             # 从 pathlib 导入 Path 类,用于跨平台路径操作


SCORE_FILE = Path(__file__).parent / "best_score.txt"   # 最高分保存文件路径(与本脚本同目录)


class Game2048:                      # 2048 游戏主类
    def __init__(self, size=4):      # 初始化方法,size 为棋盘边长,默认 4
        self.size = size             # 保存棋盘大小
        self.board = [[0] * size for _ in range(size)]   # 创建 size×size 的二维列表,初始全为 0
        self.score = 0               # 当前得分初始化为 0
        self.best_score = self._load_best()   # 从文件加载历史最高分
        self.history = []   # 历史记录列表,用于撤销操作

        self._add_random()           # 开局随机添加第一个数字
        self._add_random()           # 开局随机添加第二个数字

    # ===== 最高分持久化 =====
    def _load_best(self) -> int:     # 加载历史最高分的方法
        if SCORE_FILE.exists():      # 如果最高分文件存在
            try:                     # 尝试读取并转换
                return int(SCORE_FILE.read_text().strip())   # 读取文件内容并转为整数
            except (ValueError, OSError):   # 如果内容不是数字或读取失败
                return 0             # 返回 0
        return 0                     # 文件不存在时返回 0

    def _save_best(self):            # 保存最高分到文件的方法
        if self.score > self.best_score:   # 如果当前分数超过最高分
            self.best_score = self.score   # 更新最高分
            try:                     # 尝试写入文件
                SCORE_FILE.write_text(str(self.best_score))   # 把最高分写入文件
            except OSError:          # 如果写入失败
                pass                 # 忽略错误,不影响游戏

    # ===== 棋盘操作 =====
    def _empty_cells(self):          # 获取所有空格位置的方法
        return [(i, j) for i in range(self.size)   # 返回坐标列表,遍历行
                for j in range(self.size) if self.board[i][j] == 0]   # 遍历列,筛选值为 0 的格子

    def _add_random(self):           # 在随机空格添加数字的方法
        empties = self._empty_cells()   # 获取所有空格坐标
        if not empties:              # 如果没有空格
            return False             # 返回 False,表示添加失败
        i, j = random.choice(empties)   # 随机选一个空格
        self.board[i][j] = 4 if random.random() < 0.1 else 2   # 10% 概率放 4,否则放 2
        return True                  # 返回 True,表示添加成功

    def _compress_row(self, row):    # 向左压缩合并一行的方法
        """向左压缩合并一行,返回(新行, 本次得分)"""
        # 去掉零
        nums = [n for n in row if n != 0]   # 过滤掉行中的 0,只保留有效数字
        merged = []                  # 存放合并后的数字列表
        score = 0                    # 本次合并得分
        i = 0                        # 索引指针,从 0 开始
        while i < len(nums):         # 遍历数字列表
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:   # 如果当前和下一个数字相同
                val = nums[i] * 2    # 合并后的值(翻倍)
                merged.append(val)   # 把合并值加入结果
                score += val         # 累加得分
                i += 2               # 跳过下一个(已被合并)
            else:                    # 否则不能合并
                merged.append(nums[i])   # 直接把当前数字加入结果
                i += 1               # 指针后移一位
        # 补零到原长
        merged += [0] * (len(row) - len(merged))   # 末尾补 0,保持行长不变
        return merged, score         # 返回新行和本次得分

    def _move_left(self) -> tuple[bool, int]:   # 整个棋盘向左移动的方法
        moved = False                # 是否发生移动的标志
        gained = 0                   # 本次得分
        new_board = []               # 存放移动后的新棋盘
        for row in self.board:       # 遍历棋盘每一行
            new_row, score = self._compress_row(row)   # 对该行进行压缩合并
            if new_row != row:       # 如果该行发生了变化
                moved = True         # 标记发生了移动
            gained += score          # 累加得分
            new_board.append(new_row)   # 把新行加入新棋盘
        self.board = new_board       # 用新棋盘替换旧棋盘
        return moved, gained         # 返回是否移动和本次得分

    def move(self, direction: str) -> bool:   # 移动方法,direction 为方向
        """
        移动。direction: left/right/up/down
        返回是否发生了移动。
        """
        # 保存历史
        self.history.append((copy.deepcopy(self.board), self.score))   # 深拷贝当前棋盘和分数,存入历史
        if len(self.history) > 100:  # 如果历史记录超过 100 条
            self.history.pop(0)      # 删除最早的一条,防止内存占用过大

        # 通过旋转把所有方向都变成"左移"
        rotations = {                # 方向到旋转次数的映射字典
            "left": 0,               # 左移:不需要旋转
            "up": 1,                 # 上移:顺时针旋转 1 次
            "right": 2,              # 右移:顺时针旋转 2 次
            "down": 3,               # 下移:顺时针旋转 3 次
        }
        if direction not in rotations:   # 如果传入的方向不合法
            return False             # 返回 False

        # 顺时针旋转 n 次
        for _ in range(rotations[direction]):   # 按方向对应的次数旋转
            self.board = self._rotate_cw(self.board)   # 顺时针旋转棋盘一次

        moved, gained = self._move_left()   # 执行左移操作
        self.score += gained         # 把本次得分加到总分

        # 旋转回来
        back = (4 - rotations[direction]) % 4   # 计算需要反向旋转的次数
        for _ in range(back):        # 反向旋转,把棋盘转回原方向
            self.board = self._rotate_cw(self.board)   # 顺时针旋转(累计还原)

        if moved:                    # 如果发生了移动
            self._add_random()       # 随机添加一个新数字
            self._save_best()        # 更新并保存最高分
        else:                        # 如果没有移动
            self.history.pop()   # 没动就不记录   # 弹出刚才存的历史,因为没有实际移动

        return moved                 # 返回是否发生了移动

    @staticmethod                    # 静态方法装饰器,表示该方法不依赖实例
    def _rotate_cw(board):           # 顺时针旋转棋盘 90° 的方法
        n = len(board)               # 获取棋盘边长
        return [[board[n - 1 - j][i] for j in range(n)] for i in range(n)]   # 列表推导:行列重新组合实现旋转

    # ===== 游戏状态 =====
    def is_game_over(self) -> bool:  # 判断游戏是否结束的方法
        if self._empty_cells():      # 如果还有空格
            return False             # 没结束,可以继续
        # 检查是否还能合并
        for i in range(self.size):   # 遍历每一行
            for j in range(self.size):   # 遍历每一列
                v = self.board[i][j] # 当前格子的值
                if j + 1 < self.size and v == self.board[i][j + 1]:   # 如果右侧格子相同,可以合并
                    return False     # 没结束
                if i + 1 < self.size and v == self.board[i + 1][j]:   # 如果下方格子相同,可以合并
                    return False     # 没结束
        return True                  # 没空格也不能合并,游戏结束

    def has_won(self, target=2048) -> bool:   # 判断是否达到目标数字(默认 2048)
        return any(any(cell >= target for cell in row) for row in self.board)   # 任意格子达到目标即胜利

    def undo(self) -> bool:          # 撤销上一步的方法
        if not self.history:         # 如果没有历史记录
            return False             # 撤销失败
        self.board, self.score = self.history.pop()   # 弹出最近一次历史,恢复棋盘和分数
        return True                  # 撤销成功

    # ===== 显示 =====
    def render(self) -> str:         # 把棋盘渲染成字符串的方法
        cell_width = 6               # 每个格子的显示宽度
        lines = []                   # 存放每一行输出
        hline = "+" + "+".join(["-" * cell_width] * self.size) + "+"   # 横向分隔线
        lines.append(f"分数: {self.score}    最高: {self.best_score}")   # 添加分数显示行
        lines.append(hline)          # 添加顶部分隔线
        for row in self.board:       # 遍历棋盘每一行
            cells = []               # 存放该行每个格子的字符串
            for v in row:            # 遍历该行的每个值
                s = str(v) if v else ""   # 0 显示为空字符串,否则显示数字
                cells.append(f"{s:^{cell_width}}")   # 居中填入定宽格子
            lines.append("|" + "|".join(cells) + "|")   # 用竖线拼接该行
            lines.append(hline)      # 添加分隔线
        return "\n".join(lines)      # 用换行符拼接所有行并返回


def clear_screen():                  # 清屏函数
    os.system("cls" if os.name == "nt" else "clear")   # Windows 用 cls,其他系统用 clear


def get_key():                       # 读取用户按键的函数
    """读取方向键(WASD 或箭头)"""
    # Windows
    if os.name == "nt":              # 如果是 Windows 系统
        import msvcrt                # 导入 Windows 专用键盘模块
        key = msvcrt.getch()         # 读取一个按键(字节)
        if key == b'\xe0':     # 方向键前缀   # 如果是方向键前缀字节
            key2 = msvcrt.getch()    # 再读一个字节判断具体方向
            mapping = {b'H': "up", b'P': "down", b'M': "right", b'K': "left"}   # 方向键字节到方向映射
            return mapping.get(key2, "")   # 返回对应方向字符串
        return key.decode("utf-8", errors="ignore").lower()   # 普通键解码为小写返回
    else:                            # 非 Windows 系统
        # Unix
        import tty, termios          # 导入 Unix 终端控制模块
        fd = sys.stdin.fileno()      # 获取标准输入的文件描述符
        old = termios.tcgetattr(fd)  # 保存原始终端属性
        try:                         # 尝试修改终端模式
            tty.setraw(fd)           # 设置为原始模式,无需回车即可读取
            ch = sys.stdin.read(1)   # 读取一个字符
            if ch == '\x1b':         # 如果是转义符(方向键开头)
                ch2 = sys.stdin.read(2)   # 再读两个字符
                mapping = {'[A': "up", '[B': "down", '[C': "right", '[D': "left"}   # 转义序列到方向映射
                return mapping.get(ch2, "")   # 返回对应方向
            return ch.lower()        # 普通字符转小写返回
        finally:                     # 无论是否异常都执行
            termios.tcsetattr(fd, termios.TCSADRAIN, old)   # 恢复原始终端属性


def main():                          # 主函数,程序入口
    clear_screen()                   # 清屏
    print("=== 2048 ===")            # 打印游戏标题
    print("WASD 或方向键移动, U 撤销, Q 退出")   # 打印操作说明
    input("按任意键开始...")          # 等待用户按键开始

    game = Game2048()                # 创建一局新游戏
    won_shown = False                # 标记胜利提示是否已显示

    while True:                      # 主游戏循环
        clear_screen()               # 清屏
        print(game.render())         # 打印当前棋盘
        print("方向: W/A/S/D  或 ↑ ← ↓ →  |  U 撤销  |  Q 退出")   # 打印操作提示

        if game.has_won() and not won_shown:   # 如果达成 2048 且未提示过
            print("\n🎉 恭喜!你合成了 2048!继续玩吗?(按任意键继续)")   # 打印胜利信息
            won_shown = True         # 标记已提示
            input()                  # 等待用户按键继续

        if game.is_game_over():      # 如果游戏结束
            print(f"\n游戏结束!最终得分: {game.score}")   # 打印结束信息
            print("再来一局?(y/n): ", end="")   # 询问是否再来一局
            ans = input().strip().lower()   # 读取回答并去空格转小写
            if ans == "y":           # 如果选择再来
                game = Game2048()    # 创建新游戏
                won_shown = False    # 重置胜利提示
                continue             # 继续循环
            else:                    # 否则
                break                # 退出游戏循环

        key = get_key()              # 读取用户按键
        mapping = {                  # 按键到方向的映射字典
            "w": "up", "a": "left", "s": "down", "d": "right",   # WASD 键
            "up": "up", "down": "down", "left": "left", "right": "right",   # 方向键
        }
        if key in mapping:           # 如果是移动键
            game.move(mapping[key])  # 执行对应方向移动
        elif key == "u":             # 如果是撤销键
            game.undo()              # 撤销上一步
        elif key == "q":             # 如果是退出键
            print("\n再见!")         # 打印再见
            break                    # 退出游戏循环


if __name__ == "__main__":           # 当脚本直接运行时
    main()                           # 调用主函数
