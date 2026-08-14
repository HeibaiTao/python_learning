"""练习 2:异步网络爬虫

题目描述:
    用 asyncio + aiohttp 实现并发爬虫
    - 给定一组 URL,异步抓取并解析
    - 用信号量限制并发数
    - 统计每个请求耗时
    - 处理异常和超时

要求:
    - 使用 pip install aiohttp
    - 如果没有 aiohttp,可用 httpx 或仅做 mock
"""

import asyncio  # 导入异步编程库
import time  # 导入时间模块用于计时
import random  # 导入随机数模块
from typing import Optional  # 导入 Optional 类型


# ===== 模拟异步 HTTP 客户端(无需安装 aiohttp) =====
class MockResponse:  # 模拟响应类
    def __init__(self, text, status=200):  # 初始化响应文本和状态码
        self.text = text  # 保存响应文本
        self.status = status  # 保存状态码

    async def text_async(self):  # 异步获取文本
        return self.text  # 返回响应文本

    async def __aenter__(self):  # 异步上下文进入
        return self  # 返回自身

    async def __aexit__(self, *args):  # 异步上下文退出
        return False  # 不处理异常


class MockClientSession:  # 模拟客户端会话类
    async def __aenter__(self):  # 异步进入
        return self  # 返回自身

    async def __aexit__(self, exc_type, exc, tb):  # 异步退出
        return False  # 不处理异常

    async def get(self, url):  # 异步 GET 方法
        await asyncio.sleep(random.uniform(0.05, 0.3))  # 随机休眠模拟网络延迟
        return MockResponse(f"<html>{url}</html>")  # 返回模拟响应


# ===== 实际可用的实现(需要 aiohttp) =====
"""
import aiohttp

class RealClientSession:
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self._session.close()

    async def get(self, url):
        async with self._session.get(url, timeout=10) as resp:
            resp.raise_for_status()
            return await resp.text()
"""


# ===== 爬虫主体 =====
class AsyncCrawler:  # 异步爬虫类
    def __init__(self, urls, max_concurrent=5, delay_range=(0.05, 0.2)):  # 初始化方法
        self.urls = urls  # URL 列表
        self.semaphore = asyncio.Semaphore(max_concurrent)  # 信号量限制并发数
        self.delay_range = delay_range  # 延迟范围
        self.results = {}  # 结果字典

    async def fetch_one(self, session, url):  # 抓取单个 URL
        async with self.semaphore:  # 获取信号量
            t0 = time.time()  # 记录开始时间
            try:  # 尝试抓取
                resp = await session.get(url)  # 发起 GET 请求
                text = await resp.text_async()  # 获取响应文本
                elapsed = time.time() - t0  # 计算耗时
                self.results[url] = {  # 保存成功结果
                    "ok": True,  # 成功标志
                    "size": len(text),  # 文本大小
                    "elapsed": elapsed,  # 耗时
                }
            except Exception as e:  # 捕获异常
                self.results[url] = {"ok": False, "error": str(e)}  # 保存失败结果

    async def run(self):  # 运行爬虫
        async with MockClientSession() as session:  # 创建会话
            tasks = [self.fetch_one(session, url) for url in self.urls]  # 为每个 URL 创建任务
            await asyncio.gather(*tasks, return_exceptions=True)  # 并发执行所有任务

    def report(self):  # 打印报告
        print(f"\n共抓取 {len(self.results)} 个 URL")  # 打印总数
        for url, res in self.results.items():  # 遍历结果
            if res["ok"]:  # 如果成功
                print(f"  ✓ {url}  大小={res['size']}B  耗时={res['elapsed']*1000:.0f}ms")  # 打印成功信息
            else:
                print(f"  ✗ {url}  错误: {res['error']}")  # 打印失败信息


if __name__ == "__main__":  # 直接运行本文件时执行
    urls = [f"https://example.com/page/{i}" for i in range(10)]  # 生成 10 个 URL

    start = time.time()  # 记录开始时间
    crawler = AsyncCrawler(urls, max_concurrent=3)  # 创建爬虫,并发 3
    asyncio.run(crawler.run())  # 运行爬虫
    print(f"总耗时: {time.time() - start:.2f}s")  # 打印总耗时
    crawler.report()  # 打印报告
