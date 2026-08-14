"""练习1: 学生成绩分析

用 Pandas 分析学生成绩数据:
    - 计算每人总分、平均分、排名
    - 统计各科成绩分布
    - 找出偏科学生
"""

import pandas as pd                               # 导入 pandas 模块
import numpy as np                                # 导入 numpy 模块

# 创建学生成绩数据
np.random.seed(42)                                # 设置随机种子，保证每次运行结果一致
df = pd.DataFrame({                               # 创建成绩 DataFrame
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"],
    "语文": np.random.randint(60, 100, 8),        # 随机生成60-99的语文成绩
    "数学": np.random.randint(60, 100, 8),        # 数学成绩
    "英语": np.random.randint(60, 100, 8),        # 英语成绩
})

# 计算总分和平均分
df["总分"] = df[["语文", "数学", "英语"]].sum(axis=1)  # 三科总分
df["平均分"] = df["总分"] / 3                     # 平均分

# 按总分排名
df["排名"] = df["总分"].rank(ascending=False, method="min").astype(int)  # rank 排名
df = df.sort_values("排名")                       # 按排名排序

print("=== 成绩表 ===")                            # 打印标题
print(df.to_string(index=False))                  # to_string 美化打印

# 各科统计
print("\n=== 各科统计 ===")                        # 打印标题
stats = df[["语文", "数学", "英语"]].describe()   # describe 生成统计摘要
print(stats)                                      # 打印统计信息

# 找偏科学生（标准差大于15）
df["标准差"] = df[["语文", "数学", "英语"]].std(axis=1)  # 计算每人各科标准差
偏科 = df[df["标准差"] > 15]                      # 筛选标准差大于15的学生
print(f"\n=== 偏科学生（标准差>15）===")           # 打印标题
if len(偏科) > 0:                                 # 如果有偏科学生
    print(偏科[["姓名", "语文", "数学", "英语", "标准差"]])  # 打印偏科详情
else:                                             # 如果没有
    print("无偏科学生")                            # 打印提示

# 各科最高分和最低分
print("\n=== 各科最高/最低 ===")                   # 打印标题
for subject in ["语文", "数学", "英语"]:          # 遍历每科
    max_idx = df[subject].idxmax()                # 找最高分的行索引
    min_idx = df[subject].idxmin()                # 找最低分的行索引
    print(f"{subject}: 最高={df.loc[max_idx, '姓名']}({df.loc[max_idx, subject]}分), "
          f"最低={df.loc[min_idx, '姓名']}({df.loc[min_idx, subject]}分)")  # 打印最高最低

# 及格率
print("\n=== 及格率 ===")                          # 打印标题
for subject in ["语文", "数学", "英语"]:          # 遍历每科
    rate = (df[subject] >= 60).mean()             # 计算及格率
    print(f"{subject}及格率: {rate:.1%}")         # 打印及格率
