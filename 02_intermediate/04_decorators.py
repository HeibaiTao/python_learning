"""04 - 装饰器深入

学习目标:
    - 掌握函数装饰器
    - 掌握带参数的装饰器
    - 学会类装饰器
    - 理解 functools.wraps
"""

import functools  # 导入 functools 模块,提供 wraps 等工具
import time  # 导入 time 模块,用于计时和休眠
import logging  # 导入 logging 模块,用于日志记录(本文件未直接使用)


# ===== 1. 基本装饰器 =====
print("--- 基本装饰器 ---")  # 打印分隔标题,演示基本装饰器
def my_decorator(func):  # 定义装饰器函数,接收被装饰的函数
    @functools.wraps(func)        # 保留原函数元信息
    def wrapper(*args, **kwargs):  # 定义内层包装函数,接收任意参数
        print(f"调用 {func.__name__} 之前")  # 调用原函数前打印提示
        result = func(*args, **kwargs)  # 调用原函数并保存结果
        print(f"调用 {func.__name__} 之后")  # 调用原函数后打印提示
        return result  # 返回原函数的结果
    return wrapper  # 返回包装函数

@my_decorator  # 用 my_decorator 装饰 greet 函数
def greet(name):  # 定义 greet 函数,接收名字
    return f"Hello, {name}"  # 返回问候字符串

print(greet("Tom"))  # 调用被装饰的 greet,会触发装饰器逻辑


# ===== 2. 计时装饰器 =====
print("\n--- 计时装饰器 ---")  # 打印分隔标题,演示计时装饰器
def timer(func):  # 定义计时装饰器
    @functools.wraps(func)  # 保留原函数元信息
    def wrapper(*args, **kwargs):  # 定义包装函数
        t0 = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 调用原函数
        print(f"{func.__name__} 耗时 {time.time() - t0:.4f}s")  # 打印函数耗时
        return result  # 返回原函数结果
    return wrapper  # 返回包装函数

@timer  # 用 timer 装饰 slow_function
def slow_function():  # 定义慢速函数
    time.sleep(0.1)  # 休眠 0.1 秒模拟耗时操作

slow_function()  # 调用函数,会打印耗时


# ===== 3. 带参数的装饰器 =====
print("\n--- 带参数的装饰器 ---")  # 打印分隔标题,演示带参数的装饰器
def repeat(times):  # 外层函数接收装饰器参数(重复次数)
    def decorator(func):  # 中层函数接收被装饰函数
        @functools.wraps(func)  # 保留原函数元信息
        def wrapper(*args, **kwargs):  # 内层包装函数
            for _ in range(times):  # 循环指定次数
                result = func(*args, **kwargs)  # 每次都调用原函数
            return result  # 返回最后一次的结果
        return wrapper  # 返回包装函数
    return decorator  # 返回真正的装饰器

@repeat(3)  # 用 repeat(3) 装饰 say_hi,表示重复调用 3 次
def say_hi():  # 定义 say_hi 函数
    print("Hi!")  # 打印 Hi!

say_hi()  # 调用一次,实际会执行 3 次


# ===== 4. 类装饰器 =====
print("\n--- 类装饰器 ---")  # 打印分隔标题,演示类装饰器
def count_calls(cls):  # 定义类装饰器,接收类
    """统计类实例化次数"""
    original_new = cls.__new__  # 保存原始的 __new__ 方法

    def new_new(cls_, *args, **kwargs):  # 定义新的 __new__ 方法
        cls_.instance_count = getattr(cls_, "instance_count", 0) + 1  # 实例计数加 1
        # object.__new__() 只接受 cls 参数,子类可以接受额外参数
        if original_new is object.__new__:  # 如果原方法是 object.__new__
            return original_new(cls_)  # 只传 cls 参数
        return original_new(cls_, *args, **kwargs)  # 否则传递所有参数

    cls.__new__ = staticmethod(new_new)  # 用新方法替换类的 __new__
    return cls  # 返回修改后的类

@count_calls  # 用 count_calls 装饰 Widget 类
class Widget:  # 定义 Widget 类
    def __init__(self, name):  # 构造方法,接收名字
        self.name = name  # 保存名字到实例属性

w1 = Widget("a"); w2 = Widget("b")  # 创建两个 Widget 实例
print(f"创建了 {Widget.instance_count} 个 Widget")  # 打印实例化次数


# ===== 5. 装饰器链 =====
print("\n--- 装饰器链 ---")  # 打印分隔标题,演示多个装饰器叠加
def bold(func):  # 定义 bold 装饰器,加粗标签
    @functools.wraps(func)  # 保留原函数元信息
    def wrapper(*args, **kwargs):  # 包装函数
        return f"<b>{func(*args, **kwargs)}</b>"  # 给结果套上 <b> 标签
    return wrapper  # 返回包装函数

def italic(func):  # 定义 italic 装饰器,斜体标签
    @functools.wraps(func)  # 保留原函数元信息
    def wrapper(*args, **kwargs):  # 包装函数
        return f"<i>{func(*args, **kwargs)}</i>"  # 给结果套上 <i> 标签
    return wrapper  # 返回包装函数

@bold  # 先应用外层 bold 装饰器
@italic  # 再应用内层 italic 装饰器
def hello():  # 定义 hello 函数
    return "Hello"  # 返回字符串 Hello

print(hello())   # <b><i>Hello</i></b>


# ===== 6. 缓存装饰器 =====
print("\n--- 缓存装饰器 ---")  # 打印分隔标题,演示缓存装饰器
@functools.lru_cache(maxsize=128)  # 用 lru_cache 装饰,最多缓存 128 个结果
def fib(n):  # 定义斐波那契函数
    if n < 2:  # 如果 n 小于 2
        return n  # 直接返回 n(基线条件)
    return fib(n - 1) + fib(n - 2)  # 递归计算前两项之和

print(f"fib(50) = {fib(50)}")  # 快速计算


# ===== 7. property 装饰器回顾 =====
print("\n--- 进阶 property ---")  # 打印分隔标题,演示进阶 property
class Temperature:  # 定义 Temperature 类,演示 property
    def __init__(self, celsius: float):  # 构造方法,接收摄氏度
        self._celsius = celsius  # 把摄氏度存到受保护属性

    @property  # 把 celsius 方法定义为属性
    def celsius(self):  # celsius 的 getter
        return self._celsius  # 返回摄氏度

    @celsius.setter  # 为 celsius 添加 setter
    def celsius(self, value):  # 设置摄氏度时进行校验
        if value < -273.15:  # 如果低于绝对零度
            raise ValueError("低于绝对零度")  # 抛出异常
        self._celsius = value  # 合法则更新摄氏度

    @property  # 把 fahrenheit 定义为只读属性
    def fahrenheit(self):  # 华氏度的 getter
        return self._celsius * 9 / 5 + 32  # 由摄氏度换算华氏度

t = Temperature(100)  # 创建 Temperature 实例,100 摄氏度
print(f"100°C = {t.fahrenheit}°F")  # 打印换算后的华氏度


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 写一个 retry 装饰器,失败后自动重试 N 次")  # 练习题 1
    print("2. 写一个 type_check 装饰器,根据函数注解做参数类型校验")  # 练习题 2
    print("3. 写一个 singleton 装饰器,让类只能有一个实例")  # 练习题 3
