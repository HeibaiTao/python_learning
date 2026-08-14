"""练习 1:变量交换与基本运算

题目描述:
    1. 不使用第三个变量,交换 a 和 b 的值
    2. 接收用户输入的两个数字,计算它们的和、差、积、商
    3. 判断用户输入的年份是否为闰年
       (闰年:能被4整除但不能被100整除,或能被400整除)

要求:
    - 每个功能用独立函数实现
    - 处理非法输入(非数字)
    - 主程序能依次演示三个功能
"""

def swap_demo():                          # 定义变量交换演示函数
    """演示变量交换"""                     # 函数文档字符串
    a, b = 5, 10                          # 初始化两个变量 a=5, b=10
    print(f"交换前: a={a}, b={b}")         # 打印交换前的值
    a, b = b, a                           # Python 特色交换,无需第三个变量
    print(f"交换后: a={a}, b={b}")         # 打印交换后的值


def basic_calculator():                   # 定义简单计算器函数
    """简单计算器"""                       # 函数文档字符串
    try:                                  # 尝试执行可能出错的输入
        x = float(input("请输入第一个数字: "))  # 获取用户输入并转为浮点数
        y = float(input("请输入第二个数字: "))  # 获取用户输入并转为浮点数
    except ValueError:                    # 如果输入不是数字会触发 ValueError
        print("输入必须是数字")            # 提示输入必须为数字
        return                            # 提前结束函数

    print(f"{x} + {y} = {x + y}")         # 打印加法结果
    print(f"{x} - {y} = {x - y}")         # 打印减法结果
    print(f"{x} * {y} = {x * y}")         # 打印乘法结果
    if y != 0:                            # 如果除数不为 0
        print(f"{x} / {y} = {x / y}")     # 打印除法结果
    else:                                 # 如果除数为 0
        print("除数不能为0")               # 提示除数不能为 0


def is_leap_year(year: int) -> bool:      # 定义闰年判断函数,year 是整数,返回布尔值
    """判断是否闰年"""                     # 函数文档字符串
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # 能被4整除且不被100整除,或能被400整除


def leap_year_check():                    # 定义闰年检测器函数(带用户交互)
    """闰年检测器"""                       # 函数文档字符串
    try:                                  # 尝试执行输入
        year = int(input("请输入年份: "))  # 获取用户输入的年份并转为整数
    except ValueError:                    # 如果输入不是整数
        print("年份必须是整数")            # 提示必须输入整数
        return                            # 提前结束函数

    if is_leap_year(year):                # 调用 is_leap_year 函数判断
        print(f"{year} 年是闰年")          # 是闰年则打印提示
    else:                                 # 否则
        print(f"{year} 年不是闰年")        # 打印不是闰年


if __name__ == "__main__":                # 当本文件被直接运行时才执行
    swap_demo()                           # 调用变量交换演示函数
    # basic_calculator()       # 取消注释以运行交互版本  # 取消注释可运行计算器
    # leap_year_check()                                 # 取消注释可运行闰年检测
