"""05 - 异步编程 asyncio

学习目标:
    - 理解 async/await 语法
    - 掌握 asyncio 核心 API
    - 学会异步上下文管理器
    - 了解 asyncio 任务并发
"""

import asyncio  # 导入异步编程标准库
import time  # 导入时间模块用于计时


# ===== 1. 基本协程 =====
print("--- 基本协程 ---")  # 打印本节标题
async def hello():  # 用 async 定义协程函数
    print("  Hello")  # 先打印 Hello
    await asyncio.sleep(0.1)  # 异步休眠 0.1 秒,不阻塞主线程
    print("  World")  # 休眠后打印 World

# Python 3.7+
asyncio.run(hello())  # 运行协程,自动创建和关闭事件循环


# ===== 2. awaitable 对象 =====
print("\n--- awaitable ---")  # 打印本节标题
async def slow_op(n):  # 定义返回值的协程
    await asyncio.sleep(0.1)  # 异步休眠
    return n * 2  # 返回参数的两倍

async def main():  # 定义主协程
    result = await slow_op(5)  # 等待 slow_op 返回结果
    print(f"  结果: {result}")  # 打印结果

asyncio.run(main())  # 运行主协程


# ===== 3. 任务并发(gather) =====
print("\n--- gather ---")  # 打印本节标题
async def fetch_data(i):  # 定义取数据协程
    print(f"  开始获取 {i}")  # 打印开始信息
    await asyncio.sleep(0.1)  # 模拟耗时
    print(f"  完成获取 {i}")  # 打印完成信息
    return i * 10  # 返回 i 的 10 倍

async def main2():  # 定义主协程
    start = time.time()  # 记录开始时间
    results = await asyncio.gather(*(fetch_data(i) for i in range(5)))  # 并发执行 5 个任务
    print(f"  结果: {results}")  # 打印结果列表
    print(f"  耗时: {time.time() - start:.2f}s")  # 打印总耗时

asyncio.run(main2())  # 运行主协程


# ===== 4. Task 对象 =====
print("\n--- Task ---")  # 打印本节标题
async def main3():  # 定义主协程
    task1 = asyncio.create_task(fetch_data(1))  # 创建任务 1
    task2 = asyncio.create_task(fetch_data(2))  # 创建任务 2
    # 可以先做其他事
    print("  任务已创建,等待结果")  # 打印提示信息
    r1 = await task1  # 等待任务 1 结果
    r2 = await task2  # 等待任务 2 结果
    print(f"  合并: {r1 + r2}")  # 打印两任务结果之和

asyncio.run(main3())  # 运行主协程


# ===== 5. 超时与取消 =====
print("\n--- 超时 ---")  # 打印本节标题
async def long_task():  # 定义长时间任务
    await asyncio.sleep(5)  # 休眠 5 秒
    return "完成"  # 返回完成字符串

async def main4():  # 定义主协程
    try:  # 尝试执行可能超时的任务
        await asyncio.wait_for(long_task(), timeout=0.3)  # 最多等 0.3 秒
    except asyncio.TimeoutError:  # 捕获超时异常
        print("  任务超时!")  # 打印超时提示

asyncio.run(main4())  # 运行主协程


# ===== 6. 异步上下文管理器 =====
print("\n--- 异步上下文管理器 ---")  # 打印本节标题
class AsyncResource:  # 定义异步资源类
    async def __aenter__(self):  # 异步进入方法
        print("  异步打开")  # 打印打开信息
        await asyncio.sleep(0.05)  # 模拟打开耗时
        return self  # 返回资源对象

    async def __aexit__(self, exc_type, exc, tb):  # 异步退出方法
        print("  异步关闭")  # 打印关闭信息
        await asyncio.sleep(0.05)  # 模拟关闭耗时

async def main5():  # 定义主协程
    async with AsyncResource() as r:  # 使用异步上下文管理器
        print("  使用中")  # 打印使用信息
    print("  结束")  # 打印结束信息

asyncio.run(main5())  # 运行主协程


# ===== 7. 异步迭代器 =====
print("\n--- 异步迭代器 ---")  # 打印本节标题
class AsyncCounter:  # 定义异步计数器类
    def __init__(self, stop):  # 初始化方法
        self.stop = stop  # 设置终止值
        self.current = 0  # 当前值初始化为 0
    def __aiter__(self):  # 返回异步迭代器
        return self  # 返回自身
    async def __anext__(self):  # 异步获取下一个值
        if self.current >= self.stop:  # 达到终止条件
            raise StopAsyncIteration  # 抛出停止迭代异常
        await asyncio.sleep(0.05)  # 模拟异步耗时
        self.current += 1  # 当前值自增
        return self.current  # 返回当前值

async def main6():  # 定义主协程
    async for i in AsyncCounter(3):  # 异步迭代
        print(f"  {i}")  # 打印每个值

asyncio.run(main6())  # 运行主协程


# ===== 8. 信号量(限流) =====
print("\n--- Semaphore ---")  # 打印本节标题
async def limited_task(sem, i):  # 定义限流任务
    async with sem:  # 获取信号量
        print(f"  任务 {i} 开始")  # 打印开始
        await asyncio.sleep(0.1)  # 模拟耗时
        print(f"  任务 {i} 完成")  # 打印完成

async def main7():  # 定义主协程
    sem = asyncio.Semaphore(2)    # 同时最多2个  # 创建信号量,允许 2 个并发
    await asyncio.gather(*(limited_task(sem, i) for i in range(5)))  # 并发 5 个任务

asyncio.run(main7())  # 运行主协程


# ===== 9. 异步队列 =====
print("\n--- asyncio.Queue ---")  # 打印本节标题
async def producer(q):  # 定义异步生产者
    for i in range(3):  # 生产 3 个数据
        await q.put(i)  # 异步入队
    await q.put(None)    # 哨兵  # 放入结束标志

async def consumer(q):  # 定义异步消费者
    while True:  # 无限循环消费
        item = await q.get()  # 异步出队
        if item is None:  # 收到哨兵
            break  # 退出循环
        print(f"  消费: {item}")  # 打印消费数据

async def main8():  # 定义主协程
    q = asyncio.Queue()  # 创建异步队列
    await asyncio.gather(producer(q), consumer(q))  # 并发运行生产者和消费者

asyncio.run(main8())  # 运行主协程


# ===== 10. 实战:模拟并发 HTTP 请求 =====
print("\n--- 模拟并发请求 ---")  # 打印本节标题
async def mock_http(url, delay):  # 定义模拟 HTTP 请求
    await asyncio.sleep(delay)  # 模拟网络延迟
    return f"<{url}:{int(delay*1000)}ms>"  # 返回带延迟信息的结果

async def main9():  # 定义主协程
    urls = [("a", 0.1), ("b", 0.05), ("c", 0.15), ("d", 0.08)]  # URL 和对应延迟
    start = time.time()  # 记录开始时间
    tasks = [mock_http(u, d) for u, d in urls]  # 创建任务列表
    results = await asyncio.gather(*tasks)  # 并发执行所有任务
    print(f"  并发结果: {results}")  # 打印结果
    print(f"  总耗时: {time.time() - start:.2f}s (应接近最长的单个请求)")  # 打印总耗时

asyncio.run(main9())  # 运行主协程


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 用 aiohttp 实现真正的并发 HTTP 请求(需 pip install aiohttp)")  # 练习题 1
    print("2. 实现一个异步的生产者-消费者模型")  # 练习题 2
    print("3. 编写一个异步定时器(每秒打印一次时间)")  # 练习题 3
