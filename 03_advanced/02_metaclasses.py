"""02 - 元类编程

学习目标:
    - 理解类也是对象
    - 掌握 type() 的两种用法
    - 学会自定义元类
    - 了解 __new__ / __init__ 在元类中的执行顺序
"""

from abc import ABCMeta, abstractmethod  # 导入抽象基类元类和抽象方法装饰器


# ===== 1. 类也是对象 =====
print("--- 类是对象 ---")  # 打印本节标题
class MyClass:  # 定义一个普通类
    pass  # 空类,仅作演示

# 类由 type 创建
print(f"MyClass 的类型: {type(MyClass)}")  # 打印类的类型,结果是 type  # <class 'type'>

# 动态创建类
MyDynamic = type("MyDynamic", (object,), {"x": 100, "hello": lambda self: "hi"})  # 用 type 动态创建类:类名、基类元组、属性字典
obj = MyDynamic()  # 实例化动态类
print(f"动态类: {obj.x}, {obj.hello()}")  # 打印属性和方法返回值


# ===== 2. 自定义元类 =====
print("\n--- 元类基础 ---")  # 打印本节标题
class UpperAttrMeta(type):  # 定义元类,继承自 type
    """让属性名都变成大写"""  # 元类的说明
    def __new__(mcs, name, bases, namespace):  # 在创建类时拦截,参数:元类、类名、基类、命名空间
        upper_attrs = {  # 构造属性名大写后的新字典
            attr_name if attr_name.startswith("__") else attr_name.upper(): value  # 双下划线开头保留原名,否则转大写
            for attr_name, value in namespace.items()  # 遍历原命名空间
        }
        return super().__new__(mcs, name, bases, upper_attrs)  # 调用父类创建类


class MyClass(metaclass=UpperAttrMeta):  # 使用自定义元类创建类
    x = 1  # 定义属性 x(将被转为 X)
    y = 2  # 定义属性 y(将被转为 Y)
    greet = lambda self: "hi"  # 定义方法 greet(将被转为 GREET)

print("dir(MyClass):", [a for a in dir(MyClass) if not a.startswith("_")])  # 打印非下划线开头的属性名


# ===== 3. 元类应用:自动注册 =====
print("\n--- 插件自动注册 ---")  # 打印本节标题
class PluginRegistry(type):  # 定义插件注册元类
    """自动收集所有子类"""  # 元类说明
    plugins = {}  # 类属性,用于保存已注册的插件

    def __new__(mcs, name, bases, namespace):  # 拦截类的创建
        cls = super().__new__(mcs, name, bases, namespace)  # 先正常创建类
        if bases:    # 跳过基类  # 如果有基类说明是子类
            mcs.plugins[name] = cls  # 把子类注册到字典
        return cls  # 返回创建好的类


class Plugin(metaclass=PluginRegistry):  # 插件基类,使用注册元类
    pass  # 空类


class JSONPlugin(Plugin):  # JSON 插件子类
    def parse(self, data): return data  # 解析方法,直接返回数据


class XMLPlugin(Plugin):  # XML 插件子类
    def parse(self, data): return data  # 解析方法,直接返回数据


print("已注册插件:", list(PluginRegistry.plugins.keys()))  # 打印所有已注册插件名


# ===== 4. 抽象元类 =====
print("\n--- ABCMeta ---")  # 打印本节标题
class Animal(metaclass=ABCMeta):  # 使用 ABCMeta 元类定义抽象基类
    @abstractmethod  # 标记为抽象方法
    def speak(self): ...  # 子类必须实现此方法


class Cat(Animal):  # Cat 继承抽象类 Animal
    def speak(self): return "喵"  # 实现抽象方法


# Animal()  # 报错  # 不能直接实例化抽象类
print(Cat().speak())  # 打印 Cat 实例的 speak 返回值


# ===== 5. 元类与 dataclass =====
print("\n--- dataclass 原理 ---")  # 打印本节标题
from dataclasses import dataclass, field  # 导入数据类装饰器和字段函数

@dataclass  # 用 dataclass 装饰器自动生成 __init__、__repr__ 等方法
class Point:  # 定义点类
    x: float  # x 坐标,浮点数
    y: float  # y 坐标,浮点数
    label: str = "origin"  # 标签,默认为 origin

    def distance_to(self, other):  # 计算到另一个点的距离
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5  # 用勾股定理计算距离


p1 = Point(0, 0)  # 创建点 (0,0)
p2 = Point(3, 4)  # 创建点 (3,4)
print(p1)  # 打印点对象
print(f"距离: {p1.distance_to(p2)}")  # 打印两点距离


# ===== 6. __init_subclass__ (替代元类的现代方法) =====
print("\n--- __init_subclass__ ---")  # 打印本节标题
class Validator:  # 定义校验基类
    def __init_subclass__(cls, required_methods=(), **kwargs):  # 子类被创建时调用
        super().__init_subclass__(**kwargs)  # 调用父类的同名方法
        # 保存要求的方法到类属性,只在非抽象子类中检查
        cls.__required__ = required_methods  # 把要求的方法保存为类属性
        if required_methods:  # 如果指定了必需方法
            # 如果子类自己声明了 required_methods 但没实现,只是作为中间基类,不报错
            # 只在叶子类(没有被子类再继承时)检查 — 这里简化为:不立即报错,留给运行时
            pass  # 此处简化处理,不做立即检查


class Shape(Validator, required_methods=("area", "perimeter")):  # 指定子类必须实现这两个方法
    """抽象基类,子类必须实现 area 和 perimeter"""  # 类说明
    def area(self):  # 面积方法
        raise NotImplementedError  # 抛出未实现错误

    def perimeter(self):  # 周长方法
        raise NotImplementedError  # 抛出未实现错误


class Square(Shape):  # 正方形类继承 Shape
    def __init__(self, side):  # 初始化,接收边长
        self.side = side  # 保存边长
    def area(self):  # 实现面积方法
        return self.side ** 2  # 面积=边长平方
    def perimeter(self):  # 实现周长方法
        return 4 * self.side  # 周长=4倍边长


# class Broken(Shape):    # 报错  # 未实现必需方法的类会报错
#     pass

s = Square(5)  # 创建边长为 5 的正方形
print(f"面积: {s.area()}, 周长: {s.perimeter()}")  # 打印面积和周长


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 用元类实现一个 Singleton(单例模式)")  # 练习题 1
    print("2. 用元类禁止类中出现以 _ 开头的方法(私有方法检查)")  # 练习题 2
    print("3. 用 __init_subclass__ 实现接口校验")  # 练习题 3
