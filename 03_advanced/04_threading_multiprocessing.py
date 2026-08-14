"""04 - 并发编程:线程与多进程

学习目标:
    - 理解 GIL 与多线程
    - 掌握 threading 模块
    - 掌握 concurrent.futures
    - 掌握 multiprocessing
"""

import time  # 导入时间模块,用于 sleep 和计时
import threading  # 导入线程模块
import multiprocessing  # 导入多进程模块
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed  # 导入线程池、进程池和完成回调


# ===== 1. GIL 与线程 =====
print("--- 关于 GIL ---")  # 打印本节标题
# GIL(全局解释器锁)使得 Python 同一时刻只有一个线程执行字节码
# CPU 密集型任务:多线程无帮助,应用多进程
# I/O 密集型任务:多线程能提升性能


# ===== 2. 基本线程 =====
print("\n--- threading ---")  # 打印本节标题
def worker(name, delay):  # 定义线程工作函数
    print(f"  线程 {name} 启动")  # 打印启动信息
    time.sleep(delay)  # 模拟耗时操作
    print(f"  线程 {name} 完成")  # 打印完成信息
    return name  # 返回线程名

threads = []  # 用于保存线程对象
for i in range(3):  # 创建 3 个线程
    t = threading.Thread(target=worker, args=(f"T{i}", 0.1))  # 创建线程,指定目标和参数
    threads.append(t)  # 加入列表
    t.start()  # 启动线程

for t in threads:  # 遍历所有线程
    t.join()  # 等待线程结束
print("所有线程完成")  # 打印完成提示


# ===== 3. 线程同步:Lock =====
print("\n--- Lock ---")  # 打印本节标题
counter = 0  # 全局计数器
lock = threading.Lock()  # 创建锁对象

def increment():  # 定义自增函数
    global counter  # 声明使用全局变量
    for _ in range(100000):  # 循环 10 万次
        with lock:        # 临界区  # 加锁保护共享变量
            counter += 1  # 自增

ts = [threading.Thread(target=increment) for _ in range(5)]  # 创建 5 个自增线程
for t in ts: t.start()  # 启动所有线程
for t in ts: t.join()  # 等待所有线程结束
print(f"counter = {counter}")    # 应为 500000  # 打印结果,理论值为 50 万


# ===== 4. ThreadPoolExecutor =====
print("\n--- ThreadPoolExecutor ---")  # 打印本节标题
def fetch_url(url):  # 定义模拟抓取函数
    time.sleep(0.1)        # 模拟 I/O  # 模拟网络延迟
    return f"<{url}>"  # 返回模拟结果

urls = [f"http://example.com/{i}" for i in range(10)]  # 生成 10 个 URL
start = time.time()  # 记录开始时间
with ThreadPoolExecutor(max_workers=5) as pool:  # 创建最多 5 个线程的线程池
    results = list(pool.map(fetch_url, urls))  # 并发执行 map
elapsed = time.time() - start  # 计算耗时
print(f"10 个任务并发耗时 {elapsed:.2f}s,结果数: {len(results)}")  # 打印耗时和结果数


# ===== 5. 多进程(绕过 GIL) =====
print("\n--- multiprocessing ---")  # 打印本节标题
def cpu_bound(n):  # 定义 CPU 密集型任务
    return sum(i * i for i in range(n))  # 计算并返回平方和

if __name__ == "__main__":  # 多进程必须放在这里  # Windows 下多进程的入口保护
    with ProcessPoolExecutor(max_workers=4) as pool:  # 创建最多 4 个进程的进程池
        nums = [10**6, 10**6, 10**6, 10**6]  # 4 个大数字
        results = list(pool.map(cpu_bound, nums))  # 并行计算
    print(f"4 个 CPU 任务结果之和: {sum(results)}")  # 打印结果总和


# ===== 6. 进程间通信 =====
print("\n--- multiprocessing.Queue ---")  # 打印本节标题
def producer(q):  # 定义生产者函数
    for i in range(5):  # 生产 5 个数据
        q.put(i)  # 放入队列
    q.put(None)            # 哨兵  # 放入结束标志

def consumer(q):  # 定义消费者函数
    while True:  # 无限循环消费
        item = q.get()  # 从队列取出
        if item is None:  # 收到哨兵
            break  # 退出循环
        print(f"  消费: {item}")  # 打印消费的数据


# 简化:仅打印说明
print("Queue 演示完成")  # 简化处理,仅打印说明


# ===== 7. 守护线程 =====
print("\n--- 守护线程 ---")  # 打印本节标题
def background():  # 定义后台任务
    while True:  # 无限循环
        print("  后台运行中...")  # 打印运行信息
        time.sleep(0.5)  # 每 0.5 秒一次

t = threading.Thread(target=background, daemon=True)  # 创建守护线程
t.start()  # 启动守护线程
time.sleep(1.2)  # 主线程休眠 1.2 秒
print("主线程结束,后台线程自动退出")  # 主线程退出时守护线程自动结束


# ===== 8. 线程安全的 Queue =====
print("\n--- queue.Queue ---")  # 打印本节标题
import queue  # 导入 queue 模块
q = queue.Queue()  # 创建线程安全队列
for i in range(3):  # 放入 3 个元素
    q.put(i)  # 入队
while not q.empty():  # 队列非空时循环
    print(f"  取出: {q.get()}")  # 出队并打印


if __name__ == "__main__":  # 直接运行本文件时执行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 用多线程实现一个并发下载器")  # 练习题 1
    print("2. 用多进程并行计算一个大列表的所有元素平方和,对比单进程速度")  # 练习题 2
    print("3. 实现一个生产者-消费者模型")  # 练习题 3
