"""练习 3:猜数字与密码强度检查

题目描述:
    1. 实现猜数字游戏
       - 程序随机生成 1-100 的数字
       - 用户输入猜测,程序提示"大了"或"小了"
       - 猜中后显示用了多少次,并允许选择再玩一局
    2. 实现密码强度检查函数
       - 长度 >= 8
       - 同时包含大小写字母、数字、特殊字符
       - 返回 0-4 的强度评分
"""

import random                       # 导入随机数模块,用于生成随机数字
import string                       # 导入字符串模块,用于获取特殊字符集合


def guess_number():                 # 定义猜数字游戏函数
    """猜数字游戏"""                 # 函数文档字符串
    while True:                     # 外层循环:控制是否再玩一局
        secret = random.randint(1, 100)  # 生成 1-100 的随机数字
        count = 0                       # 初始化猜测次数为 0
        print("\n我心里想了一个 1-100 的数字,你来猜!")  # 打印游戏提示

        while True:                 # 内层循环:反复让用户猜
            try:                    # 尝试获取用户输入
                guess = int(input("请输入: "))  # 获取输入并转为整数
            except ValueError:      # 如果输入不是数字
                print("请输入数字")  # 提示输入数字
                continue            # 跳过本次,继续让用户输入

            count += 1              # 猜测次数加 1
            if guess < secret:      # 如果猜的比目标小
                print("小了")       # 提示小了
            elif guess > secret:    # 如果猜的比目标大
                print("大了")       # 提示大了
            else:                   # 否则就是猜对了
                print(f"恭喜!你猜中了,用了 {count} 次")  # 打印恭喜信息和次数
                break               # 跳出内层循环,结束本局

        again = input("再玩一次?(y/n): ").strip().lower()  # 询问是否再玩,去掉空格并转小写
        if again != "y":            # 如果回答不是 y
            break                   # 跳出外层循环,结束游戏


def check_password_strength(password: str) -> int:  # 定义密码强度检查函数,返回 0-4 的评分
    """返回 0-4 的强度评分"""        # 函数文档字符串
    score = 0                       # 初始化分数为 0
    if len(password) >= 8:          # 如果密码长度大于等于 8
        score += 1                  # 分数加 1
    if any(c.islower() for c in password):  # 如果密码中包含小写字母
        score += 1                  # 分数加 1
    if any(c.isupper() for c in password):  # 如果密码中包含大写字母
        score += 1                  # 分数加 1
    if any(c.isdigit() for c in password):  # 如果密码中包含数字
        score += 1                  # 分数加 1
    if any(c in string.punctuation for c in password):  # 如果密码中包含特殊字符
        score += 1                  # 分数加 1
    return min(score, 4)            # 返回分数,最大不超过 4


def password_demo():                # 定义密码演示函数(带用户交互)
    while True:                     # 循环让用户反复输入密码
        pwd = input("请输入密码(输入 q 退出): ")  # 获取用户输入的密码
        if pwd == "q":              # 如果输入 q
            break                   # 退出循环
        score = check_password_strength(pwd)  # 调用强度检查函数
        levels = ["极弱", "较弱", "中等", "较强", "极强"]  # 强度等级对应中文
        print(f"强度: {levels[score]} ({score}/4)")  # 打印强度等级和分数


if __name__ == "__main__":          # 当本文件被直接运行时才执行
    # guess_number()                # 取消注释可运行猜数字游戏
    password_demo()                 # 调用密码演示函数
