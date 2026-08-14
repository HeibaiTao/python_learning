"""06 - 文件 I/O

学习目标:
    - 掌握文件的读写
    - 了解 with 语句(上下文管理器)
    - 了解 JSON / CSV 文件处理
"""

import json                                       # 导入 json 模块，用于处理 JSON 格式文件
import csv                                        # 导入 csv 模块，用于处理 CSV 表格文件
import os                                         # 导入 os 模块，用于操作系统相关功能
from pathlib import Path                          # 从 pathlib 模块导入 Path 类，用于路径处理

# ===== 1. 文本文件读写 =====
print("--- 文本文件读写 ---")                      # 打印标题

DATA_DIR = Path(__file__).parent / "data"         # 获取当前脚本所在目录，并在其中创建 data 子目录路径
DATA_DIR.mkdir(exist_ok=True)                     # 创建 data 目录，exist_ok=True 表示目录已存在时不报错
sample_file = DATA_DIR / "sample.txt"             # 定义示例文件的完整路径

# 写入
with open(sample_file, "w", encoding="utf-8") as f:  # 用 with 语句打开文件，"w" 表示写入模式，自动关闭文件
    f.write("第一行\n")                            # 写入一行文本，\n 表示换行符
    f.write("第二行\n")                            # 再写入一行文本
    f.writelines(["第三行\n", "第四行\n"])          # writelines 一次写入列表中的多行文本

# 读取方式
with open(sample_file, "r", encoding="utf-8") as f:  # 用 with 语句打开文件，"r" 表示读取模式
    content = f.read()              # 一次性读取全部  # read() 方法读取文件全部内容，返回一个字符串
    print(content)                                 # 打印读取到的全部内容

with open(sample_file, "r", encoding="utf-8") as f:  # 再次打开文件进行读取
    line = f.readline()             # 一次读一行    # readline() 只读取一行内容，返回字符串
    print("单行:", line.strip())                   # 打印读取的一行，strip() 去掉末尾的换行符

with open(sample_file, "r", encoding="utf-8") as f:  # 再次打开文件进行读取
    lines = f.readlines()           # 读成列表      # readlines() 读取所有行，返回列表，每行是一个元素
    print("列表:", lines)                          # 打印读取到的行列表

# 逐行遍历(推荐,适合大文件)
with open(sample_file, "r", encoding="utf-8") as f:  # 用 with 语句打开文件进行读取
    for i, line in enumerate(f, 1):                # enumerate 遍历文件的每一行，i 是行号（从 1 开始）
        print(f"  L{i}: {line.rstrip()}")          # 打印行号和内容，rstrip() 去掉右侧空白字符


# ===== 2. pathlib(现代路径处理) =====
print("\n--- pathlib ---")                         # 打印换行和标题
p = Path(".") / "data" / "sample.txt"
print("cwd:", Path.cwd())                        # 当前工作目录
print("脚本目录:", Path(__file__).parent)         # 脚本所在目录
print("p 的绝对路径:", p.resolve())               # p 解析后的绝对路径
print("sample_file:", sample_file)                # sample_file 的路径              # 用 / 符号拼接路径，"." 表示当前目录
print(p.exists(), p.is_file(), p.suffix, p.stem)   # 打印：是否存在、是否是文件、后缀名、文件名（不含后缀）
print(list(Path(".").glob("**/*.py"))[:3], "...")  # 列出前3个 .py 文件  # glob 递归搜索所有 .py 文件，取前 3 个


# ===== 3. JSON 文件 =====
print("\n--- JSON ---")                             # 打印换行和标题
data = {                                           # 定义一个字典，用于演示 JSON 数据结构
    "name": "Tom",                                 # 姓名
    "age": 18,                                     # 年龄
    "skills": ["Python", "Java", "Go"],            # 技能列表
    "address": {"city": "Beijing", "zip": "100000"}  # 地址信息（嵌套字典）
}

json_file = DATA_DIR / "data.json"                 # 定义 JSON 文件的完整路径
with open(json_file, "w", encoding="utf-8") as f:  # 用 with 语句打开文件进行写入
    json.dump(data, f, ensure_ascii=False, indent=2)  # json.dump 将字典写入文件，ensure_ascii=False 保留中文，indent=2 缩进格式化

with open(json_file, "r", encoding="utf-8") as f:  # 用 with 语句打开文件进行读取
    loaded = json.load(f)                          # json.load 从文件读取 JSON 数据，转为 Python 字典
    print(loaded)                                  # 打印加载的字典
    print("姓名:", loaded["name"])                 # 通过键"name"访问字典中的值


# ===== 4. CSV 文件 =====
print("\n--- CSV ---")                              # 打印换行和标题
csv_file = DATA_DIR / "data.csv"                   # 定义 CSV 文件的完整路径

# 写入
with open(csv_file, "w", newline="", encoding="utf-8") as f:  # 用 with 语句打开 CSV 文件，newline="" 避免 Windows 多余空行
    writer = csv.writer(f)                         # 创建 CSV 写入器对象
    writer.writerow(["姓名", "年龄", "城市"])       # 写入表头行（列名）
    writer.writerow(["Tom", 18, "Beijing"])        # 写入第一行数据
    writer.writerow(["Jerry", 20, "Shanghai"])     # 写入第二行数据

# 读取
with open(csv_file, "r", encoding="utf-8") as f:   # 用 with 语句打开 CSV 文件进行读取
    reader = csv.reader(f)                         # 创建 CSV 读取器对象
    for row in reader:                             # 遍历每一行
        print(row)                                 # 打印当前行（列表形式）

# 用 DictReader(更方便)
with open(csv_file, "r", encoding="utf-8") as f:   # 用 with 语句打开 CSV 文件进行读取
    reader = csv.DictReader(f)                     # 创建字典读取器，每行转为字典，键是表头
    for row in reader:                             # 遍历每一行
        print(row)                                 # 打印当前行（字典形式，如 {'姓名': 'Tom', '年龄': '18', ...}）


# ===== 5. 二进制文件 =====
print("\n--- 二进制文件 ---")                        # 打印换行和标题
bin_file = DATA_DIR / "sample.bin"                 # 定义二进制文件的完整路径
data_bytes = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"    # "世界" UTF-8 编码  # 定义字节串，b 前缀表示二进制数据

with open(bin_file, "wb") as f:                    # 用 with 语句打开文件，"wb" 表示二进制写入模式
    f.write(data_bytes)                            # 写入二进制数据到文件

with open(bin_file, "rb") as f:                    # 用 with 语句打开文件，"rb" 表示二进制读取模式
    raw = f.read()                                 # 读取全部二进制数据
    print(raw)                                     # 打印原始字节串
    print(raw.decode("utf-8"))                     # 将字节串用 UTF-8 解码为字符串并打印


# ===== 6. 异常处理(在文件操作中) =====
print("\n--- 异常处理 ---")                          # 打印换行和标题
try:                                               # try 语句块，尝试执行可能出错的代码
    with open("not_exist.txt", "r", encoding="utf-8") as f:  # 尝试打开一个不存在的文件
        print(f.read())                            # 尝试读取文件内容
except FileNotFoundError as e:                     # 捕获文件不存在的异常
    print("文件不存在:", e)                         # 打印错误提示和异常信息
except PermissionError:                            # 捕获权限不足的异常
    print("没有权限")                               # 打印权限错误提示


# 清理示例文件
for f in [sample_file, json_file, csv_file, bin_file]:  # 遍历所有示例文件路径
    if f.exists():                                 # 判断文件是否存在
        f.unlink()                                 # unlink() 删除文件
print("清理完成")                                   # 打印清理完成提示


# ===== 练习 1: 读取日志文件,统计 ERROR 出现的次数 =====
print("\n--- 练习1: 统计日志中 ERROR 次数 ---")      # 打印标题

# 先创建一个模拟日志文件
log_file = DATA_DIR / "app.log"                    # 定义日志文件路径
with open(log_file, "w", encoding="utf-8") as f:   # 打开文件进行写入
    f.write("2024-01-01 10:00:00 INFO  服务启动\n")  # 写入一条 INFO 日志
    f.write("2024-01-01 10:01:00 ERROR 数据库连接失败\n")  # 写入一条 ERROR 日志
    f.write("2024-01-01 10:02:00 INFO  重试中...\n")  # 写入一条 INFO 日志
    f.write("2024-01-01 10:03:00 ERROR 超时未响应\n")  # 写入一条 ERROR 日志
    f.write("2024-01-01 10:04:00 WARN  内存使用偏高\n")  # 写入一条 WARN 日志
    f.write("2024-01-01 10:05:00 ERROR 权限不足\n")  # 写入一条 ERROR 日志

# 统计 ERROR 出现的次数
error_count = 0                                    # 初始化错误计数器为 0
with open(log_file, "r", encoding="utf-8") as f:   # 打开日志文件进行读取
    for line in f:                                 # 逐行遍历日志文件
        if "ERROR" in line:                        # 判断当前行是否包含 "ERROR" 字符串
            error_count += 1                       # 如果包含，计数器加 1
            print(f"  发现错误: {line.strip()}")   # 打印该错误行内容
print(f"ERROR 总次数: {error_count}")              # 打印统计结果

# 清理日志文件
log_file.unlink()                                  # 删除模拟日志文件


# ===== 练习 2: 把 CSV 转成 JSON 格式 =====
print("\n--- 练习2: CSV 转 JSON ---")               # 打印标题

# 先创建一个 CSV 文件
csv_file2 = DATA_DIR / "users.csv"                 # 定义 CSV 文件路径
with open(csv_file2, "w", newline="", encoding="utf-8") as f:  # 打开 CSV 文件进行写入
    writer = csv.writer(f)                         # 创建 CSV 写入器
    writer.writerow(["姓名", "年龄", "城市"])       # 写入表头
    writer.writerow(["张三", 25, "北京"])           # 写入第一行数据
    writer.writerow(["李四", 30, "上海"])           # 写入第二行数据
    writer.writerow(["王五", 28, "广州"])           # 写入第三行数据

# 读取 CSV，转为 JSON
records = []                                       # 创建空列表，用于存储所有行数据
with open(csv_file2, "r", encoding="utf-8") as f:  # 打开 CSV 文件进行读取
    reader = csv.DictReader(f)                     # 创建字典读取器，每行自动转为字典
    for row in reader:                             # 遍历每一行
        row["年龄"] = int(row["年龄"])              # 把年龄从字符串转为整数
        records.append(row)                        # 将字典添加到列表中

# 写入 JSON 文件
json_file2 = DATA_DIR / "users.json"               # 定义 JSON 文件路径
with open(json_file2, "w", encoding="utf-8") as f:  # 打开 JSON 文件进行写入
    json.dump(records, f, ensure_ascii=False, indent=2)  # 将列表写入 JSON 文件，保留中文，缩进格式

# 打印转换结果
print("CSV 转 JSON 完成:")                          # 打印提示
for record in records:                             # 遍历转换后的数据
    print(f"  {record}")                           # 打印每条记录

# 清理练习文件
csv_file2.unlink()                                 # 删除 CSV 文件
json_file2.unlink()                                # 删除 JSON 文件


# ===== 练习 3: 用 pathlib 遍历目录,统计所有 .py 文件的行数 =====
print("\n--- 练习3: 统计 .py 文件行数 ---")          # 打印标题

py_dir = Path(__file__).parent                     # 获取当前脚本所在目录（01_beginner）
total_lines = 0                                    # 初始化总行数为 0
file_count = 0                                     # 初始化文件数为 0

for py_file in py_dir.glob("*.py"):                # glob("*.py") 找出目录下所有 .py 文件
    with open(py_file, "r", encoding="utf-8") as f:  # 打开每个 .py 文件
        line_count = sum(1 for line in f)          # 用生成器表达式统计行数：每遍历一行就计数 1
    print(f"  {py_file.name}: {line_count} 行")    # 打印文件名和行数
    total_lines += line_count                      # 累加到总行数
    file_count += 1                                # 文件数加 1

print(f"共 {file_count} 个 .py 文件，总计 {total_lines} 行")  # 打印统计汇总


if __name__ == "__main__":                         # 判断是否直接运行此脚本（不是被导入）
    print("\n[练习] 请尝试:")                       # 打印练习提示
    print("1. 读取一个日志文件,统计 ERROR 出现的次数")  # 练习1：日志分析
    print("2. 把一个 CSV 转成 JSON 格式")           # 练习2：格式转换
    print("3. 用 pathlib 遍历某目录,统计所有 .py 文件的行数")  # 练习3：目录遍历统计