"""06 - 上下文管理器

学习目标:
    - 掌握 with 语句原理
    - 学会 @contextmanager 装饰器
    - 自定义上下文管理器类
    - 了解 ExitStack
"""

import time  # 导入 time 模块,用于计时
from contextlib import contextmanager, ExitStack  # 导入 contextmanager 装饰器和 ExitStack 工具
from pathlib import Path  # 导入 Path 类,用于路径操作


# ===== 1. 基于类的上下文管理器 =====
print("--- 类实现 ---")  # 打印分隔标题,演示基于类的上下文管理器
class FileOpener:  # 定义 FileOpener 类,实现文件上下文管理
    def __init__(self, path, mode="r", encoding="utf-8"):  # 构造方法,接收路径、模式、编码
        self.path = path  # 保存文件路径
        self.mode = mode  # 保存打开模式
        self.encoding = encoding  # 保存编码方式
        self.file = None  # 初始化文件对象为空

    def __enter__(self):  # 进入 with 块时调用
        print("打开文件")  # 打印提示
        self.file = open(self.path, self.mode, encoding=self.encoding)  # 打开文件
        return self.file  # 返回文件对象,作为 as 后的变量

    def __exit__(self, exc_type, exc_val, exc_tb):  # 离开 with 块时调用,接收异常信息
        print("关闭文件")  # 打印提示
        if self.file:  # 如果文件对象存在
            self.file.close()  # 关闭文件
        # 返回 True 表示吞掉异常;False/None 表示不处理
        return False  # 返回 False,不吞掉异常


tmp = Path("demo.txt")  # 创建表示 demo.txt 的 Path 对象
tmp.write_text("Hello Context Manager", encoding="utf-8")  # 写入文本到临时文件
with FileOpener(tmp) as f:  # 用 FileOpener 打开文件
    print("内容:", f.read())  # 读取并打印文件内容
tmp.unlink()  # 删除临时文件


# ===== 2. @contextmanager 装饰器(更简洁) =====
print("\n--- @contextmanager ---")  # 打印分隔标题,演示装饰器方式
@contextmanager  # 用 contextmanager 装饰器把生成器函数变成上下文管理器
def timer(label="block"):  # 定义计时上下文管理器,可带标签
    start = time.time()  # 记录开始时间
    print(f"[{label}] 开始")  # 打印开始提示
    try:  # 用 try/finally 确保结束时执行清理
        yield  # yield 之前是 __enter__ 的代码,yield 处是 with 块执行点
    finally:  # 无论是否异常都会执行
        print(f"[{label}] 结束,耗时 {time.time() - start:.4f}s")  # 打印结束提示和耗时

with timer("test"):  # 用 timer 上下文管理器
    time.sleep(0.05)  # 休眠 0.05 秒模拟工作


# ===== 3. 实用示例:临时修改工作目录 =====
print("\n--- 临时切换目录 ---")  # 打印分隔标题,演示临时切换工作目录
@contextmanager  # 用 contextmanager 装饰
def change_dir(path):  # 定义临时切换目录的上下文管理器
    """临时切换工作目录,退出时自动恢复"""
    import os  # 导入 os 模块
    original = os.getcwd()  # 保存当前工作目录
    os.chdir(path)  # 切换到新目录
    try:  # try/finally 确保恢复
        yield  # 在新目录中执行 with 块
    finally:  # 退出时恢复
        os.chdir(original)  # 切回原工作目录

with change_dir(".."):  # 临时切换到上级目录
    print("当前目录:", Path.cwd().name)  # 打印当前所在目录名
print("恢复后:", Path.cwd().name)  # 打印恢复后的目录名


# ===== 4. 资源池:数据库连接 =====
print("\n--- 资源池示例 ---")  # 打印分隔标题,演示连接池
class ConnectionPool:  # 定义连接池类
    def __init__(self, size):  # 构造方法,接收池大小
        self._pool = [f"conn-{i}" for i in range(size)]  # 初始化连接列表
        self._used = set()  # 用集合记录已使用的连接

    @contextmanager  # 把 acquire 方法变成上下文管理器
    def acquire(self):  # 定义获取连接的方法
        if not self._pool:  # 如果池空
            raise RuntimeError("无可用连接")  # 抛出异常
        conn = self._pool.pop()  # 从池中取出一个连接
        self._used.add(conn)  # 标记为已使用
        try:  # try/finally 确保归还
            yield conn  # 把连接交给 with 块使用
        finally:  # 退出时归还连接
            self._used.discard(conn)  # 从已用集合移除
            self._pool.append(conn)  # 放回池中

pool = ConnectionPool(3)  # 创建大小为 3 的连接池
with pool.acquire() as c1:  # 获取连接 c1
    print("拿到:", c1)  # 打印拿到的连接
    with pool.acquire() as c2:  # 嵌套获取连接 c2
        print("拿到:", c2)  # 打印拿到的连接
print("归还后剩余:", pool._pool)  # 打印归还后池中剩余的连接


# ===== 5. ExitStack:动态管理多个上下文 =====
print("\n--- ExitStack ---")  # 打印分隔标题,演示 ExitStack
def merge_files(*paths):  # 定义合并多个文件的函数
    """合并多个文件的内容,自动关闭所有文件"""
    with ExitStack() as stack:  # 创建 ExitStack 上下文管理器
        files = [stack.enter_context(open(p, encoding="utf-8")) for p in paths]  # 把所有打开的文件加入栈,统一管理关闭
        return "".join(f.read() for f in files)  # 读取所有文件内容并拼接返回

# 演示
tmp1 = Path("a.txt"); tmp1.write_text("Hello ", encoding="utf-8")  # 创建临时文件 a.txt
tmp2 = Path("b.txt"); tmp2.write_text("World!", encoding="utf-8")  # 创建临时文件 b.txt
print(merge_files(tmp1, tmp2))  # 合并并打印两个文件内容
tmp1.unlink(); tmp2.unlink()  # 删除两个临时文件


# ===== 6. 抑制特定异常 =====
print("\n--- suppress ---")  # 打印分隔标题,演示 suppress
from contextlib import suppress  # 导入 suppress 上下文管理器

# 替代 try/except PASS
with suppress(FileNotFoundError):  # 抑制 FileNotFoundError 异常
    Path("nope.txt").unlink()  # 尝试删除不存在的文件,异常被抑制
print("不存在文件删除已忽略")  # 打印提示


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 实现一个 HTML 标签上下文管理器(进入时输出开始标签,退出时输出结束标签)")  # 练习题 1
    print("2. 实现一个 Lock 互斥锁上下文管理器(基于 threading.Lock)")  # 练习题 2
    print("3. 用 ExitStack 写一个同时打开多个 URL 的工具")  # 练习题 3
