"""练习 1:实现一个简单的 ORM

题目描述:
    不用 SQLAlchemy,自己实现一个迷你 ORM:
    - 字段描述符:Integer / String / Float
    - 基类 Model,支持 save() / delete() / find() / all()
    - 用字典模拟存储(内存数据库)

要求:
    - 用描述符定义字段类型
    - 用元类自动收集字段
    - 字段支持类型校验

进阶:
    - 加上 update / count / where 查询
"""

from typing import Any  # 导入任意类型
from datetime import datetime  # 导入日期时间类型(预留)


# ===== 字段描述符 =====
class Field:  # 定义字段基类(描述符)
    def __init__(self, type_, required=True, default=None):  # 初始化方法
        self.type = type_  # 保存期望类型
        self.required = required  # 是否必填
        self.default = default  # 默认值
        self.name = None  # 字段名,由 __set_name__ 注入

    def __set_name__(self, owner, name):  # 解释器自动调用,告知字段名
        self.name = name  # 保存字段名

    def __get__(self, obj, objtype=None):  # 取值钩子
        if obj is None: return self  # 类访问返回描述符
        return obj.__dict__.get(self.name, self.default)  # 返回值或默认值

    def __set__(self, obj, value):  # 赋值钩子
        if value is None:  # 如果赋值为 None
            if self.required and self.default is None:  # 必填且无默认值
                raise ValueError(f"{self.name} 是必填字段")  # 抛出错误
            obj.__dict__[self.name] = None  # 存为 None
            return  # 结束
        if not isinstance(value, self.type):  # 类型不符
            try:  # 尝试类型转换
                value = self.type(value)  # 转换为目标类型
            except (ValueError, TypeError):  # 转换失败
                raise TypeError(f"{self.name} 类型错误,期望 {self.type.__name__}")  # 抛类型错误
        obj.__dict__[self.name] = value  # 存入实例字典


class IntegerField(Field):  # 整数字段类
    def __init__(self, **kwargs): super().__init__(int, **kwargs)  # 固定类型为 int

class StringField(Field):  # 字符串字段类
    def __init__(self, max_length=None, **kwargs):  # 接收最大长度
        super().__init__(str, **kwargs)  # 固定类型为 str
        self.max_length = max_length  # 保存最大长度
    def __set__(self, obj, value):  # 重写赋值钩子
        super().__set__(obj, value)  # 先调用父类赋值
        if value is not None and self.max_length and len(value) > self.max_length:  # 非空且超长
            raise ValueError(f"{self.name} 不能超过 {self.max_length} 字符")  # 抛出错误


# ===== 元类 =====
class ModelMeta(type):  # 定义模型元类
    def __new__(mcs, name, bases, namespace):  # 创建类时拦截
        # 收集字段
        fields = {}  # 用于保存字段
        for key, value in list(namespace.items()):  # 遍历命名空间
            if isinstance(value, Field):  # 如果是 Field 实例
                fields[key] = value  # 收集到字典
        namespace["_fields"] = fields  # 把字段字典存到类的 _fields 属性
        return super().__new__(mcs, name, bases, namespace)  # 创建类


# ===== 基类 =====
class Model(metaclass=ModelMeta):  # 模型基类,使用 ModelMeta 元类
    _storage: dict = {}    # 类级存储:{类名: [实例, ...]}  # 内存数据库

    def __init__(self, **kwargs):  # 初始化方法
        for f in self._fields.values():  # 遍历所有字段
            if f.name in kwargs:  # 如果传入了该字段
                setattr(self, f.name, kwargs[f.name])  # 设置字段值
            else:
                # 使用默认值
                setattr(self, f.name, f.default)  # 用默认值

    def save(self):  # 保存方法
        storage = self._storage.setdefault(self.__class__.__name__, [])  # 取出该类的存储列表
        # 检查是否已存在(根据内存地址)
        if self not in storage:  # 如果不在存储中
            storage.append(self)  # 添加进去
        return self  # 返回自身以便链式调用

    def delete(self):  # 删除方法
        storage = self._storage.get(self.__class__.__name__, [])  # 取出存储列表
        if self in storage:  # 如果在里面
            storage.remove(self)  # 移除

    def __repr__(self):  # 字符串表示
        attrs = ", ".join(f"{k}={getattr(self, k, None)!r}" for k in self._fields)  # 拼接字段信息
        return f"{self.__class__.__name__}({attrs})"  # 返回类名加字段


# ===== 使用示例 =====
class User(Model):  # 定义 User 模型
    id = IntegerField()  # id 字段为整数
    name = StringField(max_length=50)  # name 字段为字符串,最长 50
    age = IntegerField(default=0)  # age 字段为整数,默认 0

    @classmethod  # 类方法
    def find(cls, user_id):  # 根据 id 查找用户
        for u in cls._storage.get("User", []):  # 遍历存储
            if u.id == user_id:  # 找到匹配的 id
                return u  # 返回该用户
        return None  # 没找到返回 None

    @classmethod  # 类方法
    def all(cls):  # 获取所有用户
        return list(cls._storage.get("User", []))  # 返回列表副本


if __name__ == "__main__":  # 直接运行本文件时执行
    u1 = User(id=1, name="Tom", age=18).save()  # 创建并保存用户 1
    u2 = User(id=2, name="Jerry").save()  # 创建并保存用户 2
    print(u1)  # 打印用户 1
    print(u2)  # 打印用户 2
    print("所有用户:", User.all())  # 打印所有用户
    print("找到 id=1:", User.find(1))  # 查找 id=1

    # 类型校验
    try:  # 尝试触发类型错误
        User(id=3, name=123)  # name 传整数会报错
    except TypeError as e:  # 捕获类型错误
        print("校验:", e)  # 打印错误信息
