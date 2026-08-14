"""练习 3:依赖注入容器

题目描述:
    实现一个简单的 IoC 容器:
    - 注册接口到具体实现
    - 自动解析依赖(根据类型注解)
    - 支持单例和瞬态(transient)两种生命周期
    - 容器可以嵌套,子容器继承父容器的注册

提示:
    - 使用 inspect.signature 获取函数参数
    - 用 __annotations__ 读取类型提示
"""

import inspect  # 导入 inspect 模块用于检查签名
from typing import get_type_hints  # 导入获取类型提示的函数


class Container:  # 定义依赖注入容器类
    def __init__(self, parent=None):  # 初始化方法,可指定父容器
        self.parent = parent  # 保存父容器
        self._registry: dict = {}    # type -> (factory, lifetime)  # 注册表:类型 -> (实现, 是否单例)

    def register(self, interface, implementation=None, singleton=True):  # 注册接口到实现
        """注册接口到实现。implementation 默认就是 interface 本身"""  # 方法说明
        if implementation is None:  # 如果没传实现
            implementation = interface  # 实现就是接口本身
        self._registry[interface] = (implementation, singleton)  # 保存到注册表
        return self  # 返回自身以支持链式调用

    def resolve(self, interface):  # 解析接口返回实例
        if interface in self._registry:  # 如果本容器注册了
            impl, singleton = self._registry[interface]  # 取出实现和生命周期
            if singleton and not hasattr(impl, "_instance"):  # 单例且未创建过
                impl._instance = self._create(impl)  # 创建并缓存实例
            return impl._instance if singleton else self._create(impl)  # 单例返回缓存,否则新建

        if self.parent:  # 本容器没注册但有父容器
            return self.parent.resolve(interface)  # 委托给父容器解析

        raise KeyError(f"未注册: {interface.__name__}")  # 都没有则抛出错误

    def _create(self, cls):  # 创建实例并自动注入依赖
        """根据类型注解自动注入依赖"""  # 方法说明
        try:  # 尝试获取类型提示
            hints = get_type_hints(cls.__init__)  # 读取 __init__ 的类型注解
        except Exception:  # 出错时
            hints = {}  # 用空字典
        params = inspect.signature(cls.__init__).parameters  # 获取参数列表
        kwargs = {}  # 用于保存要注入的参数
        for name, param in params.items():  # 遍历每个参数
            if name == "self":  # 跳过 self
                continue  # 继续
            if name in hints:  # 如果该参数有类型注解
                dep = hints[name]  # 取出依赖类型
                kwargs[name] = self.resolve(dep)  # 递归解析依赖
        return cls(**kwargs)  # 用注入的参数创建实例


# ===== 演示:一个应用 =====
class Logger:  # 日志类
    def log(self, msg):  # 日志方法
        print(f"  [LOG] {msg}")  # 打印日志


class Database:  # 数据库类
    def __init__(self, logger: Logger):  # 构造函数依赖 Logger
        self.logger = logger  # 保存日志器
    def query(self, sql):  # 查询方法
        self.logger.log(f"执行查询: {sql}")  # 记录日志
        return [{"id": 1, "name": "Tom"}]  # 返回模拟结果


class UserService:  # 用户服务类
    def __init__(self, db: Database, logger: Logger):  # 依赖 Database 和 Logger
        self.db = db  # 保存数据库
        self.logger = logger  # 保存日志器
    def list_users(self):  # 列出用户方法
        self.logger.log("UserService.list_users")  # 记录日志
        return self.db.query("SELECT * FROM users")  # 调用数据库查询


if __name__ == "__main__":  # 直接运行本文件时执行
    # 配置容器
    container = Container()  # 创建容器
    container.register(Logger, singleton=True)  # 注册 Logger 为单例
    container.register(Database)  # 注册 Database
    container.register(UserService)  # 注册 UserService

    # 解析
    service = container.resolve(UserService)  # 解析 UserService(自动注入依赖)
    print(service.list_users())  # 调用方法并打印结果

    # 单例验证
    l1 = container.resolve(Logger)  # 解析 Logger
    l2 = container.resolve(Logger)  # 再次解析 Logger
    print(f"Logger 单例: {l1 is l2}")  # 验证是否为同一实例

    # 子容器
    child = Container(parent=container)  # 创建子容器,父容器为 container
    child.register(UserService)   # 覆盖  # 子容器重新注册 UserService
    s1 = container.resolve(UserService)  # 父容器解析
    s2 = child.resolve(UserService)  # 子容器解析
    print(f"父子容器实例不同: {s1 is not s2}")  # 验证两个实例不同
