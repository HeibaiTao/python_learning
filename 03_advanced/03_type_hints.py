"""03 - 类型提示与静态检查

学习目标:
    - 掌握 typing 模块
    - 学会使用 mypy 做静态检查
    - 了解泛型、协变、逆变
"""

from typing import (  # 从 typing 模块导入常用的类型工具
    Any, Optional, Union, List, Dict, Tuple, Set,  # 导入基础类型别名
    Callable, Iterable, Iterator, TypeVar, Generic,  # 导入可调用、可迭代、泛型相关
    NewType, Final, Literal, Annotated, Protocol  # 导入新类型、常量、字面量、注解、协议
)
from dataclasses import dataclass  # 导入数据类装饰器


# ===== 1. 基本类型注解 =====
print("--- 基本注解 ---")  # 打印本节标题
def add(a: int, b: int) -> int:  # 定义函数,参数和返回值都标注为 int
    return a + b  # 返回两数之和

x: int = 10  # 声明变量 x 为 int 类型并赋值
name: str = "Tom"  # 声明变量 name 为 str 类型并赋值
items: list[int] = [1, 2, 3]            # Python 3.9+  # 声明列表元素为 int
mapping: dict[str, int] = {"a": 1}  # 声明字典键为 str,值为 int


# ===== 2. Optional / Union =====
print("\n--- Optional / Union ---")  # 打印本节标题
def find_user(user_id: int) -> Optional[dict]:  # 返回值为 dict 或 None
    """找不到时返回 None"""  # 函数说明
    if user_id <= 0:  # 如果 ID 不合法
        return None  # 返回 None
    return {"id": user_id, "name": "Tom"}  # 返回用户字典

# Union[A, B, C] 相当于 A | B | C
def parse(value: str) -> Union[int, float, str]:  # 返回值可能是 int、float 或 str
    try:  # 尝试转为整数
        return int(value)  # 转换成功返回整数
    except ValueError:  # 转整数失败
        try:  # 再尝试转为浮点数
            return float(value)  # 转换成功返回浮点数
        except ValueError:  # 转浮点也失败
            return value  # 返回原始字符串


# ===== 3. Callable =====
print("\n--- Callable ---")  # 打印本节标题
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:  # 接收一个 (int,int)->int 的函数
    return func(a, b)  # 调用传入的函数并返回结果

print(apply(lambda x, y: x + y, 3, 5))   # 8  # 传入加法 lambda,打印结果


# ===== 4. 泛型 =====
print("\n--- 泛型 ---")  # 打印本节标题
T = TypeVar("T")  # 定义类型变量 T
K = TypeVar("K")  # 定义类型变量 K
V = TypeVar("V")  # 定义类型变量 V

def first(items: List[T]) -> Optional[T]:  # 取列表第一个元素,类型与列表元素一致
    return items[0] if items else None  # 列表非空返回首元素,否则返回 None

def get_or_default(mapping: Dict[K, V], key: K, default: V) -> V:  # 字典取值,类型自动推导
    return mapping.get(key, default)  # 返回 key 对应的值或默认值


# ===== 5. 自定义泛型类 =====
print("\n--- 泛型类 ---")  # 打印本节标题
class Stack(Generic[T]):  # 定义泛型栈类,元素类型为 T
    def __init__(self) -> None:  # 初始化方法
        self._items: List[T] = []  # 内部用列表存储元素

    def push(self, item: T) -> None:  # 入栈方法,参数类型为 T
        self._items.append(item)  # 把元素追加到末尾

    def pop(self) -> T:  # 出栈方法,返回类型为 T
        return self._items.pop()  # 弹出并返回末尾元素

    def __len__(self) -> int:  # 支持len()函数
        return len(self._items)  # 返回元素个数


s = Stack[int]()  # 创建一个 int 类型的栈
s.push(1); s.push(2)  # 压入两个整数
print(f"栈大小: {len(s)}, 弹出: {s.pop()}")  # 打印栈大小和弹出值


# ===== 6. Protocol:结构化子类型 =====
print("\n--- Protocol ---")  # 打印本节标题
class Sized(Protocol):  # 定义协议类,只要实现了 __len__ 就算符合
    def __len__(self) -> int: ...  # 声明需要实现的方法

def total_size(items: list[Sized]) -> int:  # 接收符合 Sized 协议的对象列表
    return sum(len(x) for x in items)  # 累加每个对象的长度

# 任何有 __len__ 的对象都满足 Sized
print(total_size(["abc", [1, 2, 3], (4, 5, 6, 7)]))  # 打印字符串、列表、元组的长度总和


# ===== 7. Literal / Final / Annotated =====
print("\n--- Literal / Final / Annotated ---")  # 打印本节标题
MODE_DEBUG: Final = "debug"          # 常量  # 用 Final 声明不可变常量
def set_mode(mode: Literal["debug", "release"]) -> None:  # 参数只能是这两个字符串之一
    print(f"模式: {mode}")  # 打印当前模式

set_mode("debug")  # 调用函数传入合法字面量

# Annotated:附加元信息(供 IDE、mypy、pydantic 使用)
from typing import Annotated  # 再次导入 Annotated(演示用)
UserId = Annotated[int, "用户ID,正整数"]  # 给 int 类型附加说明信息


# ===== 8. dataclass + 类型提示 =====
print("\n--- dataclass ---")  # 打印本节标题
@dataclass(frozen=True)  # frozen=True 表示实例不可变
class Coordinate:  # 定义坐标类
    x: float  # x 坐标
    y: float  # y 坐标

    def distance(self, other: "Coordinate") -> float:  # 计算到另一个坐标的距离
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5  # 勾股定理


c1 = Coordinate(0, 0)  # 创建坐标 (0,0)
c2 = Coordinate(3, 4)  # 创建坐标 (3,4)
print(f"距离: {c1.distance(c2)}")  # 打印两点距离
# c1.x = 10   # frozen=True,不可修改  # 不可变实例不能修改属性


# ===== 9. 实战:TypedDict =====
print("\n--- TypedDict ---")  # 打印本节标题
from typing import TypedDict  # 导入 TypedDict

class UserDict(TypedDict):  # 定义带类型约束的字典
    id: int  # id 字段为 int
    name: str  # name 字段为 str
    email: str  # email 字段为 str

def process(u: UserDict) -> None:  # 处理用户字典的函数
    print(f"{u['id']}: {u['name']} <{u['email']}>")  # 打印用户信息

process({"id": 1, "name": "Tom", "email": "t@x.com"})  # 调用函数传入字典


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 为之前练习中的类补充完整类型提示")  # 练习题 1
    print("2. 用 mypy 检查你的项目(命令行:mypy your_module.py)")  # 练习题 2
    print("3. 用 Protocol 定义一个 Repository 接口")  # 练习题 3
