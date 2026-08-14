# Python 学习路径总结

> 本文档是对 [LEARNING_ROADMAP.md](file:///e:/编程练习/python_learning/LEARNING_ROADMAP.md) 的精简总结，列出每个阶段的**学习文件、重点知识、练习目标**，方便快速定位学习内容。

---

## 阶段一：入门基础（01_beginner）

> 🎯 目标：掌握 Python 语法基础，能写 100 行以内的小脚本

### 学习文件

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_variables_types.py](file:///e:/编程练习/python_learning/01_beginner/01_variables_types.py) | 变量赋值、5种基本数据类型、类型转换 | 能正确定义变量并进行类型转换 |
| 2 | [02_control_flow.py](file:///e:/编程练习/python_learning/01_beginner/02_control_flow.py) | if/elif/else、for/while、break/continue、推导式 | 能用循环和条件解决简单逻辑问题 |
| 3 | [03_functions.py](file:///e:/编程练习/python_learning/01_beginner/03_functions.py) | 函数定义、参数（*args/**kwargs）、作用域、lambda、装饰器入门 | 能独立封装函数并理解参数传递 |
| 4 | [04_data_structures.py](file:///e:/编程练习/python_learning/01_beginner/04_data_structures.py) | list/tuple/dict/set、collections、推导式 vs 生成器 | 能选择合适的数据结构解决问题 |
| 5 | [05_strings.py](file:///e:/编程练习/python_learning/01_beginner/05_strings.py) | 字符串方法、格式化(f-string)、正则表达式入门 | 能处理字符串并写简单正则匹配 |
| 6 | [06_file_io.py](file:///e:/编程练习/python_learning/01_beginner/06_file_io.py) | 文件读写、with语句、pathlib、JSON/CSV、异常处理 | 能读写文件并处理常见异常 |
| 7 | [07_exceptions.py](file:///e:/编程练习/python_learning/01_beginner/07_exceptions.py) | try/except/finally、自定义异常、异常最佳实践 | 能正确捕获和处理异常 |
| 8 | [08_venv_engineering.py](file:///e:/编程练习/python_learning/01_beginner/08_venv_engineering.py) | 虚拟环境、pip、PEP 8、Git基础、项目结构 | 能创建虚拟环境并管理依赖 |

### 练习文件

| 文件 | 内容 |
|------|------|
| [ex01_swap_calculator.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex01_swap_calculator.py) | 变量交换 + 简易计算器 |
| [ex02_fibonacci_palindrome.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex02_fibonacci_palindrome.py) | 斐波那契数列 + 回文判断 |
| [ex03_guess_password.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex03_guess_password.py) | 猜数字游戏 + 密码强度检测 |
| [ex04_file_stats.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex04_file_stats.py) | 文件读取 + 词频统计 |

### ✅ 检验标准
- 能独立完成 4 个练习文件
- 能配置虚拟环境并安装第三方库
- 能读懂基础报错信息（SyntaxError / TypeError 等）

---

## 阶段二：进阶开发（02_intermediate）

> 🎯 目标：掌握面向对象编程与常用标准库，能组织 500 行规模的模块化项目

### 学习文件

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_oop_basics.py](file:///e:/编程练习/python_learning/02_intermediate/01_oop_basics.py) | 类与对象、属性/方法、封装、property | 能定义类并创建实例 |
| 2 | [02_inheritance.py](file:///e:/编程练习/python_learning/02_intermediate/02_inheritance.py) | 继承、super()、多继承MRO、抽象基类 | 能设计继承体系并重写方法 |
| 3 | [03_magic_methods.py](file:///e:/编程练习/python_learning/02_intermediate/03_magic_methods.py) | __init__/__str__/__repr__/__eq__/__lt__等 | 能用魔术方法定制类行为 |
| 4 | [04_decorators.py](file:///e:/编程练习/python_learning/02_intermediate/04_decorators.py) | 闭包、装饰器原理、functools.wraps、带参装饰器 | 能手写装饰器并理解执行流程 |
| 5 | [05_generators.py](file:///e:/编程练习/python_learning/02_intermediate/05_generators.py) | yield、生成器表达式、itertools、惰性求值 | 能用生成器处理大数据流 |
| 6 | [06_context_managers.py](file:///e:/编程练习/python_learning/02_intermediate/06_context_managers.py) | __enter__/__exit__、@contextmanager、ExitStack | 能自定义上下文管理器 |
| 7 | [07_stdlib.py](file:///e:/编程练习/python_learning/02_intermediate/07_stdlib.py) | datetime/json/re/hashlib/logging/argparse/sqlite3 | 能使用常用标准库解决实际问题 |
| 8 | [08_modules_packages.py](file:///e:/编程练习/python_learning/02_intermediate/08_modules_packages.py) | import机制、__init__.py、包结构、相对导入 | 能组织多文件项目结构 |

### 练习文件

| 文件 | 内容 |
|------|------|
| [ex01_card_game.py](file:///e:/编程练习/python_learning/02_intermediate/exercises/ex01_card_game.py) | OOP实战：扑克牌游戏 |
| [ex02_lru_cache.py](file:///e:/编程练习/python_learning/02_intermediate/exercises/ex02_lru_cache.py) | 数据结构：LRU缓存实现 |
| [ex03_expression_eval.py](file:///e:/编程练习/python_learning/02_intermediate/exercises/ex03_expression_eval.py) | 算法：表达式求值器 |

### ✅ 检验标准
- 能用 OOP 设计扑克牌游戏
- 能手写装饰器和上下文管理器
- 能为自己的代码写 pytest 测试

---

## 阶段三：高级特性（03_advanced）

> 🎯 目标：深入 Python 内部机制，能解决性能瓶颈和架构设计问题

### 学习文件

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_descriptors.py](file:///e:/编程练习/python_learning/03_advanced/01_descriptors.py) | 描述符协议、__get__/__set__、属性查找顺序 | 理解property底层原理 |
| 2 | [02_metaclasses.py](file:///e:/编程练习/python_learning/03_advanced/02_metaclasses.py) | type()、元类、__init_subclass__、dataclasses | 能用元类实现自动注册 |
| 3 | [03_type_hints.py](file:///e:/编程练习/python_learning/03_advanced/03_type_hints.py) | 类型提示、typing模块、Generic、Protocol、mypy | 能为项目添加类型注解 |
| 4 | [04_threading_multiprocessing.py](file:///e:/编程练习/python_learning/03_advanced/04_threading_multiprocessing.py) | GIL、threading、multiprocessing、concurrent.futures | 能选择合适的并发方案 |
| 5 | [05_asyncio.py](file:///e:/编程练习/python_learning/03_advanced/05_asyncio.py) | async/await、事件循环、Task、Semaphore | 能编写异步IO程序 |
| 6 | [06_design_patterns.py](file:///e:/编程练习/python_learning/03_advanced/06_design_patterns.py) | 创建型/结构型/行为型模式、Python特色实现 | 能在实际项目中运用设计模式 |
| 7 | [07_testing.py](file:///e:/编程练习/python_learning/03_advanced/07_testing.py) | pytest进阶、fixture、mock、覆盖率、TDD | 能编写完善的单元测试 |

### 练习文件

| 文件 | 内容 |
|------|------|
| [ex01_mini_orm.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex01_mini_orm.py) | 用元类+描述符实现迷你ORM |
| [ex02_async_crawler.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex02_async_crawler.py) | 用asyncio实现异步爬虫 |
| [ex03_di_container.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex03_di_container.py) | 实现依赖注入容器 |

### ✅ 检验标准
- 能完成迷你ORM/异步爬虫/依赖注入练习
- 能用cProfile定位并优化慢函数
- 能为项目添加完整类型注解

---

## 阶段四：实战项目（04_projects）

> 🎯 目标：通过真实项目将知识融会贯通

### 项目列表

| 难度 | 项目 | 核心技术 | 练习目标 |
|------|------|---------|---------|
| 🟢 入门 | [todo_cli](file:///e:/编程练习/python_learning/04_projects/todo_cli/todo.py) | argparse + JSON + 文件操作 | 命令行工具开发 |
| 🟢 入门 | [chatbot](file:///e:/编程练习/python_learning/04_projects/chatbot/chatbot.py) | 字符串匹配 + 条件分支 | 规则引擎设计 |
| 🟢 入门 | [web_crawler](file:///e:/编程练习/python_learning/04_projects/web_crawler/crawler.py) | requests + BeautifulSoup | 网页数据抓取 |
| 🟡 进阶 | [game_2048](file:///e:/编程练习/python_learning/04_projects/game_2048/game.py) | OOP + 矩阵操作 + 终端UI | 游戏逻辑设计 |
| 🟡 进阶 | [data_analysis](file:///e:/编程练习/python_learning/04_projects/data_analysis/analyze.py) | CSV读取 + 统计分析 | 数据处理流程 |
| 🟠 中高 | [simple_web_server](file:///e:/编程练习/python_learning/04_projects/simple_web_server/server.py) | socket + HTTP协议 + 多线程 | 网络编程基础 |

---

## 阶段五：数据科学库（06_numpy → 07_pandas → 08_matplotlib）

> 🎯 目标：掌握数据分析三大核心库，能完成数据清洗、分析、可视化全流程

### 5.1 NumPy 科学计算

> ⚠️ 先学 NumPy，它是 Pandas 和 Matplotlib 的基础

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_array_creation.py](file:///e:/编程练习/python_learning/06_numpy/01_array_creation.py) | ndarray创建、数组属性、dtype | 能用多种方式创建数组 |
| 2 | [02_indexing_slicing.py](file:///e:/编程练习/python_learning/06_numpy/02_indexing_slicing.py) | 索引、切片、布尔索引、花式索引、where | 能灵活选取数组元素 |
| 3 | [03_operations.py](file:///e:/编程练习/python_learning/06_numpy/03_operations.py) | 逐元素运算、广播机制、矩阵乘法、向量化 | 理解广播规则并能向量化运算 |
| 4 | [04_shape_manipulation.py](file:///e:/编程练习/python_learning/06_numpy/04_shape_manipulation.py) | reshape/flatten/transpose、拼接拆分、copy vs view | 能变换数组形状并理解视图 |
| 5 | [05_statistical.py](file:///e:/编程练习/python_learning/06_numpy/05_statistical.py) | 统计函数、排序去重、npy/npz文件读写 | 能对数据做统计分析 |
| 6 | [06_linear_algebra.py](file:///e:/编程练习/python_learning/06_numpy/06_linear_algebra.py) | 行列式、逆矩阵、解方程组、SVD、最小二乘 | 能用线性代数解决实际问题 |

**练习：**
- [矩阵计算器](file:///e:/编程练习/python_learning/06_numpy/exercises/ex01_matrix_calculator.py)
- [成绩数据分析](file:///e:/编程练习/python_learning/06_numpy/exercises/ex02_data_analysis.py)
- [图像处理入门](file:///e:/编程练习/python_learning/06_numpy/exercises/ex03_image_processing.py)

### 5.2 Pandas 数据处理

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_series.py](file:///e:/编程练习/python_learning/07_pandas/01_series.py) | Series创建、属性、索引、运算 | 理解一维数据结构 |
| 2 | [02_dataframe.py](file:///e:/编程练习/python_learning/07_pandas/02_dataframe.py) | DataFrame创建、属性、行列增删 | 能创建和操作二维表 |
| 3 | [03_indexing.py](file:///e:/编程练习/python_learning/07_pandas/03_indexing.py) | loc/iloc、条件筛选、isin/between、排序 | 能灵活查询和筛选数据 |
| 4 | [04_data_cleaning.py](file:///e:/编程练习/python_learning/07_pandas/04_data_cleaning.py) | 缺失值/重复值处理、类型转换、replace、apply | 能清洗脏数据 |
| 5 | [05_groupby.py](file:///e:/编程练习/python_learning/07_pandas/05_groupby.py) | groupby、agg、merge、concat、pivot_table | 能分组聚合和合并数据 |
| 6 | [06_io.py](file:///e:/编程练习/python_learning/07_pandas/06_io.py) | CSV/Excel/JSON读写、时间序列、多文件合并 | 能读写各种格式文件 |

**练习：**
- [学生成绩分析](file:///e:/编程练习/python_learning/07_pandas/exercises/ex01_student_analysis.py)
- [销售数据分析](file:///e:/编程练习/python_learning/07_pandas/exercises/ex02_sales_report.py)
- [数据清洗流水线](file:///e:/编程练习/python_learning/07_pandas/exercises/ex03_data_pipeline.py)

### 5.3 Matplotlib 数据可视化

| 顺序 | 文件 | 重点知识 | 练习目标 |
|------|------|---------|---------|
| 1 | [01_basic_plots.py](file:///e:/编程练习/python_learning/08_matplotlib/01_basic_plots.py) | figure/axes、折线图、散点图、格式字符串 | 能画基本折线图和散点图 |
| 2 | [02_chart_types.py](file:///e:/编程练习/python_learning/08_matplotlib/02_chart_types.py) | 柱状图、饼图、直方图、箱线图、堆积图 | 能根据场景选择合适图表 |
| 3 | [03_style_customization.py](file:///e:/编程练习/python_learning/08_matplotlib/03_style_customization.py) | 颜色、坐标轴、注释箭头、图例、内置样式 | 能美化图表样式 |
| 4 | [04_subplots.py](file:///e:/编程练习/python_learning/08_matplotlib/04_subplots.py) | subplot/subplots、共享轴、不规则布局、双Y轴 | 能绘制多子图布局 |
| 5 | [05_advanced_plots.py](file:///e:/编程练习/python_learning/08_matplotlib/05_advanced_plots.py) | 热力图、面积图、3D图、等高线、雷达图 | 能画高级图表 |
| 6 | [06_pandas_integration.py](file:///e:/编程练习/python_learning/08_matplotlib/06_pandas_integration.py) | df.plot()、时间序列、完整分析流程 | 能与Pandas结合做可视化 |

**练习：**
- [城市气温可视化](file:///e:/编程练习/python_learning/08_matplotlib/exercises/ex01_temperature_trend.py)
- [销售数据仪表盘](file:///e:/编程练习/python_learning/08_matplotlib/exercises/ex02_sales_dashboard.py)
- [成绩分布分析](file:///e:/编程练习/python_learning/08_matplotlib/exercises/ex03_score_distribution.py)

### ✅ 数据科学阶段检验标准
- 能用 NumPy 完成矩阵运算和统计计算
- 能用 Pandas 完成数据清洗 → 分组聚合 → 文件读写全流程
- 能用 Matplotlib 画出包含 4 种图表的综合仪表盘
- 能完成「销售数据 → 清洗 → 分析 → 可视化」完整项目

---

## 学习建议

### 推荐学习顺序

```
阶段一（基础）→ 阶段二（进阶）→ 阶段三（高级）
                                    ↓
                              阶段四（实战项目）← 可随时穿插
                                    ↓
                    阶段五（NumPy → Pandas → Matplotlib）
```

### 每日学习节奏

1. **70/30 原则**：70% 时间写代码，30% 时间读文档
2. **先看注释再运行**：每个文件先通读注释理解逻辑，再运行看结果
3. **动手改代码**：改参数、改条件，观察输出变化
4. **完成练习**：每个阶段的学习文件后，完成对应的练习文件
5. **遇到问题**：先想 15 分钟，再查文档或搜索

### 文件使用方式

```
每个学习文件的结构：
├── """文档字符串"""        ← 学习目标
├── ===== 1. 知识点 ===     ← 分段学习
├── 代码示例 + 行末注释      ← 每行都有注释
├── ===== 2. 知识点 ===
├── ...
└── if __name__ == "__main__":  ← 练习题提示
```

### 测验

| 文件 | 覆盖阶段 |
|------|---------|
| [01_beginner_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/01_beginner_quiz.md) | 阶段一 |
| [02_intermediate_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/02_intermediate_quiz.md) | 阶段二 |
| [03_advanced_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/03_advanced_quiz.md) | 阶段三 |

---

## 文件统计

| 阶段 | 学习文件 | 练习文件 | 总行数（约） |
|------|---------|---------|------------|
| 01_beginner | 8 | 4 | 1,100 |
| 02_intermediate | 8 | 3 | 1,400 |
| 03_advanced | 7 | 3 | 1,500 |
| 04_projects | 6 | - | 1,100 |
| 06_numpy | 6 | 3 | 900 |
| 07_pandas | 6 | 3 | 1,000 |
| 08_matplotlib | 6 | 3 | 1,200 |
| utils | 1 | - | 42 |
| **合计** | **48** | **16** | **~8,200** |

> 所有文件均已添加逐行中文注释，适合初学者自学使用。
