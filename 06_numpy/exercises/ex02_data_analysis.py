"""练习2: 成绩数据分析

用 NumPy 分析学生成绩:
    - 计算每人总分、平均分
    - 找出每科最高分/最低分
    - 按总分排名
    - 计算标准差评估成绩稳定性
"""

import numpy as np                                # 导入 numpy 模块

# 学生成绩数据：5名学生 × 3科（语文、数学、英语）
scores = np.array([                               # 定义成绩矩阵
    [85, 92, 78],                                 # 学生1
    [72, 88, 95],                                 # 学生2
    [90, 85, 82],                                 # 学生3
    [65, 70, 75],                                 # 学生4
    [88, 95, 90],                                 # 学生5
])
subjects = ["语文", "数学", "英语"]                # 科目名称列表

# 计算每人总分和平均分
total = scores.sum(axis=1)                        # 沿行方向求和（每人的总分）
average = scores.mean(axis=1)                     # 沿行方向求均值（每人的平均分）
print("每人总分:", total)                         # 打印总分
print("每人平均:", np.round(average, 1))          # 打印平均分（保留1位小数）

# 每科统计
for i, subject in enumerate(subjects):            # 遍历每科
    col = scores[:, i]                            # 取该科所有学生的成绩
    print(f"{subject}: 最高{col.max()}, 最低{col.min()}, 均值{col.mean():.1f}")  # 打印统计

# 按总分排名
rank_indices = np.argsort(total)[::-1]            # argsort 排序后取逆序（从高到低）
print("\n成绩排名:")                              # 打印排名标题
for rank, idx in enumerate(rank_indices, 1):      # 遍历排名
    print(f"  第{rank}名: 学生{idx+1}, 总分{total[idx]}")  # 打印排名信息

# 成绩稳定性（标准差越小越稳定）
stds = scores.std(axis=1)                         # 计算每人成绩的标准差
print("\n成绩稳定性(标准差):")                     # 打印标题
for i, std in enumerate(stds):                    # 遍历每个学生
    stability = "稳定" if std < 8 else "波动较大"  # 标准差小于8判为稳定
    print(f"  学生{i+1}: σ={std:.2f} ({stability})")  # 打印结果

# 及格率
pass_rate = (scores >= 60).mean()                 # 布尔索引算及格率
print(f"\n总体及格率: {pass_rate:.1%}")           # 打印及格率
