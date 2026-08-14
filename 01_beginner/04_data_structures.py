"""04 - 数据结构

学习目标:
    - 熟练使用 list、tuple、dict、set
    - 掌握列表/字典推导式
    - 了解 collections 中的高级容器
"""

# ===== 1. 列表(list) =====
print("--- list ---")                                # 打印分隔标题
fruits = ["apple", "banana", "cherry"]               # 创建列表，存3种水果

# 增删改查
fruits.append("date")                                # 在列表末尾追加"date"
fruits.insert(1, "apricot")                          # 在索引1的位置插入"apricot"
fruits.remove("banana")                              # 按值删除第一个匹配的"banana"
popped = fruits.pop()                                # 弹出并删除末尾元素，结果赋给popped
popped2 = fruits.pop(0)                              # 弹出并删除索引0的元素，结果赋给popped2
print(fruits)                                        # 打印最终列表

# 切片
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]              # 创建0~9的数字列表
print(nums[2:5])                                     # 切片：取索引2到4（不含5），结果[2,3,4]
print(nums[:5])                                      # 切片：从开头取到索引4，结果[0,1,2,3,4]
print(nums[::2])                                     # 切片：步长为2，取偶数索引，结果[0,2,4,6,8]
print(nums[::-1])                                    # 切片：步长为-1，反转列表

# 列表方法
nums.sort()                                          # 原地排序（从小到大）
nums.reverse()                                       # 原地反转顺序
print(len(nums), min(nums), max(nums), sum(nums))    # 打印长度、最小值、最大值、总和
print(nums)


# ===== 2. 元组(tuple) =====
print("\n--- tuple ---")                             # 打印分隔标题
point = (10, 20)                                     # 创建元组，表示坐标点
x, y = point                                         # 解包：将元组两个值分别赋给x和y
a, b, *rest = (1, 2, 3, 4, 5)                       # 高级解包：a=1, b=2, rest=[3,4,5]
print(x, y, a, b, rest)                              # 打印解包结果

# 不可变,但可作为 dict key
d = {(0, 0): "origin", (1, 1): "diag"}             # 元组不可变，可用作字典的键
print(d[(0, 0)])                                     # 用元组键取值，打印"origin"


# ===== 3. 字典(dict) =====
print("\n--- dict ---")                              # 打印分隔标题
person = {"name": "Tom", "age": 18, "city": "Beijing"}  # 创建字典，存个人信息
print(person["name"])                                # 用键"name"取值，打印"Tom"
print(person.get("email", "N/A"))                    # 用get安全取值，键不存在返回默认值"N/A"

# 增删改
person["email"] = "tom@example.com"                  # 新增键值对
person["age"] = 19                                   # 修改已有键的值
del person["city"]                                   # 删除键"city"及其对应的值

# 遍历
for key, value in person.items():                    # 遍历字典的键值对
    print(f"  {key}: {value}")                       # 打印每个键和值

# 字典推导式
squares_dict = {x: x ** 2 for x in range(5)}        # 字典推导式：{0:0, 1:1, 2:4, 3:9, 4:16}
print(squares_dict)                                  # 打印结果字典


# ===== 4. 集合(set) =====
print("\n--- set ---")                               # 打印分隔标题
s = {1, 2, 3, 3, 4, 4, 5}                          # 创建集合，重复元素自动去重
print(s)                                             # 打印集合，结果{1,2,3,4,5}

# 集合运算
a = {1, 2, 3, 4}                                     # 创建集合a
b = {3, 4, 5, 6}                                     # 创建集合b
print(a | b)                                         # 并集：a和b中所有不重复的元素
print(a & b)                                         # 交集：a和b中共有的元素
print(a - b)                                         # 差集：在a中但不在b中的元素
print(a ^ b)                                         # 对称差：a和b中非共有的元素

# 快速去重
nums_with_dup = [1, 2, 2, 3, 3, 3, 4]              # 创建有重复数字的列表
unique = list(set(nums_with_dup))                    # 先转集合去重，再转回列表
print(unique)                                        # 打印去重后的结果


# ===== 5. 高级容器(collections) =====
print("\n--- collections ---")                       # 打印分隔标题
from collections import Counter, defaultdict, deque, OrderedDict  # 导入collections模块中的4个工具

# Counter:计数器
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]  # 创建单词列表
counter = Counter(words)                             # 用Counter统计每个单词出现次数
print(counter.most_common(2))                        # 返回出现频率最高的2个元素及次数

# defaultdict:带默认值的字典
dd = defaultdict(int)                                # 创建默认值为0的字典
dd["a"] += 1                                         # "a"不存在，自动初始化为0再+1
dd["b"] += 1                                         # "b"不存在，自动初始化为0再+1
print(dd)                                            # 打印结果：{'a':1, 'b':1}

# deque:双端队列(高效的头尾操作)
dq = deque([1, 2, 3])                                # 创建双端队列，初始元素1,2,3
dq.appendleft(0)                                     # 在队列左侧添加0
dq.append(4)                                         # 在队列右侧添加4
print(dq)                                            # 打印队列
dq.popleft()                                         # 弹出并删除左侧元素0
print(dq)                                            # 打印删除后的队列


# ===== 6. 列表推导式 vs 生成器表达式 =====
print("\n--- 推导式 ---")                             # 打印分隔标题
# 列表推导式
squares_list = [x ** 2 for x in range(10)]           # 列表推导式：立即生成0~9的平方列表
# 集合推导式
squares_set = {x ** 2 for x in range(10)}            # 集合推导式：生成平方集合（自动去重）
# 生成器表达式(惰性求值,节省内存)
squares_gen = (x ** 2 for x in range(10))            # 生成器表达式：不立即计算，按需产出值
print(next(squares_gen), next(squares_gen), next(squares_gen))  # 逐个取值：0, 1, 4


# ===== 练习 1: 用 Counter 统计单词出现次数 =====
print("\n--- 练习1: Counter 统计单词频率 ---")        # 打印标题
text = "apple banana apple cherry banana apple grape"  # 定义一段测试文本，用空格分隔单词
words = text.split()                                   # 按空格拆分文本，得到单词列表
word_count = Counter(words)                            # 用 Counter 统计每个单词的出现次数
print("单词统计:", word_count)                         # 打印统计结果，如 Counter({'apple': 3, ...})
print("最常见的2个:", word_count.most_common(2))       # 打印出现频率最高的2个单词及次数


# ===== 练习 2: 用 defaultdict 实现简单的图结构 =====
print("\n--- 练习2: defaultdict 实现图 ---")           # 打印标题
graph = defaultdict(list)                              # 创建默认值为空列表的字典，存储邻接表

# 添加边（无向图）：A连接到B，同时B也连接到A
graph["A"].append("B")                                 # 添加边 A -> B
graph["B"].append("A")                                 # 添加边 B -> A（无向图需要双向）
graph["A"].append("C")                                 # 添加边 A -> C
graph["C"].append("A")                                 # 添加边 C -> A
graph["B"].append("C")                                 # 添加边 B -> C
graph["C"].append("B")                                 # 添加边 C -> B

print("图结构:", dict(graph))                          # 打印图：{'A':['B','C'], 'B':['A','C'], 'C':['A','B']}
# 遍历每个节点的邻居
for node, neighbors in graph.items():                  # 遍历图中每个节点及其邻居列表
    print(f"  {node} 的邻居: {neighbors}")             # 打印每个节点的邻居节点


# ===== 练习 3: 用 deque 实现最近 N 次操作的历史记录 =====
print("\n--- 练习3: deque 实现操作历史 ---")           # 打印标题
N = 3                                                  # 设置最多保留最近 N 次操作
history = deque(maxlen=N)                              # 创建 deque，maxlen=N 表示满了自动删除旧记录

# 模拟一系列操作
history.append("打开文件")                             # 添加操作记录
history.append("编辑内容")                             # 添加操作记录
history.append("保存文件")                             # 添加操作记录
print("历史记录:", list(history))                      # 打印当前历史：['打开文件', '编辑内容', '保存文件']

history.append("撤销操作")                             # 满3条后再添加新记录，最旧的"打开文件"自动被挤出
print("历史记录:", list(history))                      # 打印：['编辑内容', '保存文件', '撤销操作']

history.append("重做操作")                             # 继续添加，"编辑内容"被挤出
print("历史记录:", list(history))                      # 打印：['保存文件', '撤销操作', '重做操作']


if __name__ == "__main__":
    print("\n[练习] 已完成上述三个练习，可直接运行查看效果。")