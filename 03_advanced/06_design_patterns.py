"""06 - 设计模式

学习目标:
    - 掌握常见设计模式的 Python 实现
    - 理解模式的应用场景
    - 学会用 Python 高级特性简化模式实现
"""

from __future__ import annotations  # 启用延迟注解求值,允许类内引用自身类型
from typing import Protocol, Any  # 导入协议和任意类型
import functools  # 导入 functools 用于装饰器工具


# ===== 1. 单例模式 =====
print("--- Singleton ---")  # 打印本节标题
class Singleton:  # 定义单例类
    _instance = None  # 类属性保存唯一实例
    def __new__(cls, *args, **kwargs):  # 重写创建实例的方法
        if cls._instance is None:  # 如果还没创建过实例
            cls._instance = super().__new__(cls)  # 调用父类创建并保存
        return cls._instance  # 返回唯一实例

s1 = Singleton()  # 创建实例 1
s2 = Singleton()  # 创建实例 2
print(f"s1 is s2: {s1 is s2}")  # 打印是否为同一对象

# 装饰器版本
def singleton(cls):  # 定义单例装饰器函数
    instances = {}  # 用字典保存各类的实例
    @functools.wraps(cls)  # 保留原类的元信息
    def get_instance(*args, **kwargs):  # 包装后的获取实例函数
        if cls not in instances:  # 如果该类还没创建实例
            instances[cls] = cls(*args, **kwargs)  # 创建并保存
        return instances[cls]  # 返回实例
    return get_instance  # 返回包装函数

@singleton  # 用装饰器把 Database 变成单例
class Database:  # 定义数据库类
    def __init__(self):  # 初始化方法
        self.connection = "connected"  # 模拟连接状态

d1 = Database(); d2 = Database()  # 两次获取实例
print(f"d1 is d2: {d1 is d2}")  # 打印是否为同一对象


# ===== 2. 工厂模式 =====
print("\n--- Factory ---")  # 打印本节标题
class Animal(Protocol):  # 定义动物协议
    def speak(self) -> str: ...  # 要求实现 speak 方法

class Dog:  # 狗类
    def speak(self): return "汪"  # 返回汪汪

class Cat:  # 猫类
    def speak(self): return "喵"  # 返回喵喵

class Fish:  # 鱼类
    def speak(self): return "..."  # 返回省略号

def animal_factory(kind: str) -> Animal:  # 工厂函数,根据字符串创建动物
    factory = {"dog": Dog, "cat": Cat, "fish": Fish}  # 字符串到类的映射
    if kind not in factory:  # 如果是未知类型
        raise ValueError(f"未知动物: {kind}")  # 抛出错误
    return factory[kind]()  # 实例化对应的类

for kind in ["dog", "cat", "fish"]:  # 遍历三种动物
    a = animal_factory(kind)  # 用工厂创建
    print(f"  {kind}: {a.speak()}")  # 打印叫声


# ===== 3. 观察者模式 =====
print("\n--- Observer ---")  # 打印本节标题
class Subject:  # 主题类(被观察者)
    def __init__(self):  # 初始化方法
        self._observers: list = []  # 观察者列表
    def subscribe(self, observer):  # 订阅方法
        self._observers.append(observer)  # 添加观察者
    def unsubscribe(self, observer):  # 取消订阅方法
        self._observers.remove(observer)  # 移除观察者
    def notify(self, message):  # 通知方法
        for obs in self._observers:  # 遍历所有观察者
            obs.update(message)  # 调用其 update 方法

class Observer:  # 观察者类
    def __init__(self, name): self.name = name  # 初始化时设置名字
    def update(self, message): print(f"  [{self.name}] 收到: {message}")  # 收到通知时打印

subject = Subject()  # 创建主题
o1 = Observer("A"); o2 = Observer("B")  # 创建两个观察者
subject.subscribe(o1)  # 订阅 o1
subject.subscribe(o2)  # 订阅 o2
subject.notify("事件发生")  # 通知所有观察者
subject.unsubscribe(o1)  # o1 取消订阅
subject.notify("第二个事件")  # 再次通知


# ===== 4. 策略模式 =====
print("\n--- Strategy ---")  # 打印本节标题
class SortStrategy(Protocol):  # 定义排序策略协议
    def sort(self, data: list) -> list: ...  # 要求实现 sort 方法

class QuickSort:  # 快速排序类
    def sort(self, data):  # 排序方法
        if len(data) <= 1: return data  # 长度小于等于 1 直接返回
        pivot = data[0]  # 取第一个元素为基准
        return ([x for x in data[1:] if x < pivot] +  # 比基准小的部分
                [pivot] +  # 基准本身
                [x for x in data[1:] if x >= pivot])  # 比基准大的部分

class BubbleSort:  # 冒泡排序类
    def sort(self, data):  # 排序方法
        arr = data[:]  # 复制一份数据
        for i in range(len(arr)):  # 外层循环
            for j in range(len(arr) - 1 - i):  # 内层循环
                if arr[j] > arr[j+1]:  # 如果前大后小
                    arr[j], arr[j+1] = arr[j+1], arr[j]  # 交换
        return arr  # 返回排序后的列表

class Sorter:  # 排序器类
    def __init__(self, strategy: SortStrategy):  # 接收一个排序策略
        self.strategy = strategy  # 保存策略
    def sort(self, data):  # 排序方法
        return self.strategy.sort(data)  # 委托给策略对象

data = [3, 1, 4, 1, 5, 9, 2, 6]  # 测试数据
print(f"  快排: {Sorter(QuickSort()).sort(data)}")  # 用快排
print(f"  冒泡: {Sorter(BubbleSort()).sort(data)}")  # 用冒泡


# ===== 5. 装饰器模式 =====
print("\n--- Decorator (模式) ---")  # 打印本节标题
class Component(Protocol):  # 定义组件协议
    def operation(self) -> str: ...  # 要求实现 operation 方法

class ConcreteComponent:  # 具体组件类
    def operation(self) -> str: return "ConcreteComponent"  # 返回组件名

class Decorator:  # 装饰器基类
    def __init__(self, component: Component):  # 接收被装饰的组件
        self._component = component  # 保存组件
    def operation(self) -> str:  # 操作方法
        return self._component.operation()  # 委托给组件

class BoldDecorator(Decorator):  # 加粗装饰器
    def operation(self) -> str:  # 重写操作
        return f"<b>{super().operation()}</b>"  # 用 b 标签包裹

class ItalicDecorator(Decorator):  # 斜体装饰器
    def operation(self) -> str:  # 重写操作
        return f"<i>{super().operation()}</i>"  # 用 i 标签包裹

result = BoldDecorator(ItalicDecorator(ConcreteComponent())).operation()  # 嵌套装饰
print(f"  {result}")  # 打印结果


# ===== 6. 上下文模式:Object Pool =====
print("\n--- Object Pool ---")  # 打印本节标题
class ObjectPool:  # 对象池类
    def __init__(self, factory, max_size=10):  # 接收工厂函数和最大容量
        self._factory = factory  # 保存工厂函数
        self._pool: list = []  # 空闲对象列表
        self._max = max_size  # 最大容量

    def acquire(self):  # 获取对象
        if self._pool:  # 池中有空闲对象
            return self._pool.pop()  # 弹出一个返回
        return self._factory()  # 否则新建

    def release(self, obj):  # 释放对象回池
        if len(self._pool) < self._max:  # 池未满
            self._pool.append(obj)  # 放回池中


class Connection:  # 连接类
    _id = 0  # 类属性,自增 ID
    def __init__(self):  # 初始化方法
        Connection._id += 1  # ID 自增
        self.id = Connection._id  # 保存唯一 ID
    def __repr__(self):  # 字符串表示
        return f"Conn#{self.id}"  # 返回连接编号


pool = ObjectPool(Connection, max_size=3)  # 创建对象池
c1 = pool.acquire()  # 获取连接 1
c2 = pool.acquire()  # 获取连接 2
pool.release(c1)  # 释放 c1 回池
c3 = pool.acquire()     # 复用 c1  # 再次获取时复用 c1
print(f"  {c1}, {c2}, {c3}")  # 打印三个连接


# ===== 7. 责任链模式 =====
print("\n--- Chain of Responsibility ---")  # 打印本节标题
class Handler(Protocol):  # 定义处理者协议
    def set_next(self, handler): ...  # 设置下一个处理者
    def handle(self, request): ...  # 处理请求

class BaseHandler:  # 处理者基类
    def __init__(self):  # 初始化方法
        self._next = None  # 下一个处理者默认为空
    def set_next(self, handler):  # 设置下一个处理者
        self._next = handler  # 保存
        return handler  # 返回处理者以便链式调用
    def handle(self, request):  # 处理请求
        if self._next:  # 如果有下一个处理者
            return self._next.handle(request)  # 传递下去
        return None  # 否则返回 None

class AuthHandler(BaseHandler):  # 认证处理者
    def handle(self, request):  # 处理请求
        if "user" in request:  # 如果请求中有 user
            print(f"  Auth 通过: {request['user']}")  # 打印认证通过
            return super().handle(request)  # 传给下一个
        print("  Auth 失败")  # 打印失败
        return None  # 返回 None

class LogHandler(BaseHandler):  # 日志处理者
    def handle(self, request):  # 处理请求
        print(f"  Log 记录: {request}")  # 打印日志
        return super().handle(request)  # 传给下一个


auth = AuthHandler()  # 创建认证处理器
log = LogHandler()  # 创建日志处理器
auth.set_next(log)  # 设置日志处理器为下一个
auth.handle({"user": "Tom", "action": "login"})  # 处理登录请求


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 实现一个 Builder 模式构建复杂对象")  # 练习题 1
    print("2. 实现一个 Adapter 让旧 API 适配新接口")  # 练习题 2
    print("3. 实现一个简单的 MVC 框架(用以上模式)")  # 练习题 3
