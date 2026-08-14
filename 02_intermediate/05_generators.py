"""05 - 生成器与迭代器

学习目标:
    - 理解迭代器协议
    - 掌握 yield 关键字
    - 学会 send / throw / close
    - 了解 yield from
"""


# ===== 1. 迭代器协议 =====
print("--- 迭代器协议 ---")  # 打印分隔标题,演示迭代器协议
class CountDown:  # 定义 CountDown 类,实现迭代器协议
    def __init__(self, start):  # 构造方法,接收起始数字
        self.n = start  # 把起始数字保存到实例属性 n
    def __iter__(self):  # 实现 __iter__,返回迭代器本身
        return self  # 返回自身,因为本类既是可迭代对象也是迭代器
    def __next__(self):  # 实现 __next__,返回下一个值
        if self.n <= 0:  # 如果计数到 0 或以下
            raise StopIteration  # 抛出 StopIteration 表示迭代结束
        self.n -= 1  # 计数减 1
        return self.n + 1  # 返回减 1 之前的值(倒序输出)

for i in CountDown(3):  # 用 for 循环遍历 CountDown 实例
    print(" ", i)  # 打印每个值


# ===== 2. 生成器函数 =====
print("\n--- 生成器函数 ---")  # 打印分隔标题,演示生成器函数
def fib_gen(limit):  # 定义生成器函数,生成不超过 limit 的斐波那契数
    a, b = 0, 1  # 初始化前两个斐波那契数
    while a < limit:  # 当 a 小于上限时循环
        yield a  # 产出当前斐波那契数 a
        a, b = b, a + b  # 同时更新 a 和 b:a 变成 b,b 变成 a+b

for n in fib_gen(100):  # 遍历生成器产出的斐波那契数
    print(" ", n, end="")  # 打印数值,不换行
print()  # 打印换行


# ===== 3. 生成器表达式 =====
print("\n--- 生成器表达式 ---")  # 打印分隔标题,演示生成器表达式
# 节省内存,惰性求值
sum_sq = sum(x * x for x in range(1000000))  # 用生成器表达式计算 0~999999 的平方和
print(f"平方和: {sum_sq}")  # 打印平方和


# ===== 4. send / throw / close =====
print("\n--- 协程式生成器 ---")  # 打印分隔标题,演示带 send 的协程式生成器
def accumulator():  # 定义累加器生成器
    total = 0  # 初始化总和为 0
    while True:  # 无限循环
        value = yield total        # 既能产出,也能接收值
        if value is None:  # 如果收到的值是 None
            break  # 退出循环
        total += value  # 把收到的值累加到总和

acc = accumulator()  # 创建生成器对象
next(acc)            # 必须先启动到第一个 yield
print(acc.send(10))   # 10
print(acc.send(20))   # 30
print(acc.send(5))    # 35
acc.close()  # 关闭生成器,释放资源


# ===== 5. yield from =====
print("\n--- yield from ---")  # 打印分隔标题,演示 yield from 委托
def sub_gen():  # 定义子生成器
    yield 1  # 产出 1
    yield 2  # 产出 2
    yield 3  # 产出 3

def main_gen():  # 定义主生成器
    yield "start"  # 先产出 "start"
    yield from sub_gen()    # 委托给子生成器
    yield "end"  # 最后产出 "end"

for v in main_gen():  # 遍历主生成器产出的所有值
    print(" ", v)  # 打印每个值


# ===== 6. 实用案例:大文件逐行处理 =====
print("\n--- 大文件处理 ---")  # 打印分隔标题,演示大文件分块读取
def read_in_chunks(path, chunk_size=1024):  # 定义按块读文件的生成器
    """按块读取大文件"""
    with open(path, "r", encoding="utf-8") as f:  # 以 UTF-8 编码打开文件
        while True:  # 无限循环
            chunk = f.read(chunk_size)  # 读取一块数据
            if not chunk:  # 如果读不到数据
                break  # 退出循环
            yield chunk  # 产出这一块数据


# 演示:写一个临时文件
import tempfile, os  # 导入 tempfile 和 os 模块
with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt", encoding="utf-8") as f:  # 创建临时文件
    for i in range(1000):  # 循环 1000 次
        f.write(f"line {i}\n")  # 每次写一行
    tmp_path = f.name  # 保存临时文件路径

# 逐块处理
total_lines = sum(chunk.count("\n") for chunk in read_in_chunks(tmp_path, 4096))  # 统计所有块的换行符总数
print(f"总行数: {total_lines}")  # 打印总行数
os.unlink(tmp_path)  # 删除临时文件


# ===== 7. itertools 速查 =====
print("\n--- itertools ---")  # 打印分隔标题,演示 itertools 常用函数
import itertools  # 导入 itertools 模块

# count, cycle, repeat
counter = itertools.count(10, 2)        # 10, 12, 14, ...
print("count:", [next(counter) for _ in range(5)])  # 取前 5 个值打印

# chain:连接多个迭代器
print("chain:", list(itertools.chain([1, 2], (3, 4), "ab")))  # 把列表、元组、字符串串联成一个列表

# combinations / permutations
print("combinations:", list(itertools.combinations([1, 2, 3], 2)))  # 列出所有 2 元组合(无序)
print("permutations:", list(itertools.permutations([1, 2, 3], 2)))  # 列出所有 2 元排列(有序)

# groupby
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]  # 准备按首元素分组的数据
for key, group in itertools.groupby(data, key=lambda x: x[0]):  # 按元组第一个元素分组
    print(f"  {key}: {[v for _, v in group]}")  # 打印每组键和对应的值列表


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 实现一个生成器,产出所有素数(无限序列)")  # 练习题 1
    print("2. 用 yield from 实现一个递归遍历树结构的生成器")  # 练习题 2
    print("3. 用 itertools 实现一个分页器")  # 练习题 3
