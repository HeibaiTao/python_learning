"""项目 2:简单网页爬虫

功能:
    - 抓取单个页面
    - 提取所有链接
    - 提取所有图片 URL
    - 简单的 BFS 爬取

依赖:
    pip install requests beautifulsoup4
"""
import re                            # 导入正则表达式模块,用于回退方案提取链接
import sys                           # 导入系统模块,用于读取命令行参数和退出
from urllib.parse import urljoin, urlparse   # 从 urllib.parse 导入 URL 拼接和解析工具
from collections import deque        # 从 collections 导入 deque,用于广度优先队列


def fetch(url, timeout=10):          # 获取网页内容的函数
    """获取网页内容,优先用 requests,没有则用 urllib"""
    try:                             # 尝试导入 requests
        import requests              # 导入第三方 requests 库
        headers = {"User-Agent": "Mozilla/5.0 (Python learning)"}   # 设置请求头,模拟浏览器
        resp = requests.get(url, headers=headers, timeout=timeout)   # 发送 GET 请求
        resp.raise_for_status()      # 如果状态码不是 200,抛出异常
        # 自动检测编码
        resp.encoding = resp.apparent_encoding   # 用检测到的编码避免乱码
        return resp.text             # 返回网页文本
    except ImportError:              # 如果没安装 requests
        from urllib.request import urlopen, Request   # 用标准库回退
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})   # 创建请求对象
        with urlopen(req, timeout=timeout) as resp:   # 打开 URL
            return resp.read().decode("utf-8", errors="replace")   # 读取并解码为字符串


def extract_links(html, base_url):   # 从 HTML 中提取所有链接的函数
    """从 HTML 中提取所有链接"""
    try:                             # 尝试用 BeautifulSoup
        from bs4 import BeautifulSoup   # 导入解析库
        soup = BeautifulSoup(html, "html.parser")   # 解析 HTML
        links = set()                # 用集合存放链接(自动去重)
        for a in soup.find_all("a", href=True):   # 查找所有带 href 的 a 标签
            href = a["href"]         # 取出 href 属性
            full = urljoin(base_url, href)   # 拼成完整 URL
            if full.startswith(("http://", "https://")):   # 只保留 http/https 链接
                links.add(full)      # 加入集合
        return links                 # 返回链接集合
    except ImportError:              # 如果没安装 bs4
        # 简易正则回退方案
        pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)   # 匹配 href 的正则
        links = set()                # 用集合存放链接
        for m in pattern.finditer(html):   # 遍历所有匹配
            full = urljoin(base_url, m.group(1))   # 拼成完整 URL
            if full.startswith(("http://", "https://")):   # 只保留 http/https 链接
                links.add(full)      # 加入集合
        return links                 # 返回链接集合


def extract_images(html, base_url):  # 提取所有图片 URL 的函数
    """提取所有图片 URL"""
    pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)   # 匹配 img 标签 src 的正则
    return {urljoin(base_url, m.group(1)) for m in pattern.finditer(html)}   # 集合推导:返回所有完整图片 URL


def same_domain(url1, url2):         # 判断两个 URL 是否同域的函数
    return urlparse(url1).netloc == urlparse(url2).netloc   # 比较两者的 netloc(域名:端口)


def crawl(start_url, max_pages=10, max_depth=2):   # 广度优先爬取的函数
    """广度优先爬取"""
    visited = {start_url}            # 已访问的 URL 集合(含起始页)
    queue = deque([(start_url, 0)])  # 爬取队列,元素为 (URL, 深度)
    all_links = set()                # 收集所有链接
    all_images = set()               # 收集所有图片 URL

    print(f"开始爬取: {start_url}")  # 打印开始信息
    while queue and len(visited) <= max_pages:   # 队列非空且未超过最大页数
        url, depth = queue.popleft() # 从队列头部取一个 URL 及其深度
        try:                         # 尝试抓取
            html = fetch(url)        # 获取网页内容
        except Exception as e:       # 如果抓取失败
            print(f"  ✗ {url}: {e}")   # 打印错误信息
            continue                 # 跳过该 URL
        print(f"  ✓ [{len(visited)}] {url} (depth={depth})")   # 打印抓取成功信息

        links = extract_links(html, url)   # 提取该页面的所有链接
        all_links.update(links)      # 加入链接集合
        all_images.update(extract_images(html, url))   # 提取并加入图片 URL

        if depth < max_depth:        # 如果还没达到最大深度
            for link in links:       # 遍历该页面的链接
                if same_domain(link, start_url) and link not in visited:   # 同域且未访问过
                    visited.add(link)   # 标记为已访问
                    queue.append((link, depth + 1))   # 加入队列,深度加 1

    return visited, all_links, all_images   # 返回已访问页、所有链接、所有图片


def main():                          # 主函数
    if len(sys.argv) < 2:            # 如果没有传入起始 URL 参数
        print("用法: python crawler.py <起始URL> [最大页数] [最大深度]")   # 打印用法
        sys.exit(1)                  # 退出程序,返回非 0 状态码

    start = sys.argv[1]              # 第一个参数:起始 URL
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 10   # 第二个参数:最大页数,默认 10
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 2   # 第三个参数:最大深度,默认 2

    pages, links, images = crawl(start, max_pages, max_depth)   # 执行爬取
    print(f"\n=== 汇总 ===")         # 打印汇总标题
    print(f"访问页面: {len(pages)}")   # 打印访问页面数
    print(f"内部链接: {len(links)}")   # 打印链接数
    print(f"图片 URL: {len(images)}")   # 打印图片数


if __name__ == "__main__":           # 当脚本直接运行时
    main()                           # 调用主函数
