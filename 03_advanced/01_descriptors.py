"""01 - 描述符与属性协议

学习目标:
    - 理解描述符协议
    - 掌握 __get__、__set__、__delete__
    - 实现类型校验描述符
    - 理解 property 的本质
"""


# ===== 1. 描述符协议 =====
print("--- 描述符基础 ---")  # 打印分隔标题,标识本节内容
class Verbose_attribute:  # 定义一个简单的描述符类
    """一个简单的描述符"""  # 类的文档字符串说明
    def __get__(self, obj, objtype=None):  # 定义读取时的钩子方法,参数为实例和所属类
        print(f"访问 {objtype.__name__}.attr on {obj!r}")  # 打印访问日志信息
        return self.value  # 返回保存在描述符实例上的值

    def __set__(self, obj, value):  # 定义赋值时的钩子方法
        print(f"设置 {obj!r}.attr = {value!r}")  # 打印赋值日志信息
        self.value = value  # 把值保存到描述符实例本身


class Point:  # 定义使用描述符的类
    x = Verbose_attribute()  # 把描述符实例作为类属性 x
    y = Verbose_attribute()  # 把描述符实例作为类属性 y

p = Point()  # 创建 Point 实例
p.x = 10        # 触发 __set__  # 给 x 赋值会调用描述符的 __set__
print(p.x)       # 触发 __get__  # 读取 x 会调用描述符的 __get__


# ===== 2. 数据描述符 vs 非数据描述符 =====
print("\n--- 数据描述符 ---")  # 打印本节标题,前加换行
class Validated:  # 定义带类型校验的描述符类
    """带类型校验的描述符"""  # 文档字符串
    def __init__(self, name, type_, min_=None, max_=None):  # 初始化方法,接收字段名、类型和范围
        self.name = name  # 保存字段名
        self.type = type_  # 保存期望的类型
        self.min = min_  # 保存最小值限制
        self.max = max_  # 保存最大值限制

    def __get__(self, obj, objtype=None):  # 定义读取钩子
        if obj is None:  # 如果通过类访问而不是实例
            return self  # 返回描述符本身
        return obj.__dict__[self.name]  # 从实例字典中取出真实值

    def __set__(self, obj, value):  # 定义赋值钩子
        if not isinstance(value, self.type):  # 检查类型是否匹配
            raise TypeError(f"{self.name} 必须是 {self.type.__name__}")  # 类型不符则抛异常
        if self.min is not None and value < self.min:  # 若设了最小值且小于它
            raise ValueError(f"{self.name} 不能小于 {self.min}")  # 抛出值错误
        if self.max is not None and value > self.max:  # 若设了最大值且大于它
            raise ValueError(f"{self.name} 不能大于 {self.max}")  # 抛出值错误
        obj.__dict__[self.name] = value  # 校验通过后存入实例字典


class Person:  # 定义使用校验描述符的类
    name = Validated("name", str)  # name 字段必须是字符串
    age = Validated("age", int, min_=0, max_=150)  # age 字段必须是 0~150 的整数

p = Person()  # 创建 Person 实例
p.name = "Tom"  # 赋值合法字符串
p.age = 18  # 赋值合法年龄
print(f"{p.name}, {p.age}岁")  # 打印属性值

try:  # 尝试执行可能出错的代码
    p.age = -1  # 赋非法年龄触发校验
except ValueError as e:  # 捕获值错误
    print("校验失败:", e)  # 打印错误信息


# ===== 3. property 的本质 =====
print("\n--- property 源码精神 ---")  # 打印本节标题
# property 实际上就是实现了描述符协议的类
class MyProperty:  # 模仿内置 property 的类
    def __init__(self, fget=None, fset=None, fdel=None):  # 接收可选的取值、赋值、删除函数
        self.fget = fget  # 保存取值函数
        self.fset = fset  # 保存赋值函数
        self.fdel = fdel  # 保存删除函数

    def __get__(self, obj, objtype=None):  # 定义取值钩子
        if obj is None: return self  # 类访问时返回自身
        if self.fget is None: raise AttributeError  # 没有取值函数则报错
        return self.fget(obj)  # 调用取值函数返回结果

    def __set__(self, obj, value):  # 定义赋值钩子
        if self.fset is None: raise AttributeError  # 没有赋值函数则报错
        self.fset(obj, value)  # 调用赋值函数

    def setter(self, fset):  # 装饰器方法,用于注册赋值函数
        self.fset = fset  # 保存赋值函数
        return self  # 返回自身以支持链式调用


class Circle:  # 定义圆类
    def __init__(self, r):  # 初始化方法,接收半径
        self._r = r  # 把半径保存到私有属性

    @MyProperty  # 用自定义 property 装饰 radius 方法
    def radius(self):  # 定义取值方法
        return self._r  # 返回半径

    @radius.setter  # 注册赋值函数
    def radius(self, v):  # 定义赋值方法
        if v < 0: raise ValueError  # 半径不能为负
        self._r = v  # 更新半径


c = Circle(5)  # 创建半径为 5 的圆
print(f"半径={c.radius}")  # 读取半径(触发 __get__)
c.radius = 10  # 修改半径(触发 __set__)
print(f"新半径={c.radius}")  # 再次读取半径


# ===== 4. 实用:ORM 风格字段 =====
print("\n--- 字段描述符 ---")  # 打印本节标题
class Field:  # 定义 ORM 风格的字段描述符
    def __init__(self, type_, default=None):  # 接收类型和默认值
        self.type = type_  # 保存字段类型
        self.default = default  # 保存默认值
        self.name = None   # 由 __set_name__ 自动注入  # 字段名占位

    def __set_name__(self, owner, name):  # 解释器自动调用,告知字段名
        self.name = name  # 记录字段名

    def __get__(self, obj, objtype=None):  # 定义取值钩子
        if obj is None: return self  # 类访问返回描述符
        return obj.__dict__.get(self.name, self.default)  # 返回值或默认值

    def __set__(self, obj, value):  # 定义赋值钩子
        if not isinstance(value, self.type) and value is not None:  # 非空且类型不符
            raise TypeError(f"{self.name} 必须是 {self.type.__name__}")  # 抛类型错误
        obj.__dict__[self.name] = value  # 存入实例字典


class Model:  # 定义模型基类
    def __init__(self, **kwargs):  # 接收关键字参数
        for k, v in kwargs.items():  # 遍历每个键值对
            setattr(self, k, v)  # 动态设置属性(触发描述符)

    def __repr__(self):  # 定义对象的字符串表示
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())  # 拼接属性信息
        return f"{self.__class__.__name__}({attrs})"  # 返回类名加属性列表


class User(Model):  # 定义 User 模型继承 Model
    name = Field(str)  # name 字段为字符串
    age = Field(int, default=0)  # age 字段为整数,默认 0

u = User(name="Tom", age=18)  # 创建 User 实例
print(u)  # 打印对象(调用 __repr__)
u.age = 20  # 修改 age
print(u)  # 再次打印


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 用描述符实现一个 lazyproperty(只计算一次)")  # 练习题 1
    print("2. 用描述符实现 Positive 类型,只能赋值正数")  # 练习题 2
    print("3. 模仿 SQLAlchemy 实现一个 Field 体系,支持 String/Integer/DateTime")  # 练习题 3
