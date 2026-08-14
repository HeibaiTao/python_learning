"""项目 3:数据分析示例

功能:
    - 读取 CSV 数据
    - 数据清洗
    - 基础统计
    - 简单可视化(需要 matplotlib)

数据:
    自动生成一个示例销售数据 CSV
"""
import csv                           # 导入 CSV 模块,用于读写 CSV 文件
import random                        # 导入随机数模块,用于生成示例数据
from datetime import datetime, timedelta   # 从 datetime 导入 datetime 和 timedelta,用于日期运算
from pathlib import Path             # 从 pathlib 导入 Path 类,用于路径操作
from collections import Counter      # 从 collections 导入 Counter,用于计数统计


def generate_sample_csv(path: Path, rows=200):   # 生成示例销售数据 CSV 的函数
    """生成示例销售数据"""
    products = ["手机", "电脑", "平板", "耳机", "键盘", "鼠标"]   # 产品列表
    regions = ["北京", "上海", "广州", "深圳", "杭州"]   # 地区列表

    start = datetime(2026, 1, 1)     # 数据起始日期
    with open(path, "w", newline="", encoding="utf-8") as f:   # 打开文件写入(newline 防止空行)
        writer = csv.writer(f)       # 创建 CSV 写入器
        writer.writerow(["日期", "产品", "数量", "单价", "地区"])   # 写入表头
        for _ in range(rows):        # 循环生成指定行数的数据
            d = start + timedelta(days=random.randint(0, 180))   # 随机日期(起始日往后 0-180 天)
            p = random.choice(products)   # 随机选产品
            q = random.randint(1, 10)   # 随机数量 1-10
            price = random.randint(100, 8000)   # 随机单价 100-8000
            r = random.choice(regions)   # 随机选地区
            writer.writerow([d.strftime("%Y-%m-%d"), p, q, price, r])   # 写入一行数据
    print(f"已生成 {rows} 行示例数据 -> {path}")   # 打印生成完成信息


def load_csv(path: Path):            # 读取 CSV 的函数
    """读取 CSV"""
    with open(path, "r", encoding="utf-8") as f:   # 打开文件读取
        return list(csv.DictReader(f))   # 用 DictReader 读取,每行转为字典


def clean_data(rows):                # 数据清洗函数:类型转换、去除空值
    """数据清洗:类型转换、去除空值"""
    cleaned = []                     # 存放清洗后的数据
    for r in rows:                   # 遍历每一行
        try:                         # 尝试转换字段类型
            cleaned.append({         # 把清洗后的行加入列表
                "日期": datetime.strptime(r["日期"], "%Y-%m-%d").date(),   # 日期字符串转 date 对象
                "产品": r["产品"].strip(),   # 产品名去空格
                "数量": int(r["数量"]),   # 数量转整数
                "单价": float(r["单价"]),   # 单价转浮点数
                "地区": r["地区"].strip(),   # 地区去空格
            })
        except (ValueError, KeyError):   # 如果转换失败或字段缺失
            continue                 # 跳过该行
    return cleaned                   # 返回清洗后的数据


def total_sales_by_product(rows):    # 按产品统计销售额的函数
    """按产品统计销售额"""
    sales = {}                       # 存放每个产品的销售额
    for r in rows:                   # 遍历每一行
        amount = r["数量"] * r["单价"]   # 计算该行销售额
        sales[r["产品"]] = sales.get(r["产品"], 0) + amount   # 累加到对应产品
    return sorted(sales.items(), key=lambda x: -x[1])   # 按销售额降序排序返回


def monthly_sales(rows):             # 按月统计销售额的函数
    """按月统计销售额"""
    sales = {}                       # 存放每月销售额
    for r in rows:                   # 遍历每一行
        key = r["日期"].strftime("%Y-%m")   # 用"年-月"作为统计键
        amount = r["数量"] * r["单价"]   # 计算该行销售额
        sales[key] = sales.get(key, 0) + amount   # 累加到对应月份
    return sorted(sales.items())     # 按月份升序排序返回


def region_distribution(rows):       # 地区销售分布的函数
    """地区销售分布"""
    counts = Counter(r["地区"] for r in rows)   # 统计每个地区出现的次数
    return counts.most_common()      # 返回按次数降序的列表


def top_products(rows, n=3):         # 销量 Top N 的函数
    """销量 Top N"""
    counts = Counter(r["产品"] for r in rows)   # 统计每个产品出现次数
    return counts.most_common(n)     # 返回前 N 名


def report(rows):                    # 生成文本报告的函数
    """生成文本报告"""
    print("\n" + "=" * 50)           # 打印分隔线
    print("          销售数据报告")   # 打印报告标题
    print("=" * 50)                  # 打印分隔线
    print(f"\n总记录数: {len(rows)}")   # 打印总记录数
    print(f"日期范围: {min(r['日期'] for r in rows)} ~ {max(r['日期'] for r in rows)}")   # 打印日期范围
    total = sum(r["数量"] * r["单价"] for r in rows)   # 计算总销售额
    print(f"总销售额: ¥{total:,.2f}")   # 打印总销售额(千分位,两位小数)

    print("\n--- 产品销售额排名 ---")   # 打印小标题
    for prod, amount in total_sales_by_product(rows):   # 遍历产品销售额排名
        print(f"  {prod:<8} ¥{amount:>10,.2f}")   # 打印产品名和销售额

    print("\n--- 月度销售趋势 ---")   # 打印小标题
    for month, amount in monthly_sales(rows):   # 遍历月度销售
        print(f"  {month}  ¥{amount:>12,.2f}")   # 打印月份和销售额

    print("\n--- 地区分布 ---")       # 打印小标题
    for region, count in region_distribution(rows):   # 遍历地区分布
        print(f"  {region:<6} {count:>4} 笔")   # 打印地区和订单数

    print("\n--- 销量 Top 3 产品 ---")   # 打印小标题
    for prod, count in top_products(rows):   # 遍历 Top 3 产品
        print(f"  {prod:<8} {count:>4} 件")   # 打印产品名和销量

    print("=" * 50)                  # 打印分隔线


def plot(rows):                      # 可视化函数(需要 matplotlib)
    """可视化(需要 matplotlib)"""
    try:                             # 尝试导入 matplotlib
        import matplotlib.pyplot as plt   # 导入绘图库
        plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]   # 设置中文字体
        plt.rcParams["axes.unicode_minus"] = False   # 正常显示负号
    except ImportError:              # 如果没安装 matplotlib
        print("(跳过可视化,未安装 matplotlib)")   # 打印提示
        return                       # 直接返回

    # 产品销售额柱状图
    sales = total_sales_by_product(rows)   # 获取产品销售额数据
    products = [p for p, _ in sales]   # 提取产品名列表
    amounts = [a for _, a in sales]   # 提取销售额列表
    plt.figure(figsize=(10, 4))      # 创建画布,设置尺寸
    plt.subplot(1, 2, 1)             # 第 1 行第 2 列的第 1 个子图
    plt.bar(products, amounts)       # 绘制柱状图
    plt.title("产品销售额")           # 设置标题
    plt.xticks(rotation=30)          # x 轴标签旋转 30 度
    plt.ylabel("金额(¥)")           # 设置 y 轴标签

    # 月度趋势
    monthly = monthly_sales(rows)    # 获取月度销售数据
    months = [m for m, _ in monthly]   # 提取月份列表
    amts = [a for _, a in monthly]   # 提取销售额列表
    plt.subplot(1, 2, 2)             # 第 1 行第 2 列的第 2 个子图
    plt.plot(months, amts, marker="o")   # 绘制折线图(带圆点标记)
    plt.title("月度销售趋势")         # 设置标题
    plt.xticks(rotation=30)          # x 轴标签旋转 30 度

    plt.tight_layout()               # 自动调整子图间距
    plt.show()                       # 显示图表


if __name__ == "__main__":           # 当脚本直接运行时
    data_path = Path(__file__).parent / "sales.csv"   # 数据文件路径(与本脚本同目录)
    if not data_path.exists():       # 如果数据文件不存在
        generate_sample_csv(data_path)   # 生成示例数据

    rows = clean_data(load_csv(data_path))   # 读取并清洗数据
    report(rows)                    # 生成并打印报告
    plot(rows)                       # 绘制可视化图表
