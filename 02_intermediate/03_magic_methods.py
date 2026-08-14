"""03 - 魔术方法

学习目标:
    - 掌握常用魔术方法(魔法方法)
    - 学会让自定义类支持内置操作
    - 实现运算符重载
"""


class Vector:  # 定义 Vector 类,演示运算符重载
    """演示运算符重载"""
    def __init__(self, x, y):  # 构造方法,接收 x 和 y 坐标
        self.x, self.y = x, y  # 同时保存 x 和 y 到实例属性

    def __repr__(self):  # 定义 __repr__,用于开发调试时的正式字符串表示
        return f"Vector({self.x}, {self.y})"  # 返回可重建对象的字符串

    def __str__(self):  # 定义 __str__,用于 print 等场合的用户友好字符串
        return f"({self.x}, {self.y})"  # 返回简洁的坐标表示

    # 算术运算
    def __add__(self, other):  # 定义 + 运算符的行为
        return Vector(self.x + other.x, self.y + other.y)  # 返回两向量相加的新向量

    def __sub__(self, other):  # 定义 - 运算符的行为
        return Vector(self.x - other.x, self.y - other.y)  # 返回两向量相减的新向量

    def __mul__(self, scalar):  # 定义 * 运算符的行为(向量 × 标量)
        return Vector(self.x * scalar, self.y * scalar)  # 返回向量各分量乘以标量的新向量

    def __rmul__(self, scalar):  # 右乘
        return self.__mul__(scalar)  # 当标量在左边时(如 3*v)调用,直接复用 __mul__

    def __neg__(self):  # 定义一元负号 - 运算符的行为
        return Vector(-self.x, -self.y)  # 返回各分量取反的新向量

    # 比较
    def __eq__(self, other):  # 定义 == 运算符的行为
        return self.x == other.x and self.y == other.y  # 两向量分量都相等则相等

    def __lt__(self, other):  # 定义 < 运算符的行为
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)  # 按向量长度(模的平方)比较大小

    def __hash__(self):  # 定义哈希值,使实例可作为字典键或集合元素
        return hash((self.x, self.y))  # 用坐标元组的哈希值作为实例的哈希值

    # 长度 / 迭代
    def __len__(self):  # 定义 len() 函数的行为
        return 2  # 向量有 x、y 两个分量,返回 2

    def __iter__(self):  # 定义迭代行为,使实例可被 for 循环遍历
        yield self.x  # 先产出 x 分量
        yield self.y  # 再产出 y 分量

    def __getitem__(self, index):  # 定义索引访问 v[i] 的行为
        if index == 0: return self.x  # 索引 0 返回 x
        if index == 1: return self.y  # 索引 1 返回 y
        raise IndexError  # 其他索引抛出越界异常


print("--- Vector 运算 ---")  # 打印分隔标题,演示 Vector 运算
v1 = Vector(1, 2)  # 创建向量 v1 (1,2)
v2 = Vector(3, 4)  # 创建向量 v2 (3,4)
print(f"v1={v1!r}, v2={v2!r}")  # 用 !r 调用 __repr__ 打印两个向量
print(f"v1 + v2 = {v1 + v2}")  # 打印两向量相加结果
print(f"v1 - v2 = {v1 - v2}")  # 打印两向量相减结果
print(f"v1 * 3 = {v1 * 3}")  # 打印向量乘以标量的结果
print(f"3 * v1 = {3 * v1}")  # 打印标量乘以向量的结果(触发 __rmul__)
print(f"-v1 = {-v1}")  # 打印向量取反结果
print(f"v1 == Vector(1, 2): {v1 == Vector(1, 2)}")  # 打印两向量是否相等
print(f"len(v1) = {len(v1)}")  # 打印向量长度(分量个数)
print(f"list(v1) = {list(v1)}")  # 把向量转成列表打印
print(f"v1[0] = {v1[0]}")  # 打印向量第 0 个分量


# ===== 上下文管理器魔术方法 =====
print("\n--- 上下文管理器 ---")  # 打印分隔标题,演示上下文管理器
class Timer:  # 定义 Timer 类,用 with 语句计时
    def __enter__(self):  # 进入 with 块时调用
        import time  # 导入 time 模块
        self._start = time.time()  # 记录开始时间
        return self  # 返回自身,作为 as 后面的对象

    def __exit__(self, exc_type, exc_val, exc_tb):  # 离开 with 块时调用,接收异常信息
        import time  # 导入 time 模块
        self._end = time.time()  # 记录结束时间
        print(f"耗时: {self._end - self._start:.4f}s")  # 打印总耗时(秒,保留4位小数)
        return False  # 不吞掉异常

with Timer():  # 进入计时上下文
    sum(range(1000000))  # 执行一段求和代码用于演示计时


# ===== 可调用对象 =====
print("\n--- __call__ ---")  # 打印分隔标题,演示可调用对象
class Multiplier:  # 定义 Multiplier 类,演示 __call__
    def __init__(self, factor):  # 构造方法,接收乘数因子
        self.factor = factor  # 保存因子到实例属性
    def __call__(self, x):  # 定义 __call__,使实例可像函数一样被调用
        return x * self.factor  # 返回 x 乘以因子的结果

double = Multiplier(2)  # 创建乘数为 2 的实例
print(f"double(5) = {double(5)}")  # 对象当函数用


# ===== 自定义容器 =====
print("\n--- 自定义容器 ---")  # 打印分隔标题,演示自定义容器
class Bag:  # 定义 Bag 类,演示自定义容器
    def __init__(self):  # 构造方法
        self._items = []  # 初始化空列表存储元素
    def add(self, item):  # 定义 add 方法,添加元素
        self._items.append(item)  # 把元素追加到内部列表
    def __len__(self):  # 定义 len() 行为
        return len(self._items)  # 返回元素数量
    def __iter__(self):  # 定义迭代行为
        return iter(self._items)  # 返回内部列表的迭代器
    def __contains__(self, item):  # 定义 in 运算符行为
        return item in self._items  # 判断元素是否在容器中
    def __getitem__(self, i):  # 定义索引访问行为
        return self._items[i]  # 返回指定索引的元素

bag = Bag()  # 创建 Bag 实例
bag.add("apple"); bag.add("banana")  # 添加两个元素:apple 和 banana
print(f"len={len(bag)}, 'apple' in bag: {'apple' in bag}")  # 打印长度和是否包含 apple
for x in bag:  # 遍历 bag 中的元素
    print(" ", x)  # 打印每个元素


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 实现一个 Fraction 类,支持 + - * / 和比较")  # 练习题 1
    print("2. 实现一个 Money 类,支持不同币种相加")  # 练习题 2
    print("3. 实现一个支持切片操作的自定义类")  # 练习题 3
