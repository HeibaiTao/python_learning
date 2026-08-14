"""练习 4:文件统计工具

题目描述:
    编写一个脚本,统计指定文本文件:
        1. 总行数
        2. 总字符数(去除空白)
        3. 单词数
        4. 出现频率最高的 10 个单词
        5. 文件中所有的数字之和(整数和浮点数都要)

提示:
    - 使用 collections.Counter
    - 正则提取数字: r"\\d+(?:\\.\\d+)?"
    - 用 sys.argv 接收命令行参数
"""

import sys                            # 导入 sys 模块,用于接收命令行参数
import re                             # 导入正则表达式模块,用于匹配文本
from collections import Counter       # 从 collections 导入 Counter,用于计数
from pathlib import Path              # 从 pathlib 导入 Path,用于路径操作


def analyze_file(path: Path) -> dict:  # 定义文件分析函数,接收 Path 对象,返回统计字典
    """分析文件并返回统计结果"""         # 函数文档字符串
    if not path.exists():              # 如果文件不存在
        raise FileNotFoundError(f"文件不存在: {path}")  # 抛出文件不存在的异常

    text = path.read_text(encoding="utf-8")  # 读取文件全部内容,指定 utf-8 编码
    lines = text.splitlines()               # 按行分割文本,得到行列表

    # 词频统计
    words = re.findall(r"\b\w+\b", text.lower())  # 用正则匹配所有单词,\b 是单词边界,\w+ 匹配字母数字下划线,统一转小写
    word_counter = Counter(words)                 # 用 Counter 统计每个单词出现的次数

    # 数字提取
    numbers = re.findall(r"\d+(?:\.\d+)?", text)  # 用正则匹配所有数字(包括整数和浮点数)
    total = sum(float(n) for n in numbers)        # 把所有数字转浮点数后求和

    return {                                # 返回统计结果字典
        "file": str(path),                  # 文件路径
        "line_count": len(lines),           # 总行数
        "char_count_no_space": len(re.sub(r"\s", "", text)),  # 去除所有空白字符后的字符数
        "word_count": len(words),           # 单词总数
        "top10_words": word_counter.most_common(10),  # 出现频率最高的 10 个单词
        "number_sum": total,                # 所有数字之和
    }


def report(stats: dict):                   # 定义报告打印函数,接收统计字典
    """打印报告"""                          # 函数文档字符串
    print(f"\n=== 文件分析报告: {stats['file']} ===")  # 打印报告标题
    print(f"行数:           {stats['line_count']}")    # 打印总行数
    print(f"字符数(去空白): {stats['char_count_no_space']}")  # 打印去空白后的字符数
    print(f"单词数:         {stats['word_count']}")    # 打印单词数
    print(f"数字之和:       {stats['number_sum']:.2f}")  # 打印数字之和,保留 2 位小数
    print("高频词 Top 10:")                 # 打印高频词标题
    for word, count in stats["top10_words"]:  # 遍历前 10 个高频词
        print(f"  {word:<15} {count}")      # 打印单词和次数,<15 表示左对齐占 15 字符


if __name__ == "__main__":                 # 当本文件被直接运行时才执行
    if len(sys.argv) < 2:                  # 如果命令行参数不足(没传文件路径)
        print("用法: python ex04_file_stats.py <文件路径>")  # 打印用法提示
    else:                                  # 否则
        try:                               # 尝试分析文件
            report(analyze_file(Path(sys.argv[1])))  # 调用 analyze_file 分析文件并打印报告,sys.argv[1] 是文件路径
        except FileNotFoundError as e:     # 捕获文件不存在的异常
            print(e)                       # 打印异常信息
