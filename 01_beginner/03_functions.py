"""03 - 函数

学习目标:
    - 掌握函数定义、参数、返回值
    - 理解 *args / **kwargs
    - 了解作用域(L/E/N/G)
    - 掌握 lambda 表达式
"""

# ===== 1. 函数基础 =====
print("--- 函数基础 ---")  # 打印本节标题
def greet(name: str) -> str:        # 定义函数 greet,name 参数后是类型提示,-> str 表示返回字符串
    """返回一个问候语"""              # 函数的文档字符串,说明函数作用
    return f"Hello, {name}!"         # 返回拼接好的问候语

print(greet("Python"))  # 调用 greet 函数并打印结果


# ===== 2. 参数类型 =====
print("\n--- 参数类型 ---")  # 打印参数类型部分标题

# 位置参数
def add(a, b):  # 定义加法函数,a 和 b 是位置参数,按顺序传入
    return a + b  # 返回 a 加 b 的结果

# 默认参数(必须放在位置参数之后)
def power(x, n=2):  # n 有默认值 2,调用时不传 n 就用 2
    return x ** n  # 返回 x 的 n 次方

print(power(3))          # 9,使用默认 n=2
print(power(3, 3))       # 27  # 传入 n=3,计算 3 的 3 次方

# 关键字参数
print(power(n=3, x=2))   # 8,顺序无关  # 用参数名指定,顺序可以任意

# *args:接收多余的位置参数(打包成元组)
def sum_all(*args):  # *args 把所有位置参数收集成元组
    return sum(args)  # 用 sum 函数对元组求和并返回

print(sum_all(1, 2, 3, 4, 5))  # 打印多个数字的和

# **kwargs:接收多余的关键字参数(打包成字典)
def user_info(**kwargs):  # **kwargs 把所有关键字参数收集成字典
    for k, v in kwargs.items():  # 遍历字典的键值对
        print(f"  {k}: {v}")     # 打印每个键值对

user_info(name="Tom", age=18, city="Beijing")  # 调用函数,传入多个关键字参数

# 组合使用
def func(a, b, *args, c=10, **kwargs):  # 演示各种参数类型的组合
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")  # 打印所有参数的值

func(1, 2, 3, 4, c=20, x=100, y=200)  # 调用组合参数函数


# ===== 3. 返回值 =====
print("\n--- 返回值 ---")  # 打印返回值部分标题
def divide(a, b):              # 定义除法函数
    if b == 0:                 # 如果除数为 0
        return None  # 提前返回  # 返回 None 避免除零错误
    return a / b, a % b   # 返回元组  # 同时返回商和余数(多个值会打包成元组)

result = divide(10, 3)  # 调用函数,结果是一个元组
print(result)              # (3.33..., 1)  # 打印元组结果
quotient, remainder = divide(10, 3)  # 解包  # 把元组解包成两个变量
print(f"商={quotient}, 余数={remainder}")  # 打印商和余数


# ===== 4. 作用域(LEGB 规则) =====
print("\n--- 作用域 ---")  # 打印作用域部分标题
x = "global"           # G:Global  # 全局变量,在整个文件中都可访问

def outer():           # 定义外层函数
    x = "enclosing"    # E:Enclosing  # 嵌套作用域变量,对外层函数有效
    def inner():       # 定义内层函数
        x = "local"    # L:Local  # 局部变量,只在 inner 函数内有效
        print(x)       # 打印局部变量 x
    inner()            # 调用内层函数

outer()  # local  # 调用外层函数,会打印 local

# global 关键字
counter = 0            # 定义全局变量 counter
def inc():             # 定义自增函数
    global counter     # 声明要使用全局变量 counter(否则会创建新的局部变量)
    counter += 1       # 全局变量 counter 加 1
inc()                  # 调用自增函数
print(counter)         # 打印 counter 的值(已变为 1)

# nonlocal 关键字
def outer2():          # 定义外层函数
    n = 0              # 外层函数的局部变量
    def inner():       # 定义内层函数
        nonlocal n     # 声明使用外层函数的变量 n(不是全局也不是局部)
        n += 1         # 修改外层变量 n
        return n       # 返回 n 的值
    return inner       # 返回内层函数本身(闭包)

f = outer2()           # 调用 outer2 得到 inner 函数,赋值给 f
print(f(), f(), f())   # 1, 2, 3  # 每次调用 f,n 都会累加


# ===== 5. lambda 表达式 =====
print("\n--- lambda ---")  # 打印 lambda 部分标题
square = lambda x: x ** 2  # 用 lambda 定义匿名函数,计算 x 的平方
print(square(5))           # 调用 lambda 函数,打印 25

# 常与 sorted/map/filter 配合使用
students = [("Tom", 85), ("Jerry", 92), ("Alice", 78)]  # 学生列表,每个元素是(姓名, 分数)
students_sorted = sorted(students, key=lambda s: s[1], reverse=True)  # 按分数降序排序,key 指定用元组第 2 项比较
print(students_sorted)  # 打印排序后的列表


# ===== 6. 函数也是对象 =====
print("\n--- 函数对象 ---")  # 打印函数对象部分标题
def shout(text):        # 定义大写转换函数
    return text.upper() # 把文本转成大写

def whisper(text):      # 定义小写转换函数
    return text.lower() # 把文本转成小写

def speak(func, text):    # 函数作为参数  # 接收一个函数和文本,调用该函数处理文本
    print(func(text))     # 调用传入的函数处理文本并打印

speak(shout, "hello")  # 用 shout 函数处理"hello",打印 HELLO
speak(whisper, "WORLD")  # 用 whisper 函数处理"WORLD",打印 world


# ===== 7. 装饰器示例 =====
def log_decorator(func):  # 定义装饰器函数,接收一个函数作为参数
    """装饰器：在函数调用前后打印日志"""  # 装饰器的文档字符串
    def wrapper(*args, **kwargs):  # 定义内部包装函数,接收任意参数
        print(f"[日志] 函数 {func.__name__} 开始调用")  # 打印函数开始调用的日志
        print(f"[日志] 参数: args={args}, kwargs={kwargs}")  # 打印传入的参数

        result = func(*args, **kwargs)  # 调用原函数  # 调用被装饰的函数并保存返回值

        print(f"[日志] 函数 {func.__name__} 执行完毕")  # 打印函数执行完毕的日志
        print(f"[日志] 返回值: {result}")  # 打印返回值
        return result  # 返回原函数的结果
    return wrapper  # 返回包装函数


@log_decorator  # 用装饰器装饰下面的 add 函数
def add(a, b):   # 定义加法函数
    return a + b  # 返回 a 加 b

@log_decorator  # 用装饰器装饰下面的 greet 函数
def greet(name, greeting="你好"):  # 定义问候函数,greeting 有默认值
    return f"{greeting}, {name}!"  # 返回问候语


if __name__ == "__main__":  # 当本文件被直接运行时才执行下面的代码
    print("\n[练习] 请尝试:")  # 打印练习提示标题
    print("1. 编写一个计算阶乘的函数(用递归)")  # 练习建议 1
    print("2. 用 *args 编写一个统计函数(均值/中位数/最大值)")  # 练习建议 2
    print("3. 编写一个装饰器,在函数调用前后打印日志")  # 练习建议 3

    # 阶乘函数示例(递归)
    def factorial(n):  # 定义阶乘函数
        """计算 n 的阶乘"""  # 函数文档字符串
        if n <= 1:        # 递归终止条件:n<=1 时
            return 1      # 返回 1
        return n * factorial(n - 1)  # 递归调用,n 乘以 (n-1) 的阶乘

    print(f"5! = {factorial(5)}")  # 120  # 打印 5 的阶乘

    # def average_all(*args):
    #     return sum(args) / len(args)

    # print(average_all(1, 2, 3, 4, 5))

    def stats(*args):  # 定义统计函数,接收任意多个数字
        """统计函数:返回均值、中位数、最大值"""  # 函数文档字符串
        if len(args) == 0:  # 如果没有传入任何参数
            return None     # 返回 None
        
        # 排序后的列表(中位数需要)
        sorted_args = sorted(args)  # 对参数排序,用于计算中位数
        n = len(args)               # 获取参数个数
        
        # 均值
        mean = sum(args) / n        # 计算平均值
        
        # 中位数
        if n % 2 == 1:  # 奇数个  # 如果参数个数是奇数
            median = sorted_args[n // 2]  # 中位数是排序后中间那个数
        else:           # 偶数个  # 如果参数个数是偶数
            median = (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2  # 中位数是中间两个数的平均值
        
        # 最大值
        maximum = max(args)  # 用 max 函数求最大值
        
        return mean, median, maximum  # 返回均值、中位数、最大值
    print(stats(1, 2, 3, 4, 5, 8, 88))  # 打印统计结果

    # 测试装饰器
    print("\n--- 装饰器测试 ---")  # 打印装饰器测试标题
    print(add(3, 5))  # 调用被装饰的 add 函数,会自动打印日志
    print("---")      # 打印分隔线
    print(greet("小明", greeting="早上好"))  # 调用被装饰的 greet 函数
