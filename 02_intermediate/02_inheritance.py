"""02 - 继承与多态

学习目标:
    - 掌握单继承、多继承
    - 理解 MRO(方法解析顺序)
    - 掌握抽象基类
    - 理解多态与鸭子类型
"""

from abc import ABC, abstractmethod  # 从 abc 模块导入 ABC 基类和 abstractmethod 装饰器,用于定义抽象类


# ===== 1. 单继承 =====
print("--- 单继承 ---")  # 打印分隔标题,演示单继承

class Animal:  # 定义父类 Animal,作为动物的基类
    def __init__(self, name):  # 构造方法,接收名字参数
        self.name = name  # 把名字保存到实例属性 name

    def speak(self):  # 定义 speak 方法,要求子类重写
        raise NotImplementedError("子类必须实现")  # 若子类未重写,调用时抛出异常

class Cat(Animal):  # 定义 Cat 类,继承自 Animal
    def speak(self):  # 重写父类的 speak 方法
        return f"{self.name}: 喵~"  # 返回猫叫的字符串

class Dog(Animal):  # 定义 Dog 类,继承自 Animal
    def speak(self):  # 重写父类的 speak 方法
        return f"{self.name}: 汪~"  # 返回狗叫的字符串


for animal in [Cat("小花"), Dog("旺财")]:  # 遍历包含一只猫和一只狗的列表
    print(animal.speak())  # 调用各自的 speak 方法并打印(体现多态)


# ===== 2. 方法重写与 super() =====
print("\n--- super() ---")  # 打印分隔标题,演示 super() 调用父类方法

class Vehicle:  # 定义父类 Vehicle,表示交通工具
    def __init__(self, brand, max_speed):  # 构造方法,接收品牌和最高时速
        self.brand = brand  # 保存品牌到实例属性
        self.max_speed = max_speed  # 保存最高时速到实例属性

    def describe(self):  # 定义 describe 方法,返回描述信息
        return f"{self.brand} 最高时速 {self.max_speed} km/h"  # 返回品牌和最高时速的描述

class ElectricCar(Vehicle):  # 定义 ElectricCar 类,继承自 Vehicle
    def __init__(self, brand, max_speed, battery):  # 子类构造方法,多了一个电池参数
        super().__init__(brand, max_speed)  # 调用父类
        self.battery = battery  # 保存电池容量到实例属性

    def describe(self):  # 重写 describe 方法,扩展父类功能
        base = super().describe()  # 调用父类的 describe 得到基础描述
        return f"{base}, 电池容量 {self.battery} kWh"  # 在父类描述基础上追加电池信息

ec = ElectricCar("Tesla", 250, 100)  # 创建 ElectricCar 实例
print(ec.describe())  # 打印电动车描述信息


# ===== 3. 多继承与 MRO =====
print("\n--- 多继承 MRO ---")  # 打印分隔标题,演示多继承和方法解析顺序

class A:  # 定义类 A
    def hello(self):  # 定义 hello 方法
        return "A.hello"  # 返回字符串标识

class B(A):  # 定义类 B,继承自 A
    def hello(self):  # 重写 hello 方法
        return "B.hello"  # 返回字符串标识

class C(A):  # 定义类 C,继承自 A
    def hello(self):  # 重写 hello 方法
        return "C.hello"  # 返回字符串标识

class D(B, C):    # 多继承
    pass  # D 类继承 B 和 C,自身不添加任何内容

d = D()  # 创建 D 的实例
print("D().hello() =", d.hello())  # 打印 d 调用 hello 的结果,体现 MRO 选择的方法
print("MRO:", [cls.__name__ for cls in D.__mro__])  # 打印 D 的方法解析顺序中的类名列表
# MRO 顺序:D -> B -> C -> A -> object


# ===== 4. Mixin 模式 =====
print("\n--- Mixin ---")  # 打印分隔标题,演示 Mixin 模式
class JsonMixin:  # 定义 JsonMixin,提供转 JSON 的功能
    def to_json(self):  # 定义 to_json 方法
        import json  # 导入 json 模块
        return json.dumps(self.__dict__, ensure_ascii=False, default=str)  # 把实例属性字典转为 JSON 字符串,中文不转义

class LogMixin:  # 定义 LogMixin,提供日志功能
    def log(self, msg):  # 定义 log 方法,接收消息
        print(f"[{self.__class__.__name__}] {msg}")  # 打印带类名的日志信息

class User(JsonMixin, LogMixin):  # 定义 User 类,通过多继承获得 JSON 和日志功能
    def __init__(self, name, age):  # 构造方法,接收名字和年龄
        self.name = name  # 保存名字
        self.age = age  # 保存年龄

u = User("Tom", 18)  # 创建 User 实例
u.log("创建用户")  # 调用从 LogMixin 继承的 log 方法
print(u.to_json())  # 调用从 JsonMixin 继承的 to_json 方法并打印


# ===== 5. 抽象基类(ABC) =====
print("\n--- 抽象基类 ---")  # 打印分隔标题,演示抽象基类

class Shape(ABC):  # 定义抽象基类 Shape,继承自 ABC
    @abstractmethod  # 用装饰器声明 area 为抽象方法,子类必须实现
    def area(self) -> float: ...  # 抽象方法,只定义签名不实现
    @abstractmethod  # 用装饰器声明 perimeter 为抽象方法
    def perimeter(self) -> float: ...  # 抽象方法,只定义签名不实现

    def describe(self):  # 普通方法,子类可直接使用
        return f"面积={self.area():.2f}, 周长={self.perimeter():.2f}"  # 返回面积和周长的描述字符串

class Rectangle(Shape):  # 定义 Rectangle 类,继承抽象类 Shape
    def __init__(self, w, h):  # 构造方法,接收宽和高
        self.w, self.h = w, h  # 同时保存宽和高到实例属性
    def area(self):  # 实现抽象方法 area
        return self.w * self.h  # 返回矩形面积(宽×高)
    def perimeter(self):  # 实现抽象方法 perimeter
        return 2 * (self.w + self.h)  # 返回矩形周长(2×(宽+高))

# s = Shape()  # 报错:不能实例化抽象类
r = Rectangle(3, 4)  # 创建 Rectangle 实例,宽 3 高 4
print(r.describe())  # 打印矩形的描述信息(面积和周长)


# ===== 6. 鸭子类型 =====
print("\n--- 鸭子类型 ---")  # 打印分隔标题,演示鸭子类型
class Duck:  # 定义 Duck 类
    def quack(self): return "嘎嘎"  # 定义 quack 方法,返回鸭子叫声

class Person:  # 定义 Person 类
    def quack(self): return "我会模仿鸭子叫"  # 定义 quack 方法,模仿鸭子叫

def make_quack(thing):  # 定义函数,接收任意对象
    print(thing.quack())  # 只要有 quack 方法就行

make_quack(Duck())  # 传入 Duck 实例,调用 quack
make_quack(Person())  # 传入 Person 实例,也能调用 quack(鸭子类型)


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 实现一个 Shape 继承体系:Triangle/Circle/Square")  # 练习题 1
    print("2. 用 Mixin 给一个类添加序列化和比较功能")  # 练习题 2
    print("3. 用 ABC 定义一个 Plugin 基类,实现两个具体插件")  # 练习题 3
