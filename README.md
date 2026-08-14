# Python 从入门到精通 学习项目

一个系统化的 Python 学习与练习项目,按"**入门基础 → 进阶开发 → 高级特性 → 项目实战**"四个阶段组织,每个阶段都包含知识点示例代码、配套练习题。

> 详细学习路线见 [LEARNING_ROADMAP.md](file:///e:/编程练习/python_learning/LEARNING_ROADMAP.md)

## 学习路线概览

```
01_beginner  ──►  02_intermediate  ──►  03_advanced
   入门基础        进阶开发            高级特性
       \              |                /
        └──►  04_projects  ◄─────────┘
             (各阶段穿插练习)
```

> 💡 **实战项目不是学完才做**。从入门阶段开始,每学完一个阶段就应该做 1-2 个小项目,边学边用。

## 目录结构

| 目录 | 内容 | 预计耗时 |
|------|------|----------|
| `01_beginner/` | 语法基础、流程控制、函数、数据结构、文件、异常、虚拟环境、Git | 4-5 周 |
| `02_intermediate/` | 面向对象、装饰器、生成器、上下文管理器、标准库、SQLite、requests、测试 | 5-7 周 |
| `03_advanced/` | 描述符、元类、类型提示、并发、异步、性能优化、内存模型、设计模式 | 8-12 周 |
| `04_projects/` | 6 个实战项目(由易到难) | 各阶段穿插 |
| `tests/` | 练习题单元测试(pytest) | 配合学习 |
| `05_quizzes/` | 各阶段测试题,用于自测学习效果 | 配合学习 |
| `utils/` | 项目通用工具函数 | 持续完善 |

## 各阶段对应文件

### 入门篇 (`01_beginner/`)
- [01_variables_types.py](file:///e:/编程练习/python_learning/01_beginner/01_variables_types.py) — 变量与数据类型
- [02_control_flow.py](file:///e:/编程练习/python_learning/01_beginner/02_control_flow.py) — 流程控制
- [03_functions.py](file:///e:/编程练习/python_learning/01_beginner/03_functions.py) — 函数
- [04_data_structures.py](file:///e:/编程练习/python_learning/01_beginner/04_data_structures.py) — 数据结构
- [05_strings.py](file:///e:/编程练习/python_learning/01_beginner/05_strings.py) — 字符串
- [06_file_io.py](file:///e:/编程练习/python_learning/01_beginner/06_file_io.py) — 文件 I/O
- [07_exceptions.py](file:///e:/编程练习/python_learning/01_beginner/07_exceptions.py) — 异常处理
- [08_venv_engineering.py](file:///e:/编程练习/python_learning/01_beginner/08_venv_engineering.py) — 虚拟环境与工程化

### 进阶篇 (`02_intermediate/`)
- [01_oop_basics.py](file:///e:/编程练习/python_learning/02_intermediate/01_oop_basics.py) — 面向对象基础
- [02_inheritance.py](file:///e:/编程练习/python_learning/02_intermediate/02_inheritance.py) — 继承与多态
- [03_magic_methods.py](file:///e:/编程练习/python_learning/02_intermediate/03_magic_methods.py) — 魔术方法
- [04_decorators.py](file:///e:/编程练习/python_learning/02_intermediate/04_decorators.py) — 装饰器深入
- [05_generators.py](file:///e:/编程练习/python_learning/02_intermediate/05_generators.py) — 生成器与迭代器
- [06_context_managers.py](file:///e:/编程练习/python_learning/02_intermediate/06_context_managers.py) — 上下文管理器
- [07_stdlib.py](file:///e:/编程练习/python_learning/02_intermediate/07_stdlib.py) — 常用标准库
- [08_modules_packages.py](file:///e:/编程练习/python_learning/02_intermediate/08_modules_packages.py) — 模块与包

### 高级篇 (`03_advanced/`)
- [01_descriptors.py](file:///e:/编程练习/python_learning/03_advanced/01_descriptors.py) — 描述符与属性协议
- [02_metaclasses.py](file:///e:/编程练习/python_learning/03_advanced/02_metaclasses.py) — 元类编程
- [03_type_hints.py](file:///e:/编程练习/python_learning/03_advanced/03_type_hints.py) — 类型提示与静态检查
- [04_threading_multiprocessing.py](file:///e:/编程练习/python_learning/03_advanced/04_threading_multiprocessing.py) — 并发编程
- [05_asyncio.py](file:///e:/编程练习/python_learning/03_advanced/05_asyncio.py) — 异步编程
- [06_design_patterns.py](file:///e:/编程练习/python_learning/03_advanced/06_design_patterns.py) — 设计模式
- [07_testing.py](file:///e:/编程练习/python_learning/03_advanced/07_testing.py) — 测试与调试

### 实战项目 (`04_projects/`)
按难度由低到高:

- 🟢 [todo_cli/](file:///e:/编程练习/python_learning/04_projects/todo_cli/) — 命令行待办工具(入门+)
- 🟢 [chatbot/](file:///e:/编程练习/python_learning/04_projects/chatbot/) — 规则式聊天机器人(入门+)
- 🟡 [game_2048/](file:///e:/编程练习/python_learning/04_projects/game_2048/) — 2048 小游戏(进阶)
- 🟡 [web_crawler/](file:///e:/编程练习/python_learning/04_projects/web_crawler/) — 网页爬虫(进阶)
- 🟠 [data_analysis/](file:///e:/编程练习/python_learning/04_projects/data_analysis/) — 数据分析(进阶+)
- 🔴 [simple_web_server/](file:///e:/编程练习/python_learning/04_projects/simple_web_server/) — 简易 Web 服务(中高级)

### 单元测试 (`tests/`)
- [test_beginner_exercises.py](file:///e:/编程练习/python_learning/tests/test_beginner_exercises.py) — 入门练习测试
- [test_intermediate_exercises.py](file:///e:/编程练习/python_learning/tests/test_intermediate_exercises.py) — 进阶练习测试
- [test_advanced_exercises.py](file:///e:/编程练习/python_learning/tests/test_advanced_exercises.py) — 高级练习测试

### 测试题 (`05_quizzes/`)
- [01_beginner_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/01_beginner_quiz.md) — 入门测试
- [02_intermediate_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/02_intermediate_quiz.md) — 进阶测试
- [03_advanced_quiz.md](file:///e:/编程练习/python_learning/05_quizzes/03_advanced_quiz.md) — 高级测试

## 使用方法

### 推荐学习流程
1. 按顺序阅读每个示例文件,**必须亲自运行**,并尝试修改代码
2. 完成对应 `exercises/` 目录下的练习题(先自己写,再对比)
3. 用 `05_quizzes/` 中的题目自测,错题返回去重学
4. 每学完一个阶段,选 1-2 个 `04_projects/` 中的项目做一遍
5. 参考 [LEARNING_ROADMAP.md](file:///e:/编程练习/python_learning/LEARNING_ROADMAP.md) 检查里程碑

### 运行示例
```bash
# 运行某个知识点示例
python 01_beginner/01_variables_types.py

# 完成练习题
python 01_beginner/exercises/ex02_fibonacci_palindrome.py

# 跑实战项目
python 04_projects/todo_cli/todo.py add "买牛奶" -p high
python 04_projects/todo_cli/todo.py list

# 运行单元测试
python -m pytest tests/ -v

# 查看测试覆盖率
python -m pytest tests/ --cov=.
```

## 代码质量工具
```bash
# 代码格式化
black .

# import 排序
isort .

# 代码检查
flake8 .

# 静态类型检查
mypy 03_advanced/
```

所有工具的配置都在 [pyproject.toml](file:///e:/编程练习/python_learning/pyproject.toml) 中。

## 环境要求

- Python 3.10+(推荐 3.11+)
- 推荐 IDE:VS Code + Python 扩展
- 安装依赖:`pip install -r requirements.txt`
- **重要**:使用虚拟环境(`venv` / `conda`),别污染全局环境

## 📚 学习资源

> 选 1-2 个跟到底,比囤 10 个走马观花有用得多。

### 官方文档
- [Python 官方文档](https://docs.python.org/3/) — 最权威的参考,遇到问题先查这里
- [Python 中文文档](https://docs.python.org/zh-cn/3/) — 官方中文翻译

### 在线教程
- [Real Python](https://realpython.com/) — 英文,高质量实战教程,全阶段适用
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400) — 中文经典入门

### 书籍(每阶段一本就够)
| 阶段 | 推荐 | 理由 |
|------|------|------|
| 入门 | 《Python 编程:从入门到实践》 | 项目驱动,首推 |
| 进阶 | 《流畅的 Python》(第 2 版) | 讲透 Python 特色,必读 |
| 高级 | 《Effective Python》 | 90 条改善代码的建议 |

### 专项参考(配合路线图各周内容)
| 主题 | 资源 | 说明 |
|------|------|------|
| 标准库速查 | [Python Module of the Week](https://pymotw.com/3/) | 逐模块讲解标准库,第 4/9 周配合使用 |
| 正则表达式 | [regex101.com](https://regex101.com/) | 在线调试正则,实时高亮匹配,第 9 周配合使用 |
| 并发与异步 | [asyncio 官方文档](https://docs.python.org/3/library/asyncio.html) | 异步编程权威参考,第 14-15 周配合使用 |
| 测试 | [pytest 官方文档](https://docs.pytest.org/) | pytest 权威参考,第 10 周配合使用 |
| Git | [Pro Git 中文版](https://git-scm.com/book/zh/v2) | Git 入门到精通,第 4 周配合使用 |

### 练习平台
- [LeetCode](https://leetcode.cn/) — 算法刷题(中文站)
- [Exercism](https://exercism.org/) — Python 专项练习,有 mentor 反馈

### 视频课程
- [CS50P](https://cs50.harvard.edu/python/) — 哈佛 Python 入门,免费,结构完整

### 源码阅读(高级)
- [requests](https://github.com/psf/requests) — 代码优雅,适合入门源码阅读
- [flask](https://github.com/pallets/flask) — 小巧精悍,理解 Web 框架原理

### 提问与社区
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) — 遇到问题先搜这里
- [GitHub](https://github.com/) — 读源码、提 Issue、参与开源

---

## 学习建议

### ✅ 应该做的
- 每个示例都要亲自运行、修改、试错
- 每完成一节,用练习题巩固
- 遇到报错先读 traceback,自己想 15 分钟再搜
- 用项目驱动学习,不要只看视频/看书
- 定期回顾旧代码,看能否写得更好

### ❌ 应该避免的
- 囤课不练(看了 10 门课不如敲完一个项目)
- 跳过基础直接学框架(Flask/Django 不是 Python 全部)
- 追求"精通"(够用就好,按需深入)
- 过早研究 CPython 源码(先写够 1000 行代码再说)
- 只看不敲(代码是写出来的,不是看出来的)

## 版本历史

- **v3.1** — 新增完整学习资源章节(官方文档/教程/书籍/平台/视频/源码/工具/社区/学习路径组合)
- **v3.0** — 修正技术错误(描述符查找顺序/元类层面/GIL说明),补充 Git/SQLite/requests/docstring/异常最佳实践,新增"如何提问"章节,实战项目对应到本仓库
- **v2.1** — 补充虚拟环境/工程化、pyproject.toml 配置、67 个单元测试、聊天机器人和 2048 游戏项目
- **v2.0** — 修订学习路线,修正阶段顺序,补充性能优化/内存模型/虚拟环境等缺失知识点
- **v1.0** — 初始版本,四阶段基础框架
