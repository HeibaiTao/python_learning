"""项目 4:简易 Web 服务器

功能:
    - 纯标准库实现 HTTP 服务器
    - 路由分发
    - JSON API
    - 静态文件服务

用法:
    python server.py
    浏览器访问 http://localhost:8000
"""
import json                         # 导入 JSON 模块,用于响应数据序列化
import socket                       # 导入 socket 模块(此处未直接使用,保留)
import threading                    # 导入线程模块(ThreadingHTTPServer 内部使用)
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer   # 从 http.server 导入 HTTP 处理器和多线程服务器
from urllib.parse import urlparse, parse_qs   # 从 urllib.parse 导入 URL 解析和查询参数解析
from datetime import datetime       # 从 datetime 导入 datetime 类,用于时间戳


# 内存数据(模拟数据库)
TASKS = [                           # 任务列表(模拟数据库)
    {"id": 1, "title": "学习 Python", "done": False},   # 任务 1:未完成
    {"id": 2, "title": "完成项目", "done": True},   # 任务 2:已完成
]
_next_id = 3                        # 下一个任务的自增 ID


# ===== 路由 =====
ROUTES = {}                         # 路由表,存放 method -> {path: func}

def route(path, methods=("GET",)):  # 路由注册装饰器
    def decorator(func):            # 内层装饰器函数
        for m in methods:           # 遍历所有支持的请求方法
            ROUTES.setdefault(m, {})[path] = func   # 把函数注册到对应方法和路径
        return func                 # 返回原函数
    return decorator                # 返回装饰器


@route("/api/hello", methods=["GET"])   # 注册 GET /api/hello 路由
def hello(handler, params):         # 处理函数,返回问候和时间
    return 200, {"message": "Hello, World!", "time": datetime.now().isoformat()}   # 返回状态码 200 和 JSON 数据


@route("/api/tasks", methods=["GET"])   # 注册 GET /api/tasks 路由
def list_tasks(handler, params):    # 处理函数,返回所有任务
    return 200, {"tasks": TASKS}    # 返回状态码 200 和任务列表


@route("/api/tasks", methods=["POST"])   # 注册 POST /api/tasks 路由
def create_task(handler, params):   # 处理函数,创建新任务
    global _next_id                 # 声明使用全局变量 _next_id
    body = handler.json_body or {}  # 获取请求体,没有则为空字典
    if "title" not in body:         # 如果请求体没有 title 字段
        return 400, {"error": "缺少 title 字段"}   # 返回 400 错误
    task = {"id": _next_id, "title": body["title"], "done": False}   # 创建新任务字典
    _next_id += 1                   # 自增 ID
    TASKS.append(task)              # 把新任务加入列表
    return 201, task                # 返回 201(已创建)和新任务


@route("/api/tasks/{id}", methods=["DELETE"])   # 注册 DELETE /api/tasks/{id} 路由(带路径参数)
def delete_task(handler, params, task_id):   # 处理函数,删除指定任务
    for i, t in enumerate(TASKS):   # 遍历任务列表(带索引)
        if t["id"] == int(task_id): # 找到对应 ID 的任务
            TASKS.pop(i)            # 从列表中删除
            return 200, {"deleted": task_id}   # 返回 200 和被删除的 ID
    return 404, {"error": "not found"}   # 没找到,返回 404


# ===== HTTP Handler =====
class Handler(BaseHTTPRequestHandler):   # 自定义 HTTP 请求处理器
    json_body = None                # 类属性,存放解析后的 JSON 请求体

    def log_message(self, format, *args):   # 重写日志方法
        # 简化日志
        print(f"  [{self.command}] {self.path}")   # 只打印请求方法和路径

    def _set_headers(self, status, content_type="application/json"):   # 设置响应头的方法
        self.send_response(status)  # 发送状态码
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")   # 设置内容类型
        self.send_header("Access-Control-Allow-Origin", "*")   # 允许跨域访问
        self.end_headers()          # 结束响应头

    def _send_json(self, status, data):   # 发送 JSON 响应的方法
        self._set_headers(status)   # 设置响应头(默认 JSON)
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")   # 把数据序列化为 JSON 字节
        self.wfile.write(body)      # 写入响应体

    def _read_body(self):           # 读取并解析请求体的方法
        length = int(self.headers.get("Content-Length", 0))   # 获取请求体长度
        if length == 0: return None   # 没有请求体则返回 None
        raw = self.rfile.read(length)   # 读取原始字节
        try:                        # 尝试解析 JSON
            return json.loads(raw.decode("utf-8"))   # 解码并解析为字典
        except json.JSONDecodeError:   # 如果解析失败
            return None             # 返回 None

    def _dispatch(self, method):    # 请求分发方法
        parsed = urlparse(self.path)   # 解析 URL
        path = parsed.path           # 提取路径部分
        params = parse_qs(parsed.query)   # 解析查询参数

        # 路径参数匹配(如 /api/tasks/1)
        for pattern, func in ROUTES.get(method, {}).items():   # 遍历该方法的所有路由
            if "{" in pattern:       # 如果路由含路径参数占位符
                regex_parts = []     # 存放正则片段
                kwargs = {}          # 存放路径参数
                for part in pattern.split("/"):   # 按 / 拆分路由模式
                    if part.startswith("{") and part.endswith("}"):   # 如果是参数占位符
                        name = part[1:-1]   # 去掉花括号,取出参数名
                        regex_parts.append(f"(?P<{name}>[^/]+)")   # 转为命名捕获组
                    else:            # 普通文本
                        regex_parts.append(part)   # 直接加入
                import re            # 导入正则模块
                m = re.fullmatch("/".join(regex_parts), path)   # 用正则完整匹配路径
                if m:                # 如果匹配成功
                    self.json_body = self._read_body() if method == "POST" else None   # POST 才读请求体
                    kwargs = m.groupdict()   # 提取路径参数
                    status, data = func(self, params, **kwargs)   # 调用处理函数
                    self._send_json(status, data)   # 发送响应
                    return           # 结束分发

        if path in ROUTES.get(method, {}):   # 如果是普通路由(无路径参数)
            self.json_body = self._read_body() if method == "POST" else None   # POST 才读请求体
            status, data = ROUTES[method][path](self, params)   # 调用处理函数
            self._send_json(status, data)   # 发送响应
            return                   # 结束分发

        # 静态文件
        if method == "GET" and (path == "/" or path == "/index.html"):   # 如果请求主页
            self._serve_file("index.html", "text/html")   # 返回 index.html
            return                   # 结束分发
        if method == "GET":          # 其他 GET 请求当作静态文件
            self._serve_file(path.lstrip("/"), self._guess_type(path))   # 返回对应文件
            return                   # 结束分发

        self._send_json(404, {"error": "Not Found"})   # 都没匹配,返回 404

    def _serve_file(self, name, content_type):   # 提供静态文件服务的方法
        try:                        # 尝试读取文件
            base = __import__("pathlib").Path(__file__).parent   # 获取脚本所在目录
            with open(base / name, "rb") as f:   # 以二进制方式打开文件
                data = f.read()     # 读取全部内容
            self._set_headers(200, content_type)   # 设置响应头
            self.wfile.write(data)  # 写入响应体
        except FileNotFoundError:   # 如果文件不存在
            self._send_json(404, {"error": "Not Found"})   # 返回 404

    @staticmethod                    # 静态方法装饰器
    def _guess_type(path):           # 根据扩展名猜文件类型的方法
        if path.endswith(".css"): return "text/css"   # CSS 文件
        if path.endswith(".js"): return "application/javascript"   # JS 文件
        if path.endswith(".html"): return "text/html"   # HTML 文件
        if path.endswith(".png"): return "image/png"   # PNG 图片
        if path.endswith(".jpg"): return "image/jpeg"   # JPG 图片
        return "application/octet-stream"   # 默认二进制流

    def do_GET(self): self._dispatch("GET")   # 处理 GET 请求
    def do_POST(self): self._dispatch("POST")   # 处理 POST 请求
    def do_DELETE(self): self._dispatch("DELETE")   # 处理 DELETE 请求
    def do_PUT(self): self._dispatch("PUT")   # 处理 PUT 请求


# ===== 主页 =====
INDEX_HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Python 学习项目 - 简易 Web 服务</title>
    <style>
        body { font-family: -apple-system, sans-serif; max-width: 720px; margin: 40px auto; padding: 0 16px; }
        h1 { color: #2c3e50; }
        pre { background: #f4f4f4; padding: 12px; border-radius: 6px; }
        button { padding: 6px 12px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>简易 Web 服务</h1>
    <p>这是 <code>04_projects/simple_web_server</code> 的演示页。</p>

    <h2>API 列表</h2>
    <ul>
        <li><code>GET /api/hello</code></li>
        <li><code>GET /api/tasks</code></li>
        <li><code>POST /api/tasks</code> body: {"title": "..."}</li>
    </ul>

    <h2>测试</h2>
    <button onclick="fetch('/api/tasks').then(r=>r.json()).then(d=>alert(JSON.stringify(d)))">获取任务</button>

    <h2>响应示例</h2>
    <pre id="out">点击按钮查看</pre>

    <script>
        document.querySelector('button').onclick = async () => {
            const r = await fetch('/api/tasks');
            document.getElementById('out').textContent = JSON.stringify(await r.json(), null, 2);
        };
    </script>
</body>
</html>
"""


def save_index():                    # 把主页 HTML 写入文件的方法
    """把 HTML 写入同目录"""
    p = __import__("pathlib").Path(__file__).parent / "index.html"   # 拼接 index.html 路径
    p.write_text(INDEX_HTML, encoding="utf-8")   # 把 HTML 字符串写入文件


if __name__ == "__main__":           # 当脚本直接运行时
    save_index()                     # 生成 index.html 文件
    port = 8000                      # 服务端口
    print(f"服务启动: http://localhost:{port}")   # 打印启动信息
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)   # 创建多线程 HTTP 服务器(监听所有网卡)
    try:                             # 尝试启动服务
        server.serve_forever()       # 持续对外提供服务
    except KeyboardInterrupt:        # 如果收到 Ctrl+C
        print("\n停止服务")          # 打印停止信息
        server.shutdown()            # 关闭服务器
