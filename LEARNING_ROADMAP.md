# Python 学习路线图

> 本路线图按照"**能写 → 能设计 → 能优化 → 能精通底层**"四个阶梯组织。每个阶段都有**明确的产出目标**和**检验标准**。
>
> 时间估算基于**每天 1-2 小时**有效学习时间。零基础者时间翻倍,有其他语言基础者可减半。

---

## 阶段一:入门基础(4-5 周)

### 🎯 阶段目标
掌握 Python 语法基础,能独立写 100 行以内的小脚本,解决简单问题。

### 📚 知识点清单

#### 第 1 周:语言基础
- [ ] Python 简介、版本选择(推荐 3.11+)、安装与 REPL
- [ ] 变量命名规范、注释、PEP 8 基础
- [ ] 基本数据类型:`int` / `float` / `bool` / `str` / `None`
- [ ] 数值运算、运算符优先级、`//` `/` `%` `**` 的区别
- [ ] 字符串常用方法:`strip` / `split` / `join` / `replace` / `find` / 格式化(f-string)
- [ ] `input()` 与 `print()` 基础交互
- [ ] 常见报错:读懂 `SyntaxError` / `NameError` / `TypeError` / `ValueError`

#### 第 2 周:数据结构与流程控制
- [ ] 条件分支:`if / elif / else`、三元表达式 `x if cond else y`
- [ ] `for` 循环、`while` 循环、`break` / `continue` / `else` 子句
- [ ] 列表(`list`):索引、切片、增删改查、常用方法
- [ ] 元组(`tuple`):不可变性、解包
- [ ] 字典(`dict`):键值对、遍历、`get` / `setdefault`
- [ ] 集合(`set`):去重、集合运算
- [ ] 推导式:列表推导式 / 字典推导式 / 集合推导式
- [ ] 排序:`sorted()` 与 `list.sort()`,理解 `key` 参数(如 `key=len`)

#### 第 3 周:函数与文件
- [ ] 函数定义、参数(位置/默认/关键字/`*args` / `**kwargs`)
- [ ] 返回值、多返回值、提前返回
- [ ] 作用域:局部 / 全局 / `global` / `nonlocal`(配合嵌套函数理解)
- [ ] 匿名函数 `lambda`(简单使用,如 `sorted(key=lambda x: x[1])`)
- [ ] `map` / `filter`(了解即可,推荐用推导式替代)
- [ ] 文件读写:文本文件、`with` 语句、`encoding="utf-8"` 的重要性
- [ ] `pathlib` 路径处理(推荐替代 `os.path`)
- [ ] 异常处理:`try / except / finally / else`
- [ ] **异常最佳实践**:不用裸 `except:`、自定义异常、`raise ... from ...`
- [ ] 常见内置函数:`len` / `range` / `enumerate` / `zip` / `max` / `min` / `sum`

#### 第 4 周:模块与工程基础
- [ ] 模块导入:`import` / `from ... import ...` / 别名
- [ ] 包与 `__init__.py`
- [ ] 标准库速览:`os` / `sys` / `json` / `re` / `random` / `datetime` 入门
- [ ] **虚拟环境**:`venv`(官方推荐) vs `conda`(数据科学) vs `uv`(新一代,更快)
  - 入门只需掌握 `venv`,其他了解即可
- [ ] **pip 包管理**:`pip install` / `requirements.txt` / `pip freeze`
- [ ] 代码风格:PEP 8、`black` 自动格式化(无需配置,开箱即用)
- [ ] **Git 版本控制基础**:`init` / `add` / `commit` / `push` / `clone`(必备技能)

### ✅ 检验标准
- 能不看答案独立完成 10 道 LeetCode 简单题(字符串 / 数组 / 哈希)
- 能写一个**文本词频统计工具**(读文件 → 统计 → 输出 Top N)
- 能独立配置虚拟环境并安装第三方库
- 能用 Git 管理自己的代码(提交到 GitHub)
- 入门测试题正确率 ≥ 80%

### 🛠️ 小项目练手(对应本仓库)
- 猜数字游戏 → [exercises/ex03_guess_password.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex03_guess_password.py)
- 密码强度检测器 → 同上
- 文本词频统计 → [exercises/ex04_file_stats.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex04_file_stats.py)
- 简易计算器 → [exercises/ex01_swap_calculator.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex01_swap_calculator.py)

---

## 阶段二:进阶开发(5-7 周)

### 🎯 阶段目标
掌握面向对象编程与常用标准库,能组织 500-2000 行规模的模块化项目,写出"**可读、可维护、可测试**"的代码。

### 📚 知识点清单

#### 第 5 周:面向对象基础
- [ ] 类与对象、`__init__` 构造方法
- [ ] 实例属性 vs 类属性、实例方法 vs 类方法(`@classmethod`) vs 静态方法(`@staticmethod`)
- [ ] 封装与访问控制(单下划线 / 双下划线约定,名称修饰)
- [ ] `property` 装饰器(**只作为属性访问方式学,不要深究描述符原理**)
- [ ] 继承、方法重写、`super()`
- [ ] 多继承与 MRO(方法解析顺序)
- [ ] 抽象基类 `ABC` 与 `@abstractmethod`
- [ ] **docstring 规范**:Google / NumPy / reST 风格,IDE 可识别
- [ ] `isinstance()` / `issubclass()` / `hasattr()` / `getattr()` / `setattr()`

#### 第 6 周:常用数据结构与算法思维
- [ ] `collections` 模块:`Counter` / `defaultdict` / `deque` / `namedtuple` / `OrderedDict`
- [ ] 栈、队列的 Python 实现(用 `list` 或 `collections.deque`)
- [ ] 堆:`heapq` 模块(优先队列)
- [ ] **二分查找**:`bisect` 模块(用标准库,不要手写)
- [ ] **排序**:理解 `sorted()` 的 `key` 和 `reverse`,稳定排序特性
- [ ] 递归思想(阶乘、斐波那契、目录遍历)
- [ ] 哈希表原理简介(为什么 dict 查询是 O(1))
- [ ] ⚠️ **不要花时间手写快排/归并**,Python 学习不是算法课

#### 第 7 周:迭代器与生成器
- [ ] 迭代器协议:`__iter__` / `__next__` / `StopIteration`
- [ ] 生成器函数:`yield`、惰性求值
- [ ] 生成器表达式 vs 列表推导式(内存对比)
- [ ] `yield from` 委托子生成器
- [ ] `itertools` 模块常用工具:`chain` / `combinations` / `permutations` / `groupby`
- [ ] 实战:用生成器处理大文件 / 数据流

#### 第 8 周:装饰器与上下文管理器
- [ ] 函数是一等公民(可赋值、传参、返回)
- [ ] 闭包(Closure)与自由变量
- [ ] 装饰器原理与手写装饰器
- [ ] `functools.wraps` 保留元信息(必做,否则调试困难)
- [ ] 带参数的装饰器、类装饰器、装饰器链
- [ ] `functools.lru_cache` 缓存装饰器
- [ ] 上下文管理器协议:`__enter__` / `__exit__`
- [ ] `@contextmanager` 装饰器(更简洁的写法)
- [ ] `ExitStack` 动态管理多个上下文

#### 第 9 周:标准库精选 + 第三方库入门
- [ ] `datetime` 日期时间处理、时区概念
- [ ] `logging` 日志模块(级别 / 格式化 / 多 handler)
- [ ] `argparse` 命令行参数解析
- [ ] `hashlib` / `secrets` 加密与安全随机数(密码哈希用 PBKDF2/bcrypt,不要用 MD5)
- [ ] `json` / `csv` 序列化
- [ ] ⚠️ `pickle`:**反序列化不可信数据等于执行任意代码**,只在可信环境使用
- [ ] `re` 正则表达式进阶(分组 / 捕获 / 替换 / 断言)
- [ ] `subprocess` 调用外部命令(注意 `shell=True` 的安全风险)
- [ ] `configparser` / `tomllib` 配置文件
- [ ] **`sqlite3` 模块**:Python 内置的轻量级数据库(无需安装)
- [ ] **`requests` 库**:最常用的 HTTP 客户端(`pip install requests`)

#### 第 10 周:编码、调试与测试基础
- [ ] 字符编码:ASCII / Unicode / UTF-8 的关系(理解 `UnicodeDecodeError`)
- [ ] `bytes` / `str` 转换、`encode` / `decode`
- [ ] `pdb` / `breakpoint()` 交互式调试
- [ ] IDE 断点调试(VS Code)
- [ ] 用 `logging` 替代 `print` 做调试
- [ ] 读 traceback 定位错误
- [ ] **pytest 基础**:`assert` / `fixture` / `parametrize` / `mark`
- [ ] **测试思维**:写函数时就想怎么测它

### ✅ 检验标准
- 能用 OOP 思想设计一个**扑克牌游戏**或**学生管理系统**
- 能独立实现一个**带 CLI 界面的待办工具**(参考 `04_projects/todo_cli`)
- 能用装饰器和上下文管理器写"可复用的工具函数"
- 能为自己的代码写 pytest 测试(至少 10 个用例)
- 进阶测试题正确率 ≥ 70%

### 🛠️ 小项目练手(对应本仓库)
- 命令行待办工具 → [04_projects/todo_cli/](file:///e:/编程练习/python_learning/04_projects/todo_cli/)
- 规则式聊天机器人 → [04_projects/chatbot/](file:///e:/编程练习/python_learning/04_projects/chatbot/)
- 表达式求值器 → [exercises/ex03_expression_eval.py](file:///e:/编程练习/python_learning/02_intermediate/exercises/ex03_expression_eval.py)
- LRU 缓存 → [exercises/ex02_lru_cache.py](file:///e:/编程练习/python_learning/02_intermediate/exercises/ex02_lru_cache.py)

---

## 阶段三:高级特性(8-12 周)

### 🎯 阶段目标
深入 Python 内部机制,理解"Python 为什么这么设计",能解决**性能瓶颈、架构设计、复杂工程**问题。

> ⚠️ 高级篇内容多且深,**不要追求一遍学透**。先建立概念,遇到实际问题时再回来深入。

### 📚 知识点清单

#### 第 11 周:描述符与属性协议
- [ ] 描述符协议:`__get__` / `__set__` / `__delete__`
- [ ] 数据描述符 vs 非数据描述符
- [ ] **属性查找顺序(重要,原文有误,现已修正)**:
  1. `__getattribute__` 被调用
  2. **数据描述符**(类中定义了 `__get__` 和 `__set__`)
  3. 实例 `__dict__`
  4. **非数据描述符**(只定义了 `__get__`,如函数、`property`)
  5. 类属性(含父类)
  6. `__getattr__`(兜底)
- [ ] `__set_name__`(Python 3.6+)
- [ ] `property` 的本质是数据描述符
- [ ] `__getattr__` / `__getattribute__` / `__setattr__` / `__delattr__` 的区别

#### 第 12 周:元类与对象模型
- [ ] 一切皆对象:类也是对象(`type` 是自己的元类)
- [ ] `type()` 两种用法:查类型 / 动态创建类
- [ ] **元类的两个层面(重要,原文混淆,现已区分)**:
  - 重写 `__new__` / `__init__`:控制**类的创建**(修改类属性、自动注册)
  - 重写 `__call__`:控制**实例的创建**(影响 `__new__` / `__init__` 调用)
- [ ] 元类的实际应用:ORM 字段自动收集 / 插件注册 / 接口校验
- [ ] `__init_subclass__`(Python 3.6+,**更优雅的替代方案,优先使用**)
- [ ] `dataclasses` 模块深入(`frozen` / `field` / `__post_init__`)
- [ ] 元类 vs 装饰器 vs `__init_subclass__` 的选型

#### 第 13 周:类型系统与静态检查
- [ ] 类型提示(Type Hints)基础
- [ ] `typing` 模块:`Optional` / `Union` / `Callable`
- [ ] Python 3.9+ 内置泛型:`list[int]` / `dict[str, int]`(无需 `List`/`Dict`)
- [ ] 泛型 `Generic[T]` 与 `TypeVar`
- [ ] `Protocol` 结构化子类型(鸭子类型的静态版)
- [ ] `TypedDict` / `Literal` / `Final` / `Annotated`
- [ ] `mypy` 静态检查配置
- [ ] 实战:为一个旧项目添加类型注解

#### 第 14 周:并发编程
- [ ] **GIL(全局解释器锁)**:同一时刻只有一个线程执行 Python 字节码
  - **CPU 密集型任务:多线程无法加速,必须用多进程**
  - **I/O 密集型任务:多线程/协程可以加速**(等待时释放 GIL)
- [ ] 多线程:`threading` / `Lock` / `Event` / `Queue`
- [ ] 多进程:`multiprocessing` / `Pool` / `Queue` / `Manager`
- [ ] `concurrent.futures` 统一接口(`ThreadPoolExecutor` / `ProcessPoolExecutor`)
- [ ] 线程安全问题与常见坑(竞态条件 / 死锁 / GIL 的误解)
- [ ] **选型口诀**:CPU 密集用进程,I/O 密集用线程或协程

#### 第 15 周:异步编程
- [ ] 协程概念:协作式多任务(对比抢占式)
- [ ] `async def` 定义协程,`await` 等待 awaitable
- [ ] **`asyncio.run()` 是入口**(Python 3.7+,最常用的启动方式)
- [ ] `asyncio` 事件循环、`Task`、`gather` / `wait` / `as_completed`
- [ ] 异步上下文管理器(`__aenter__` / `__aexit__`)、异步迭代器(`__aiter__` / `__anext__`)
- [ ] `asyncio.Queue` / `Semaphore` / `Lock`
- [ ] 第三方异步库:`aiohttp` / `httpx`
- [ ] **异步 vs 多线程**:协程单线程、切换成本更低,但需要全链路异步

#### 第 16 周:性能优化
- [ ] **第一条原则:先测量,再优化**(`cProfile` / `timeit`)
- [ ] **过早优化是万恶之源**(Knuth)
- [ ] Python 为什么慢(动态类型 + 解释执行 + GIL)
- [ ] 性能分析工具:`cProfile` / `timeit` / `memory_profiler` / `py-spy`
- [ ] 优化思路:算法 > 数据结构 > 语言特性 > C 扩展
- [ ] 内置数据结构的时间复杂度
- [ ] `functools.lru_cache` / `__slots__` / 生成器节省内存
- [ ] 向量化计算(NumPy)替代循环
- [ ] 了解 Cython / Numba(进阶方向,不必深入)

#### 第 17 周:内存模型与垃圾回收
- [ ] 引用计数原理与循环引用问题
- [ ] 标记-清除与分代回收(解决循环引用)
- [ ] `gc` 模块
- [ ] `weakref` 弱引用(避免内存泄漏)
- [ ] 常见内存泄漏场景与排查

#### 第 18 周:设计模式与软件工程
- [ ] **创建型**:单例 / 工厂 / 建造者 / 原型
- [ ] **结构型**:适配器 / 装饰器 / 代理 / 组合 / 享元
- [ ] **行为型**:观察者 / 策略 / 模板方法 / 责任链 / 命令
- [ ] **Python 特色**:用一等函数简化模式(不需要 Java 那套)
- [ ] 反模式与过度设计的识别
- [ ] **SOLID 原则**(了解,不必教条)
- [ ] **项目结构规范**:`src` 布局 / `pyproject.toml` / 测试组织

### ✅ 检验标准
- 能读懂一个开源项目的核心源码(如 `requests` / `flask`)
- 能完成**迷你 ORM** 或**异步爬虫框架**练习
- 能使用 `cProfile` 定位并优化一个慢函数(优化前后有数据对比)
- 能为自己的项目添加完整的类型注解并通过 mypy 检查
- 高级测试题正确率 ≥ 60%

### 🛠️ 小项目练手(对应本仓库)
- 迷你 ORM → [exercises/ex01_mini_orm.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex01_mini_orm.py)
- 异步爬虫 → [exercises/ex02_async_crawler.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex02_async_crawler.py)
- 依赖注入容器 → [exercises/ex03_di_container.py](file:///e:/编程练习/python_learning/03_advanced/exercises/ex03_di_container.py)
- 2048 游戏 → [04_projects/game_2048/](file:///e:/编程练习/python_learning/04_projects/game_2048/)

---

## 阶段四:实战与精进(持续)

### 🎯 阶段目标
通过真实项目将知识融会贯通,形成自己的技术栈和工程能力。

> 💡 **重要:实战不是学完才开始,而是从入门阶段就应该穿插进行。**
> 每个阶段结束后,都应该完成至少 1 个综合项目。

### 📂 项目推荐(由易到难,含本仓库已有项目)

#### 🟢 入门级(~100 行)
1. **命令行待办工具** → 本仓库 [04_projects/todo_cli/](file:///e:/编程练习/python_learning/04_projects/todo_cli/)
2. **规则式聊天机器人** → 本仓库 [04_projects/chatbot/](file:///e:/编程练习/python_learning/04_projects/chatbot/)
3. **文本分析器** → 本仓库 [01_beginner/exercises/ex04_file_stats.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex04_file_stats.py)
4. **数字猜谜游戏** → 本仓库 [01_beginner/exercises/ex03_guess_password.py](file:///e:/编程练习/python_learning/01_beginner/exercises/ex03_guess_password.py)

#### 🟡 进阶级(~500 行)
5. **2048 小游戏** → 本仓库 [04_projects/game_2048/](file:///e:/编程练习/python_learning/04_projects/game_2048/)
6. **简易网页爬虫** → 本仓库 [04_projects/web_crawler/](file:///e:/编程练习/python_learning/04_projects/web_crawler/)
7. **记账本** — SQLite + 统计报表(自己实现)
8. **CLI 任务管理器** — argparse + JSON + OOP(扩展 todo_cli)

#### 🟠 中高级(~1000 行)
9. **数据分析报告生成器** → 本仓库 [04_projects/data_analysis/](file:///e:/编程练习/python_learning/04_projects/data_analysis/)
10. **静态博客生成器** — Markdown 解析 + 模板 + 文件处理
11. **异步 API 服务器** — FastAPI + SQLite + 认证
12. **简易 Web 服务器** → 本仓库 [04_projects/simple_web_server/](file:///e:/编程练习/python_learning/04_projects/simple_web_server/)

#### 🔴 高级(>2000 行)
13. **完整 Web 应用** — Flask/FastAPI + SQLAlchemy + 前端
14. **分布式任务队列** — Redis + 多进程/协程
15. **发布到 PyPI 的工具库** — 打包 + 文档 + 测试 + CI/CD

### 📖 学习资源

> 完整清单见 [README.md](file:///e:/编程练习/python_learning/README.md#-学习资源)

- **文档**:[Python 官方文档](https://docs.python.org/3/) — 遇到问题先查这里
- **教程**:[Real Python](https://realpython.com/)(英文) / [廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400)(中文)
- **书籍**:入门《Python 编程:从入门到实践》 / 进阶《流畅的 Python》/ 高级《Effective Python》
- **练习**:[LeetCode](https://leetcode.cn/) / [Exercism](https://exercism.org/)
- **视频**:[CS50P](https://cs50.harvard.edu/python/) — 哈佛免费 Python 入门
- **源码阅读**:[requests](https://github.com/psf/requests) — 代码优雅,适合入门源码阅读

---

## 🗓️ 每日学习建议

1. **保证编码时间**:每天至少 1 小时动手写,光看不写等于没学
2. **70/30 原则**:70% 写代码,30% 读文档/看书
3. **主动试错**:故意改改代码,看报错,理解为什么错
4. **费曼学习法**:用自己的话把学到的讲出来(写博客 / 讲给朋友听)
5. **错题本**:记录踩过的坑,定期回顾
6. **15 分钟原则**:卡住了先自己想 15 分钟,再查资料/问人
7. **周复盘**:周末花 1 小时回顾本周所学,整理笔记
8. **注意休息**:学习是长跑,疲劳时效率极低,适当运动和睡眠很重要

---

## 🔍 如何提问与搜索(重要)

### 搜索技巧
1. **优先用英文搜索**:Stack Overflow / GitHub Issues / 官方文档
2. **加上关键词**:`python` + 具体问题,如 `python list remove while iterating`
3. **报错信息**:直接搜索完整的错误信息(去掉路径等特定信息)
4. **AI 辅助**:用 AI 工具快速定位问题,但要理解答案,不要盲目复制

### 提问规范(参考 [Stack Overflow](https://stackoverflow.com/help/how-to-ask))
1. **先搜索**:90% 的问题别人已经问过
2. **提供上下文**:你在做什么、想达到什么效果
3. **提供最小可复现代码**:不要贴整个项目,提炼出最简例子
4. **提供完整报错**:不要只说"报错了",贴出完整 traceback
5. **说明已尝试的方法**:让别人知道你试过什么

### 好的提问示例
> 我在用 Python 3.11 写一个爬虫,用 requests 库抓取网页时报 `SSLError: certificate verify failed`。
> 已尝试:1) 升级 certifi 2) 设置 `verify=True`
> 完整报错:[贴出 traceback]
> 最小复现代码:[5 行代码]
> 请问还能怎么排查?

---

## ⚠️ 常见坑与避坑指南

### ❌ 误区
1. **囤课不练**:买了 N 门课,一个都没敲完
2. **跳过基础直接学框架**:基础不牢,地动山摇
3. **追求"精通"**:Python 生态太大,先学够做项目的,再按需深入
4. **过早深入底层**:没写过 1000 行代码就研究 CPython 源码,效率很低
5. **只看不敲**:代码是写出来的,不是看出来的
6. **手写算法浪费时间**:Python 学习不是算法课,用标准库就好
7. **裸 except 吞掉异常**:`except:` 会隐藏真实错误,永远不要用
8. **用 `pickle` 处理不可信数据**:等于执行任意代码,严重安全风险
9. **用 `eval` / `exec` 处理用户输入**:同上,安全黑洞

### ✅ 正确姿势
1. **用项目驱动学习**:先想做什么,再去学需要的知识
2. **造轮子**:哪怕有现成库,自己实现一遍理解更深
3. **读优秀源码**:从你日常用的库开始,读 1-2 个核心文件
4. **写技术笔记**:不是抄书,而是写"我理解了什么 + 踩了什么坑"
5. **定期复盘**:每 2 周做一次小项目,检验学习效果
6. **参与开源**:从提交 Issue 和 PR 开始
7. **写测试**:函数写完就写测试,养成习惯

---

## 🏆 学习里程碑 Checklist

把这些作为"升级通关"的标志,每达成一个就打个勾:

- [ ] **L1**:能独立写 100 行以内的脚本解决问题
- [ ] **L2**:能使用第三方库完成简单项目
- [ ] **L3**:能写出规范的、带注释和 docstring 的、可维护的代码
- [ ] **L4**:能用 OOP 思想设计中大型项目
- [ ] **L5**:能为自己的代码写单元测试(pytest)
- [ ] **L6**:能读懂中等规模开源项目的核心代码
- [ ] **L7**:能进行性能分析和优化(有数据对比)
- [ ] **L8**:能独立设计并完成一个完整项目(从需求到上线)
- [ ] **L9**:有自己的开源项目或给知名项目提交过 PR
- [ ] **L10**:能给别人讲清楚 Python 内部机制(描述符/元类/GIL/GC)
- [ ] **L11**:参与或主导大型 Python 项目架构

---

## 📝 修订记录

- **v3.0**(2026-07):修正描述符查找顺序、元类层面区分、GIL 说明等技术错误;补充 Git、SQLite、requests、docstring、异常最佳实践;调整设计模式和测试基础到进阶阶段;新增"如何提问"章节;实战项目对应到本仓库
- **v2.0**(2026-07):按周重组知识点,补充虚拟环境、性能优化、内存模型等缺失内容,新增学习里程碑
- **v1.0**:初始版本,四阶段基础框架
