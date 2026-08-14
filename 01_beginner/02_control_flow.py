"""02 - 流程控制

学习目标:
    - 掌握 if/elif/else 条件分支
    - 掌握 for/while 循环
    - 理解 break、continue、else 子句
    - 了解 match-case(Python 3.10+)
"""

# ===== 1. if 条件分支 =====
print("--- if 条件分支 ---")  # 打印本节标题
score = 85                    # 定义一个分数变量用于演示条件判断
if score >= 90:               # 如果分数大于等于 90
    grade = "A"               # 等级设为 A
elif score >= 80:             # 否则如果分数大于等于 80
    grade = "B"               # 等级设为 B
elif score >= 70:             # 否则如果分数大于等于 70
    grade = "C"               # 等级设为 C
else:                         # 以上条件都不满足时
    grade = "D"               # 等级设为 D
print(f"分数 {score} 对应等级 {grade}")  # 打印分数和对应的等级

# 三元表达式
result = "及格" if score >= 60 else "不及格"  # 一行写完 if-else,分数>=60 返回"及格",否则"不及格"
print(result)                                 # 打印三元表达式的结果


# ===== 2. for 循环 =====
print("\n--- for 循环 ---")  # 打印 for 循环部分标题
# 遍历列表
fruits = ["apple", "banana", "cherry"]  # 定义一个水果列表
for fruit in fruits:                    # 逐个取出列表中的水果
    print(fruit)                        # 打印当前水果

# range() 生成序列
for i in range(5):           # range(5) 生成 0 到 4 的序列
    print(i, end=" ")        # 打印数字,用空格分隔而不换行
print()                      # 打印空行,起到换行作用

for i in range(1, 10, 2):    # range(起点, 终点, 步长),生成 1,3,5,7,9
    print(i, end=" ")        # 打印数字,用空格分隔
print()                      # 换行

# enumerate():同时拿到索引和值
for idx, fruit in enumerate(fruits, start=1):  # enumerate 同时返回索引和值,start=1 表示索引从 1 开始
    print(f"{idx}. {fruit}")                   # 打印"序号. 水果名"


# ===== 3. while 循环 =====
print("\n--- while 循环 ---")  # 打印 while 循环部分标题
n = 5                         # 初始化变量 n 为 5
while n > 0:                  # 当 n 大于 0 时,重复执行循环体
    print(n)                  # 打印当前 n 的值
    n -= 1                    # n 每次减 1,最终会变为 0 退出循环


# ===== 4. break / continue / else =====
print("\n--- break/continue/else ---")  # 打印本节标题
# break:跳出整个循环
for i in range(10):           # 循环 0 到 9
    if i == 5:                # 当 i 等于 5 时
        break                 # break 跳出整个循环,不再继续
    print(i, end=" ")         # 打印当前 i,用空格分隔
print()                       # 换行

# continue:跳过本次
for i in range(5):            # 循环 0 到 4
    if i == 2:                # 当 i 等于 2 时
        continue              # continue 跳过本次循环后面的代码,直接进入下一次
    print(i, end=" ")         # 打印当前 i(2 会被跳过)
print()                       # 换行

# else 子句:循环正常结束(没被 break)时执行
for i in range(3):            # 循环 0 到 2
    print(i)                  # 打印当前 i
else:                         # 循环正常结束后执行(如果被 break 则不执行)
    print("循环正常结束")      # 打印提示信息


# ===== 5. match-case(Python 3.10+) =====
print("\n--- match-case ---")  # 打印 match-case 部分标题
status = 404                   # 定义一个状态码变量
match status:                  # 根据 status 的值进行模式匹配
    case 200:                  # 如果 status 是 200
        print("OK")            # 打印 OK
    case 404:                  # 如果 status 是 404
        print("Not Found")     # 打印 Not Found
    case 500:                  # 如果 status 是 500
        print("Server Error")  # 打印 Server Error
    case _:                    # 默认分支,匹配任意值(类似 switch 的 default)
        print("Unknown")       # 打印 Unknown


# ===== 6. 列表推导式(基础) =====
print("\n--- 列表推导式 ---")         # 打印列表推导式部分标题
squares = [x ** 2 for x in range(10)]  # 生成 0-9 每个数的平方组成的列表
evens = [x for x in range(20) if x % 2 == 0]  # 筛选 0-19 中所有的偶数
print(squares)                          # 打印平方列表
print(evens)                            # 打印偶数列表


# ===== 7. pass 占位符 =====
print("\n--- pass ---")  # 打印 pass 部分标题
if True:                 # if 条件为真
    pass  # 占位,什么都不做,保证语法完整


if __name__ == "__main__":  # 当本文件被直接运行时才执行下面的代码
    print("\n[练习] 请尝试:")  # 打印练习提示标题
    print("1. 用 for 循环打印九九乘法表")        # 练习建议 1
    print("2. 用 while 实现猜数字游戏(1-100)")    # 练习建议 2
    print("3. 用 match-case 处理不同 HTTP 状态码")  # 练习建议 3

for i in range(1, 10):              # 外层循环,行号 1-9
    for j in range(1, i + 1):       # 内层循环,列号 1 到当前行号
        print(f"{j}×{i}={i*j:2d}", end="  ")  # :2d 让结果占2位,对齐
    print()                         # 每行结束后换行

import random                       # 导入随机数模块

target = random.randint(1, 100)  # 随机生成 1-100 的数
count = 0                       # 记录猜测次数,初始为 0
print("猜数字游戏(1-100),输入 q 退出")  # 打印游戏说明

while True:                          # 无限循环,直到猜对或退出
    guess = input("请输入你的猜测: ")  # 获取用户输入
    
    if guess == "q":                 # 如果用户输入 q
        print(f"退出游戏,答案是 {target}")  # 打印答案并退出
        break                        # 跳出循环,结束游戏
    
    guess = int(guess)               # 将输入的字符串转换为整数
    count += 1                       # 猜测次数加 1
    
    if guess < target:               # 如果猜的数字比目标小
        print("太小了!")              # 提示太小
    elif guess > target:             # 如果猜的数字比目标大
        print("太大了!")              # 提示太大
    else:                            # 否则就是猜对了
        print(f"猜对了!用了 {count} 次")  # 打印恭喜信息和猜测次数
        break                        # 跳出循环,结束游戏
