"""08 - 虚拟环境、包管理与工程化

学习目标:
    - 理解为什么需要虚拟环境
    - 掌握 venv / conda 的基本使用
    - 掌握 pip 与 requirements.txt
    - 了解 PEP 8 与代码风格工具
    - 学会项目目录结构规范

注意:
    本文件包含大量命令示例,请在终端中实际操作一遍。
"""

# ============================================================
# 一、为什么需要虚拟环境?
# ============================================================
# 问题场景:
#   - 项目 A 需要 requests 2.x
#   - 项目 B 需要 requests 3.x
#   - 全局安装只能有一个版本,怎么办?
#
# 答案:每个项目一个独立的虚拟环境,互不干扰。
#
# 类比:
#   虚拟环境就像一个个独立的"工具箱",每个项目用自己的工具箱,
#   工具(库)的版本可以不一样,不会互相影响。

print("=== 为什么需要虚拟环境 ===")                # 打印本节大标题
print("1. 不同项目依赖不同版本的库,互不干扰")        # 原因 1:不同项目可以用不同版本的库
print("2. 方便分享:requirements.txt 让别人一键安装所有依赖")  # 原因 2:便于分享依赖清单
print("3. 方便部署:知道项目到底依赖了什么")          # 原因 3:便于部署,依赖清晰
print("4. 不污染全局 Python 环境\n")                # 原因 4:不污染全局环境


# ============================================================
# 二、venv(官方推荐,Python 3.3+ 内置)
# ============================================================
print("=== venv 基本使用 ===")  # 打印 venv 使用部分标题
print()                         # 打印空行
print("# 1. 创建虚拟环境(在项目根目录执行)")  # 说明第 1 步:创建虚拟环境
print("   python -m venv .venv")              # 创建虚拟环境的命令,.venv 是目录名
print()                                       # 打印空行
print("# 2. 激活虚拟环境")                     # 说明第 2 步:激活虚拟环境
print("   Windows (PowerShell):  .venv\\Scripts\\Activate.ps1")  # Windows PowerShell 激活命令
print("   Windows (CMD):         .venv\\Scripts\\activate.bat")  # Windows CMD 激活命令
print("   macOS / Linux:         source .venv/bin/activate")    # macOS/Linux 激活命令
print()                                                          # 打印空行
print("# 3. 激活后,命令行前面会出现 (.venv) 标记")  # 说明激活后的现象
print("   (.venv) PS E:\\project>")                 # 演示激活后命令行样式
print()                                            # 打印空行
print("# 4. 安装依赖(只装在这个虚拟环境里)")        # 说明第 4 步:在虚拟环境中安装依赖
print("   pip install requests")                    # 安装 requests 库的命令
print()                                            # 打印空行
print("# 5. 退出虚拟环境")                         # 说明第 5 步:退出虚拟环境
print("   deactivate")                             # 退出虚拟环境的命令
print()                                            # 打印空行
print("# 6. 删除虚拟环境(直接删文件夹)")          # 说明第 6 步:删除虚拟环境
print("   rm -rf .venv   # 或手动删除 .venv 文件夹\n")  # 删除虚拟环境的命令


# ============================================================
# 三、pip 与 requirements.txt
# ============================================================
print("=== pip 常用命令 ===")  # 打印 pip 常用命令部分标题
pip_cmds = [                                   # 定义一个列表,存放 pip 命令和说明
    ("pip install requests", "安装最新版"),                      # 安装最新版命令
    ("pip install requests==2.31.0", "安装指定版本"),            # 安装指定版本命令
    ("pip install 'requests>=2.28,<3.0'", "安装范围内版本"),     # 安装指定范围内的版本
    ("pip install -r requirements.txt", "从文件批量安装"),       # 从 requirements.txt 批量安装
    ("pip uninstall requests", "卸载"),                          # 卸载包命令
    ("pip list", "列出已安装的包"),                              # 列出已安装的包
    ("pip freeze", "输出 requirements 格式的已安装列表"),        # 输出已安装包列表(requirements 格式)
    ("pip show requests", "查看包的详细信息"),                   # 查看某个包的详细信息
    ("pip install --upgrade requests", "升级包"),               # 升级包到最新版
    ("pip search xxx", "搜索包(PyPI 上)"),                     # 在 PyPI 上搜索包
]
for cmd, desc in pip_cmds:                    # 遍历每个命令和说明
    print(f"  {cmd:<45s}  # {desc}")          # 打印命令和说明,<45s 表示左对齐占 45 字符

print("\n=== requirements.txt 示例 ===")  # 打印 requirements.txt 示例标题
print("""
requests==2.31.0
beautifulsoup4==4.12.2
pandas>=2.0.0
matplotlib>=3.7.0
flask>=3.0.0
pytest>=7.4.0          # 开发依赖也可以放这里
black                   # 代码格式化
""")                                    # 打印 requirements.txt 的示例内容

print("\n=== 生成自己的 requirements.txt ===")  # 打印生成 requirements.txt 标题
print("  pip freeze > requirements.txt")        # 用 pip freeze 生成依赖文件的命令
print("  # 注意:会把所有已安装的包都写进去,可能包含不需要的")  # 提示:会包含所有已安装的包
print("  # 更推荐手动维护,只写直接依赖\n")        # 建议:手动维护,只写直接依赖


# ============================================================
# 四、PEP 8 代码风格
# ============================================================
print("=== PEP 8 核心规则(记住这几条就够用) ===")  # 打印 PEP 8 核心规则标题
pep8_rules = [                                      # 定义 PEP 8 规则列表
    ("缩进", "4 个空格,不用 Tab"),                                # 缩进规则
    ("行宽", "建议不超过 79 字符(文档字符串 72)"),                # 行宽规则
    ("空行", "函数之间空两行,类方法之间空一行"),                  # 空行规则
    ("命名", "函数/变量 snake_case,类名 PascalCase,常量 UPPER_CASE"),  # 命名规则
    ("import", "按顺序:标准库 → 第三方 → 本地,每组空一行"),     # import 规则
    ("空格", "运算符两侧加空格,逗号后加空格"),                    # 空格规则
    ("注释", "# 后面空一格,行内注释至少空两格"),                  # 注释规则
    ("字符串", "单引号和双引号都行,选一种保持一致"),              # 字符串规则
]
for item, desc in pep8_rules:                       # 遍历每条规则
    print(f"  - {item:<8s} {desc}")                 # 打印规则名称和说明


# ============================================================
# 五、代码质量工具
# ============================================================
print("\n=== 常用代码质量工具 ===")  # 打印代码质量工具部分标题
tools = [                          # 定义工具列表
    ("black", "代码格式化(无需配置,开箱即用)"),    # black 工具说明
    ("isort", "import 排序"),                       # isort 工具说明
    ("flake8", "代码检查(PEP8 + 逻辑错误 + 复杂度)"),  # flake8 工具说明
    ("mypy", "静态类型检查"),                       # mypy 工具说明
    ("pytest", "单元测试框架"),                     # pytest 工具说明
    ("coverage", "测试覆盖率"),                     # coverage 工具说明
]
for tool, desc in tools:           # 遍历每个工具
    print(f"  - {tool:<12s} {desc}")  # 打印工具名和说明

print()                            # 打印空行
print("# 一键安装常用开发工具:")    # 提示一键安装
print("  pip install black isort flake8 mypy pytest coverage\n")  # 安装所有开发工具的命令


# ============================================================
# 六、项目目录结构
# ============================================================
print("=== 常见项目结构示例 ===")  # 打印项目结构示例标题
print("""
myproject/
├── .venv/              # 虚拟环境(不要提交到 Git)
├── src/                # 源代码
│   └── mypackage/
│       ├── __init__.py
│       ├── module_a.py
│       └── module_b.py
├── tests/              # 测试代码
│   ├── __init__.py
│   ├── test_module_a.py
│   └── test_module_b.py
├── docs/               # 文档
├── data/               # 数据文件
├── examples/           # 示例
├── pyproject.toml      # 项目配置(PEP 621)
├── requirements.txt    # 运行时依赖
├── requirements-dev.txt# 开发依赖
├── README.md
├── LICENSE
└── .gitignore
""")                            # 打印标准项目目录结构示例


# ============================================================
# 七、.gitignore 常用内容
# ============================================================
print("=== Python 项目 .gitignore 示例 ===")  # 打印 .gitignore 示例标题
print("""
# 虚拟环境
.venv/
venv/
env/

# Python 编译产物
__pycache__/
*.pyc
*.pyo
*.pyd

# 测试与覆盖率
.pytest_cache/
.coverage
htmlcov/

# IDE
.vscode/
.idea/

# 系统文件
.DS_Store
Thumbs.db

# 日志
*.log

# 数据
data/*.csv
data/*.json
""")                            # 打印 .gitignore 的示例内容


# ============================================================
# 八、最佳实践检查清单
# ============================================================
print("=== 项目工程化检查清单 ===")  # 打印检查清单标题
checklist = [                      # 定义检查清单列表
    "[x] 使用虚拟环境,不污染全局",            # 检查项 1:使用虚拟环境
    "[x] 有 requirements.txt,依赖明确",       # 检查项 2:有依赖文件
    "[x] 有 README.md,说明项目用途和用法",    # 检查项 3:有 README
    "[x] 代码符合 PEP 8,用 black 自动格式化", # 检查项 4:符合 PEP 8
    "[x] 有单元测试,用 pytest 运行",          # 检查项 5:有单元测试
    "[x] 有 .gitignore,不提交无关文件",       # 检查项 6:有 .gitignore
    "[x] 目录结构清晰,源码和测试分开",        # 检查项 7:目录结构清晰
    "[x] 关键函数有文档字符串(docstring)",    # 检查项 8:有文档字符串
    "[x] 提交前跑一遍测试和 lint",            # 检查项 9:提交前测试
]
for item in checklist:            # 遍历每条检查项
    print(f"  {item}")            # 打印检查项


if __name__ == "__main__":  # 当本文件被直接运行时才执行下面的代码
    print("\n[练习] 请尝试:")                              # 打印练习提示标题
    print("1. 为这个学习项目创建一个虚拟环境 .venv")        # 练习建议 1
    print("2. 激活后安装 black 和 pytest")                 # 练习建议 2
    print("3. 用 pip freeze 看看装了哪些包")               # 练习建议 3
    print("4. 用 black 格式化一个你写的 Python 文件")      # 练习建议 4
    print("5. 生成你自己的 requirements.txt")              # 练习建议 5
