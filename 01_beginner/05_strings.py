"""05 - 字符串操作

学习目标:
    - 掌握字符串常用方法
    - 理解字符串是不可变对象
    - 了解正则表达式入门
"""

# ===== 1. 字符串基础 =====
print("--- 字符串基础 ---")                       # 打印标题分隔线
s = "Hello, Python World!"                       # 定义一个字符串变量 s

print(s.lower())          # 全小写               # 将字符串全部转为小写字母
print(s.upper())          # 全大写               # 将字符串全部转为大写字母
print(s.title())          # 单词首字母大写       # 每个单词的首字母大写，其余小写
print(s.capitalize())     # 句子首字母大写       # 仅第一个单词首字母大写，其余小写
print(s.swapcase())       # 大小写互换           # 大写变小写，小写变大写

print(s.startswith("Hello"))                     # 判断字符串是否以"Hello"开头，返回 True 或 False
print(s.endswith("!"))                           # 判断字符串是否以"!"结尾，返回 True 或 False
print(s.find("Python"))   # 找不到返回 -1        # 查找子串"Python"的位置，找不到返回 -1
print(s.index("Python"))  # 找不到抛异常         # 查找子串"Python"的位置，找不到会报错 ValueError


# ===== 2. 字符串分割与拼接 =====
print("\n--- 分割与拼接 ---")                     # 打印换行和标题
sentence = "apple,banana,cherry,date"            # 定义一个用逗号分隔的字符串
parts = sentence.split(",")                    # 分割成列表   # 按逗号拆分字符串，得到列表 ['apple', 'banana', 'cherry', 'date']
print(parts)                                     # 打印拆分后的列表

joined = " | ".join(parts)                     # 用分隔符拼接  # 用" | "作为连接符，将列表元素拼接成一个字符串
print(joined)                                    # 打印拼接后的结果

# 按行分割
text = "line1\nline2\nline3"                     # 定义一个含换行符 \n 的字符串，表示三行文本
lines = text.splitlines()                        # 按换行符拆分成列表，得到 ['line1', 'line2', 'line3']
print(lines)                                     # 打印按行拆分后的列表


# ===== 3. 字符串清理 =====
print("\n--- 字符串清理 ---")                     # 打印标题
messy = "   hello world   \n"                    # 定义一个前后有空白字符和换行符的字符串
print(repr(messy.strip()))      # 去除两端空白   # strip() 去掉两端空白，repr() 显示字符串原始样子（可以看到转义字符）
print(repr(messy.lstrip()))     # 去除左端       # lstrip() 只去掉左侧（开头）的空白
print(repr(messy.rstrip()))     # 去除右端       # rstrip() 只去掉右侧（结尾）的空白

# 替换
print("hello".replace("l", "L"))  # 全部替换     # 将字符串中所有 "l" 替换为 "L"
print("hello".replace("l", "L", 1))  # 只替换1次 # 只替换第 1 个 "l" 为 "L"


# ===== 4. 字符串格式化 =====
print("\n--- 格式化 ---")                         # 打印标题
name, age = "Tom", 18                            # 同时定义两个变量：name 为字符串 "Tom"，age 为整数 18

# f-string(推荐)
print(f"姓名: {name}, 年龄: {age}")              # f-string 用 {} 在字符串中嵌入变量，最推荐的格式化方式
print(f"圆周率: {3.14159:.2f}")          # 保留2位小数  # :.2f 表示保留 2 位小数
print(f"左对齐: {'hi':<10}|")                    # :<10 表示左对齐，总宽度 10 格，不足补空格
print(f"右对齐: {'hi':>10}|")                    # :>10 表示右对齐，总宽度 10 格
print(f"居中:   {'hi':^10}|")                    # :^10 表示居中对齐，总宽度 10 格
print(f"百分比: {0.876:.2%}")                    # :.2% 将小数转为百分比形式，保留 2 位小数
print(f"千分位: {1234567:,}")                    # :, 为数字添加千分位逗号分隔符

# format 方法
print("{} 是 {} 岁".format(name, age))           # 用 format() 按顺序填入 {} 占位符
print("{name} 是 {age} 岁".format(name=name, age=age))  # 用名称指定占位符，顺序可任意


# ===== 5. 字符串是不可变的 =====
print("\n--- 不可变性 ---")                       # 打印标题
s2 = "hello"                                     # 定义一个字符串变量 s2
# s2[0] = "H"      # 报错!TypeError              # 不能直接修改字符串中的某个字符，会报错 TypeError
s2 = "H" + s2[1:]    # 必须创建新字符串          # 正确的做法：用切片 s2[1:] 取后面的部分，再拼接成新字符串
print(s2)                                        # 打印修改后的字符串 "Hello"


# ===== 6. 正则表达式入门 =====
print("\n--- 正则表达式 ---")                     # 打印标题
import re                                        # 导入正则表达式模块 re，用于在字符串中匹配模式

text = "联系电话: 138-1234-5678, 邮箱: tom@example.com"  # 定义一个包含手机号和邮箱的测试文本

# 匹配手机号
phones = re.findall(r"1[3-9]\d-\d{4}-\d{4}", text)  # 用正则查找所有手机号，r"" 表示原始字符串（反斜杠不转义）
print("手机号:", phones)                             # 打印找到的手机号列表

# 匹配邮箱
emails = re.findall(r"[\w.]+@[\w.]+", text)          # 用正则查找所有邮箱，\w 表示字母数字下划线
print("邮箱:", emails)                               # 打印找到的邮箱列表

# 替换
masked = re.sub(r"\d", "*", "13812345678")           # 用正则将字符串中所有数字 \d 替换为 *
print("脱敏:", masked)                               # 打印脱敏后的结果，如 "***********"

# 分割
parts2 = re.split(r"[,;:\s]+", "a, b; c: d e")      # 用正则按逗号、分号、冒号、空白字符拆分字符串
print("分割:", parts2)                               # 打印拆分后的列表


# ===== 练习 1: 判断回文 =====
print("\n--- 练习1: 判断回文 ---")                     # 打印标题
def is_palindrome(s):                                # 定义函数，参数 s 是要判断的字符串
    """判断字符串是否是回文（正读反读一样）"""         # 函数说明文档
    s = s.lower()                                    # 先转为小写，忽略大小写差异
    s = ''.join(c for c in s if c.isalnum())         # 只保留字母和数字，去掉空格、标点等
    return s == s[::-1]                              # 判断处理后的字符串是否等于它的反转

# 测试回文函数
print(is_palindrome("racecar"))                      # 测试英文回文，结果 True
print(is_palindrome("A man, a plan, a canal: Panama"))  # 测试含空格标点的回文，结果 True
print(is_palindrome("上海自来水来自海上"))            # 测试中文回文，结果 True
print(is_palindrome("hello"))                        # 测试非回文，结果 False


# ===== 练习 2: 统计字符频率 =====
print("\n--- 练习2: 统计字符频率 ---")                # 打印标题
def char_frequency(text):                            # 定义函数，参数 text 是要统计的文本
    """统计文本中每个字符出现的次数，返回字典"""       # 函数说明文档
    freq = {}                                        # 创建空字典用于存储字符和次数
    for char in text:                                # 遍历文本中的每个字符
        if char in freq:                             # 如果字符已在字典中
            freq[char] += 1                          # 次数加 1
        else:                                        # 如果字符不在字典中
            freq[char] = 1                           # 初始化为 1
    return freq                                      # 返回统计结果字典

# 测试字符频率函数
sample_text = "hello world"                          # 定义测试文本
result = char_frequency(sample_text)                 # 调用函数统计频率
for char, count in sorted(result.items()):           # 遍历并按字符排序输出
    print(f"  '{char}': {count}")                    # 打印每个字符及其出现次数


# ===== 练习 3: 用正则提取 HTML 链接 =====
print("\n--- 练习3: 提取 HTML 链接 ---")              # 打印标题
def extract_links(html):                             # 定义函数，参数 html 是 HTML 文本
    """用正则表达式提取 HTML 中的所有链接"""           # 函数说明文档
    # 正则解释：<a 开始，[^>]* 匹配属性内容，href="([^"]*)" 捕获引号内的 URL
    pattern = r'<a[^>]*href="([^"]*)"'               # 定义正则：匹配 <a> 标签的 href 属性值
    links = re.findall(pattern, html)                # 用 findall 提取所有匹配的 URL
    return links                                     # 返回链接列表

# 测试提取链接函数
html_sample = """                                    # 定义测试用的 HTML 片段
<html>
<body>
    <a href="https://www.python.org">Python官网</a>
    <a href="https://docs.python.org">Python文档</a>
    <a href="https://pypi.org">PyPI</a>
</body>
</html>
"""                                                   # HTML 片段结束
links = extract_links(html_sample)                   # 调用函数提取链接
print("提取到的链接：")                               # 打印提示
for link in links:                                   # 遍历每个链接
    print(f"  {link}")                               # 打印链接


if __name__ == "__main__":                           # 判断是否直接运行此脚本（不是被导入）
    print("\n[练习] 已完成上述三个练习，可直接运行查看效果。")