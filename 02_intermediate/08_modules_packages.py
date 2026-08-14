"""08 - 模块与包

学习目标:
    - 理解模块与包的组织
    - 掌握 import 的多种方式
    - 学会编写 __init__.py
    - 了解 if __name__ == "__main__"
"""

# ===== 1. 导入方式 =====
print("--- 导入方式 ---")  # 打印分隔标题,演示各种导入方式

# import module
import math  # 导入整个 math 模块
print("math.pi =", math.pi)  # 通过模块名访问常量 pi

# from module import name
from math import sqrt, ceil  # 从 math 导入 sqrt 和 ceil 函数
print("sqrt(16) =", sqrt(16))  # 直接调用 sqrt,无需模块名前缀

# 别名
import datetime as dt  # 导入 datetime 模块并起别名 dt
print("现在:", dt.datetime.now().year)  # 用别名访问当前年份

# 导入所有(不推荐)
# from math import *  # 不推荐,会污染命名空间


# ===== 2. 导入路径 =====
print("\n--- 导入路径 ---")  # 打印分隔标题,演示导入搜索路径
import sys  # 导入 sys 模块
print("路径数:", len(sys.path))  # 打印搜索路径的数量
print("前3个:", sys.path[:3])  # 打印前 3 个搜索路径


# ===== 3. 包结构示例 =====
# 项目根/
# ├── mypackage/
# │   ├── __init__.py
# │   ├── module_a.py
# │   └── subpackage/
# │       ├── __init__.py
# │       └── module_b.py
# └── main.py

# 在 main.py 中:
#   from mypackage import module_a  # 导入 mypackage 下的 module_a
#   from mypackage.subpackage import module_b  # 导入子包中的 module_b
#   import mypackage.module_a as ma  # 用别名导入


# ===== 4. __init__.py 的作用 =====
print("\n--- __init__.py ---")  # 打印分隔标题,说明 __init__.py 作用
# mypackage/__init__.py 内容示例:
"""
# 包初始化代码
print("mypackage 已加载")  # 包被导入时执行

# 可以选择性地暴露接口
from .module_a import ClassA  # 从子模块导入 ClassA
from .module_b import function_b  # 从子模块导入 function_b

__all__ = ["ClassA", "function_b"]  # 定义 from package import * 时暴露的名称
__version__ = "1.0.0"  # 定义包版本号
"""


# ===== 5. 相对导入 vs 绝对导入 =====
# 在包内部:
#   绝对导入(推荐):from mypackage.utils import helper  # 用完整路径导入
#   相对导入:        from .utils import helper  # 当前包内的 utils
#                   from ..sibling import something  # 上一级包的 sibling


# ===== 6. 重新加载模块 =====
print("\n--- importlib ---")  # 打印分隔标题,演示 importlib
import importlib  # 导入 importlib 模块,用于动态导入和重载
# importlib.reload(module)   # 开发时热更新


# ===== 7. 自定义模块查找 =====
print("\n--- 自定义查找器(了解即可) ---")  # 打印分隔标题,介绍自定义查找器
# 通过 sys.path_hooks 注册自定义 finder
# 详见官方文档 importlib


# ===== 8. 循环导入问题 =====
print("\n--- 避免循环导入 ---")  # 打印分隔标题,介绍循环导入
# 错误: a.py 导入 b, b.py 又导入 a
# 解决:
#   1. 重新设计模块结构,提取公共部分到第三个模块
#   2. 将导入语句移到函数内部(延迟导入)
#   3. 使用 TYPE_CHECKING 进行类型提示导入


# ===== 9. 演示:一个完整的小包 =====
print("\n--- 本项目的 utils 包 ---")  # 打印分隔标题,演示项目中的 utils 包
# 让我们看看 utils 包的结构
import pathlib  # 导入 pathlib 模块
utils_path = pathlib.Path(__file__).parent.parent / "utils"  # 计算上一级目录下的 utils 路径
print(f"utils 路径: {utils_path}")  # 打印 utils 路径
if utils_path.exists():  # 如果路径存在
    for p in sorted(utils_path.iterdir()):  # 排序后遍历目录中的内容
        print(f"  {p.name}")  # 打印每个文件/目录名


if __name__ == "__main__":  # 判断是否作为主程序运行
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 创建一个 mathutils 包,包含加减乘除模块")  # 练习题 1
    print("2. 用 __init__.py 控制包对外暴露的接口")  # 练习题 2
    print("3. 解决一个实际的循环导入问题")  # 练习题 3
