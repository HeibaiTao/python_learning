"""练习 2:数列与字符串

题目描述:
    1. 用 for 循环打印九九乘法表
    2. 输出斐波那契数列前 N 项(N 由用户输入)
    3. 判断一个字符串是否为回文(忽略大小写和非字母字符)
       例如: "A man, a plan, a canal: Panama" -> True
"""

def print_multiplication_table():        # 定义打印九九乘法表的函数
    """打印九九乘法表"""                  # 函数文档字符串
    for i in range(1, 10):               # 外层循环控制行,从 1 到 9
        for j in range(1, i + 1):        # 内层循环控制列,从 1 到当前行号
            print(f"{j}*{i}={i*j}", end="\t")  # 打印乘法算式,end="\t" 用制表符分隔不换行
        print()                          # 一行结束后换行


def fibonacci(n: int):                   # 定义斐波那契数列函数,n 是要生成的项数
    """生成前 n 项斐波那契数列"""          # 函数文档字符串
    if n <= 0:                           # 如果项数小于等于 0
        return []                        # 返回空列表
    seq = [0, 1]                         # 初始化数列前两项 0 和 1
    while len(seq) < n:                  # 当数列长度不足 n 时继续循环
        seq.append(seq[-1] + seq[-2])    # 新项等于最后两项之和,追加到列表末尾
    return seq[:n]                       # 返回前 n 项(处理 n=1 的情况)


def is_palindrome(s: str) -> bool:       # 定义回文判断函数,s 是字符串,返回布尔值
    """判断回文(忽略大小写和非字母)"""     # 函数文档字符串
    cleaned = "".join(c.lower() for c in s if c.isalnum())  # 只保留字母和数字,转小写,拼成新字符串
    return cleaned == cleaned[::-1]      # 比较原字符串和反转字符串是否相等


def fibonacci_demo():                    # 定义斐波那契演示函数(带用户交互)
    try:                                 # 尝试执行输入
        n = int(input("请输入要生成的项数: "))  # 获取用户输入并转为整数
    except ValueError:                   # 如果输入不是整数
        print("请输入合法整数")           # 提示输入合法整数
        return                           # 提前结束函数
    print("斐波那契:", fibonacci(n))     # 调用 fibonacci 函数并打印结果


def palindrome_demo():                   # 定义回文演示函数(带用户交互)
    s = input("请输入字符串: ")           # 获取用户输入的字符串
    print(f"\"{s}\" 是回文: {is_palindrome(s)}")  # 调用 is_palindrome 并打印结果


if __name__ == "__main__":               # 当本文件被直接运行时才执行
    print("--- 九九乘法表 ---")           # 打印标题
    print_multiplication_table()         # 调用打印乘法表函数
    # fibonacci_demo()                   # 取消注释可运行斐波那契演示
    # palindrome_demo()                  # 取消注释可运行回文演示
