"""01 - 面向对象基础

学习目标:
    - 掌握类与对象
    - 理解 __init__、实例属性、类属性
    - 掌握实例方法、类方法、静态方法
    - 了解封装
"""


class Dog:  # 定义一个名为 Dog 的类,用于演示面向对象基础
    """Dog 类示例 - 演示基本面向对象"""

    # 类属性(所有实例共享)
    species = "Canis familiaris"  # 类属性,所有 Dog 实例共享的物种名
    count = 0  # 类属性,记录已创建的 Dog 实例数量,初始为 0

    def __init__(self, name: str, age: int, breed: str = "混血"):  # 构造方法,创建实例时自动调用
        # 实例属性
        self.name = name  # 实例属性,存储狗的名字
        self.age = age  # 实例属性,存储狗的年龄
        self.breed = breed  # 实例属性,存储狗的品种,默认为"混血"
        self._secret = "受保护的"    # 约定:下划线开头表示"内部使用"
        self.__really_secret = "私有的"  # 名称修饰,实际为 _Dog__really_secret
        Dog.count += 1  # 每创建一个实例,类属性 count 加 1

    # 实例方法
    def bark(self):  # 定义实例方法 bark,模拟狗叫
        return f"{self.name} 在汪汪叫"  # 返回狗叫的描述字符串

    def info(self):  # 定义实例方法 info,返回狗的简介
        return f"{self.name} ({self.breed}, {self.age}岁)"  # 返回包含名字、品种、年龄的字符串

    # 类方法:通过类调用,可访问/修改类属性
    @classmethod
    def total(cls):  # 定义类方法 total,cls 参数代表类本身
        return f"共创建了 {cls.count} 只狗"  # 返回已创建的狗的总数

    @classmethod
    def from_string(cls, s: str):  # 定义类方法 from_string,作为工厂方法从字符串创建对象
        """工厂方法:从字符串创建对象"""
        name, age, breed = s.split(",")  # 用逗号分割字符串,得到名字、年龄、品种
        return cls(name, int(age), breed)  # 用解析出的参数创建并返回实例

    # 静态方法:不依赖实例或类
    @staticmethod
    def is_old(age: int) -> bool:  # 定义静态方法 is_old,判断年龄是否算老
        return age > 10  # 年龄大于 10 视为老狗,返回布尔值


# ===== 使用示例 =====
print("--- 创建对象 ---")  # 打印分隔标题,表示开始演示创建对象
d1 = Dog("旺财", 3, "柴犬")  # 创建 Dog 实例 d1,名字旺财、3 岁、品种柴犬
d2 = Dog("小黑", 5)  # 创建 Dog 实例 d2,名字小黑、5 岁,品种用默认值"混血"
print(d1.info())  # 打印 d1 的简介信息
print(d2.bark())  # 打印 d2 的叫声描述

# 访问类属性
print(f"物种: {Dog.species}")  # 通过类名访问类属性 species 并打印
print(f"实例访问类属性: {d1.species}")  # 通过实例也能访问类属性 species

# 修改类属性(通过类修改,所有实例可见)
Dog.species = "Canis lupus familiaris"  # 通过类名修改类属性 species 的值
print(f"修改后: {d1.species}")  # 打印修改后 d1 看到的 species,验证所有实例都可见

# 类方法
print(Dog.total())  # 通过类名调用类方法 total,打印已创建的狗的总数
d3 = Dog.from_string("球球,2,柯基")  # 用工厂方法从字符串创建实例 d3
print(d3.info())  # 打印 d3 的简介信息

# 静态方法
print(f"15 岁算老狗吗? {Dog.is_old(15)}")  # 调用静态方法判断 15 岁是否算老狗并打印

# 私有属性(不能直接访问)
try:  # 尝试执行下面可能出错的代码
    print(d1.__really_secret)  # 尝试直接访问私有属性(会失败)
except AttributeError as e:  # 捕获属性不存在异常
    print(f"无法直接访问私有属性: {e}")  # 打印异常提示信息
# 但可以通过名称修饰访问(不推荐)
print(f"绕过去访问: {d1._Dog__really_secret}")  # 通过名称修饰后的名字访问私有属性(不推荐使用)


# ===== property 装饰器 =====
print("\n--- property ---")  # 打印分隔标题,表示开始演示 property 装饰器
class Circle:  # 定义 Circle 类,演示 property 装饰器
    def __init__(self, radius: float):  # 构造方法,接收半径参数
        self._radius = radius  # 把半径存到受保护的实例属性 _radius 中

    @property  # 用 property 装饰器把方法变成属性访问
    def radius(self):  # 定义 radius 的 getter 方法
        return self._radius  # 返回 _radius 的值

    @radius.setter  # 为 radius 属性添加 setter 方法
    def radius(self, value):  # 定义 setter,接收新值
        if value < 0:  # 如果新值小于 0
            raise ValueError("半径不能为负")  # 抛出异常,禁止负半径
        self._radius = value  # 合法则更新 _radius

    @property  # 把 area 定义为只读属性
    def area(self):  # 定义 area 方法,计算圆的面积
        return 3.14159 * self._radius ** 2  # 用公式 πr² 计算并返回面积

c = Circle(5)  # 创建 Circle 实例,半径为 5
print(f"半径={c.radius}, 面积={c.area:.2f}")  # 打印半径和面积(面积保留两位小数)
c.radius = 10  # 通过 setter 修改半径为 10
print(f"新面积={c.area:.2f}")  # 打印修改半径后的新面积


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 创建一个 BankAccount 类,支持存款/取款/查询余额")  # 练习题 1
    print("2. 用 property 实现一个温度类,支持摄氏和华氏的自动转换")  # 练习题 2
    print("3. 创建一个 Student 类,用类方法统计班级总人数")  # 练习题 3
