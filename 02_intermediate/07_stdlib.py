"""07 - 常用标准库

学习目标:
    - 了解 Python 丰富的标准库
    - 掌握常用模块的典型用法
"""

import datetime  # 导入 datetime 模块,处理日期时间
import re  # 导入 re 模块,处理正则表达式(本文件未直接使用)
import json  # 导入 json 模块,处理 JSON 数据
import os  # 导入 os 模块,与操作系统交互
import sys  # 导入 sys 模块,访问解释器变量
import logging  # 导入 logging 模块,记录日志
import argparse  # 导入 argparse 模块,解析命令行参数
import hashlib  # 导入 hashlib 模块,计算哈希
import secrets  # 导入 secrets 模块,生成安全随机数
import pathlib  # 导入 pathlib 模块,面向对象的路径操作
import subprocess  # 导入 subprocess 模块,执行子进程


# ===== 1. datetime =====
print("--- datetime ---")  # 打印分隔标题,演示 datetime 模块
now = datetime.datetime.now()  # 获取当前本地时间
print("现在:", now)  # 打印当前时间
print("格式化:", now.strftime("%Y-%m-%d %H:%M:%S"))  # 按指定格式打印时间
print("ISO:", now.isoformat())  # 打印 ISO 标准格式时间

# 时长
delta = datetime.timedelta(days=7, hours=3)  # 创建 7 天 3 小时的时间差
print("一周后:", now + delta)  # 打印当前时间加上时间差后的时间

# 解析字符串
dt = datetime.datetime.strptime("2026-07-04", "%Y-%m-%d")  # 把字符串按格式解析成日期对象
print("解析:", dt, type(dt))  # 打印解析结果和类型


# ===== 2. logging =====
print("\n--- logging ---")  # 打印分隔标题,演示 logging 模块
logging.basicConfig(  # 配置日志基本设置
    level=logging.INFO,  # 设置日志级别为 INFO
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"  # 设置日志输出格式
)
logger = logging.getLogger("demo")  # 创建名为 demo 的日志器
logger.debug("调试信息")  # 输出 debug 级别日志(不会显示,因为级别不够)
logger.info("普通信息")  # 输出 info 级别日志
logger.warning("警告")  # 输出 warning 级别日志
logger.error("错误")  # 输出 error 级别日志


# ===== 3. argparse:命令行参数 =====
print("\n--- argparse ---")  # 打印分隔标题,演示 argparse 模块
def parse_args():  # 定义解析参数的函数
    parser = argparse.ArgumentParser(description="示例 CLI 工具")  # 创建参数解析器
    parser.add_argument("name", help="用户名")  # 添加必填位置参数 name
    parser.add_argument("-a", "--age", type=int, default=0, help="年龄")  # 添加可选参数 age,类型为整数
    parser.add_argument("-v", "--verbose", action="store_true", help="详细模式")  # 添加布尔开关参数 verbose
    return parser.parse_args()  # 解析并返回参数对象

# 在命令行运行:python 07_stdlib.py Tom -a 18 -v
# 下面模拟调用
import sys  # 再次导入 sys 模块(用于修改 argv 演示)
sys.argv = ["07_stdlib.py", "Tom", "-a", "18", "-v"]  # 模拟命令行参数
try:  # 尝试解析参数
    args = parse_args()  # 调用解析函数
    print(f"姓名={args.name}, 年龄={args.age}, verbose={args.verbose}")  # 打印解析结果
except SystemExit:  # argparse 解析失败会抛出 SystemExit
    pass  # 忽略退出异常
finally:  # 无论是否出错都执行
    sys.argv = ["07_stdlib.py"]  # 恢复 argv,避免影响后续


# ===== 4. hashlib / secrets =====
print("\n--- hashlib / secrets ---")  # 打印分隔标题,演示哈希和随机数
# 哈希(用于完整性校验,不是密码)
data = "Hello, World!"  # 准备要哈希的字符串
md5 = hashlib.md5(data.encode()).hexdigest()  # 计算 MD5 哈希(十六进制字符串)
sha256 = hashlib.sha256(data.encode()).hexdigest()  # 计算 SHA256 哈希
print(f"MD5:    {md5}")  # 打印 MD5
print(f"SHA256: {sha256[:32]}...")  # 打印 SHA256 前 32 个字符

# 密码哈希(应使用 bcrypt/argon2)
# 这里仅演示 PBKDF2
import hashlib  # 再次导入 hashlib(演示用途)
salt = secrets.token_bytes(16)  # 生成 16 字节随机盐值
hashed = hashlib.pbkdf2_hmac("sha256", b"mypassword", salt, 100000)  # 用 PBKDF2-HMAC-SHA256 迭代 10 万次哈希密码
print(f"加盐哈希: {hashed.hex()[:32]}...")  # 打印加盐哈希前 32 个字符

# 生成安全随机数
print(f"安全 token: {secrets.token_hex(16)}")  # 打印 16 字节的随机十六进制 token
print(f"6 位验证码: {secrets.SystemRandom().randint(100000, 999999)}")  # 打印 6 位随机验证码


# ===== 5. pathlib =====
print("\n--- pathlib ---")  # 打印分隔标题,演示 pathlib 模块
p = pathlib.Path(".") / "utils" / "demo.py"  # 用 / 拼接路径:./utils/demo.py
print(f"路径: {p}")  # 打印路径
print(f"  后缀: {p.suffix}")  # 打印文件后缀(扩展名)
print(f"  父目录: {p.parent}")  # 打印父目录
print(f"  存在: {p.exists()}")  # 打印路径是否存在


# ===== 6. subprocess =====
print("\n--- subprocess ---")  # 打印分隔标题,演示 subprocess 模块
# 运行外部命令
result = subprocess.run(  # 运行子进程
    [sys.executable, "-c", "print('Hello from subprocess')"],  # 用当前 Python 执行一段代码
    capture_output=True, text=True  # 捕获输出并以文本形式返回
)
print("stdout:", result.stdout.strip())  # 打印子进程的标准输出(去首尾空白)
print("returncode:", result.returncode)  # 打印子进程退出码


# ===== 7. os / sys 常用 =====
print("\n--- os / sys ---")  # 打印分隔标题,演示 os 和 sys 模块
print(f"平台: {sys.platform}")  # 打印操作系统平台标识
print(f"Python: {sys.version_info.major}.{sys.version_info.minor}")  # 打印 Python 主版本号
print(f"当前进程 PID: {os.getpid()}")  # 打印当前进程 ID
print(f"环境变量 PATH 长度: {len(os.environ.get('PATH', ''))}")  # 打印 PATH 环境变量长度


# ===== 8. json 高级 =====
print("\n--- json 高级 ---")  # 打印分隔标题,演示 json 高级用法
from collections import namedtuple  # 从 collections 导入 namedtuple,创建具名元组

Point = namedtuple("Point", ["x", "y"])  # 定义具名元组 Point,有 x、y 字段

# 自定义 JSON 编码器
class PointEncoder(json.JSONEncoder):  # 自定义 JSON 编码器,继承 JSONEncoder
    def default(self, obj):  # 重写 default 方法,处理未知类型
        if isinstance(obj, Point):  # 如果是 Point 类型
            return {"__type__": "Point", "x": obj.x, "y": obj.y}  # 转成字典
        return super().default(obj)  # 其他类型交给父类处理

p = Point(1, 2)  # 创建 Point 实例
print("编码:", json.dumps(p, cls=PointEncoder))  # 用自定义编码器把 Point 转 JSON


# ===== 9. 实用:配置文件 =====
print("\n--- configparser ---")  # 打印分隔标题,演示 configparser
import configparser  # 导入 configparser 模块,处理 INI 配置文件

config = configparser.ConfigParser()  # 创建配置解析器
config["DEFAULT"] = {"debug": "false", "timeout": "30"}  # 设置默认配置段
config["database"] = {"host": "localhost", "port": "5432"}  # 设置 database 配置段
config["cache"] = {"type": "redis", "ttl": "3600"}  # 设置 cache 配置段

buf = StringIO() if False else None  # 占位
# 也可以写到文件
print("(configparser 内容详见配置)")  # 打印提示


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 写一个 CLI 工具,用 argparse 接收多个文件并合并")  # 练习题 1
    print("2. 写一个文件 hash 校验工具")  # 练习题 2
    print("3. 用 logging + configparser 搭建一个日志配置模块")  # 练习题 3
