"""项目 1:命令行 Todo 工具

功能:
    - 增/删/改/查 待办事项
    - 标记完成、按状态过滤
    - 数据持久化(JSON 文件)
    - 支持优先级和截止日期

用法:
    python todo.py add "买牛奶" -p high
    python todo.py list
    python todo.py done 1
    python todo.py delete 1
"""
import sys                          # 导入系统模块,用于平台判断和退出
import os                           # 导入操作系统模块,用于设置环境变量
# Windows 下设置 UTF-8 输出,避免 emoji 报错
if sys.platform.startswith("win"):  # 如果是 Windows 平台
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")   # 设置默认编码为 UTF-8
    try:                            # 尝试重新配置标准输出编码
        sys.stdout.reconfigure(encoding="utf-8")   # 把标准输出设为 UTF-8
        sys.stderr.reconfigure(encoding="utf-8")   # 把标准错误设为 UTF-8
    except Exception:               # 如果失败(老版本 Python 不支持)
        pass                        # 忽略错误

import argparse                     # 导入命令行参数解析模块
import json                         # 导入 JSON 模块,用于数据持久化
from dataclasses import dataclass, asdict, field   # 从 dataclasses 导入数据类相关工具
from datetime import datetime       # 从 datetime 导入 datetime 类,用于时间戳
from pathlib import Path            # 从 pathlib 导入 Path 类,用于路径操作
from typing import Optional         # 从 typing 导入 Optional 类型提示


DATA_FILE = Path(__file__).parent / "todos.json"   # 待办数据保存文件路径(与本脚本同目录)


@dataclass                          # 数据类装饰器,自动生成构造方法等
class Todo:                         # 待办事项数据类
    id: int                         # 待办 ID
    title: str                      # 待办标题
    priority: str = "medium"     # low/medium/high   # 优先级,默认中等
    done: bool = False              # 是否完成,默认未完成
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))   # 创建时间,自动生成
    due: Optional[str] = None       # 截止日期,可选

    def to_dict(self):              # 转为字典的方法(用于序列化)
        return asdict(self)         # 用 asdict 把数据类实例转成字典

    @classmethod                    # 类方法装饰器
    def from_dict(cls, d):          # 从字典创建实例的方法(用于反序列化)
        return cls(**d)             # 用字典解包构造 Todo 对象


class TodoStore:                    # 待办事项存储类,负责持久化
    def __init__(self, path: Path = DATA_FILE):   # 初始化方法,可指定数据文件路径
        self.path = path            # 保存数据文件路径
        self.items: list[Todo] = [] # 内存中的待办列表
        self._load()                # 从文件加载数据

    def _load(self):                # 从文件加载数据的方法
        if self.path.exists():      # 如果数据文件存在
            try:                    # 尝试读取并解析
                raw = json.loads(self.path.read_text(encoding="utf-8"))   # 读取并解析 JSON
                self.items = [Todo.from_dict(d) for d in raw]   # 把每条字典转成 Todo 对象
            except (json.JSONDecodeError, TypeError):   # 如果 JSON 格式错误或类型不对
                self.items = []     # 重置为空列表

    def _save(self):                # 保存数据到文件的方法
        self.path.write_text(       # 写入文件
            json.dumps([t.to_dict() for t in self.items], ensure_ascii=False, indent=2),   # 把列表序列化为 JSON(保留中文,缩进 2)
            encoding="utf-8"        # 使用 UTF-8 编码
        )

    def _next_id(self) -> int:      # 生成下一个 ID 的方法
        return max((t.id for t in self.items), default=0) + 1   # 取当前最大 ID 加 1,空列表返回 1

    def add(self, title: str, priority: str = "medium", due: str = None) -> Todo:   # 添加待办的方法
        todo = Todo(id=self._next_id(), title=title, priority=priority, due=due)   # 创建新待办对象
        self.items.append(todo)     # 加入列表
        self._save()                # 保存到文件
        return todo                 # 返回新建的待办

    def list(self, only_pending=False, only_done=False) -> list[Todo]:   # 查询待办列表的方法
        items = self.items          # 默认返回全部
        if only_pending: items = [t for t in items if not t.done]   # 只看未完成
        if only_done: items = [t for t in items if t.done]   # 只看已完成
        return items                # 返回过滤后的列表

    def complete(self, todo_id: int) -> bool:   # 标记完成的方法
        for t in self.items:        # 遍历所有待办
            if t.id == todo_id:     # 找到对应 ID
                t.done = True       # 标记为完成
                self._save()        # 保存到文件
                return True         # 返回成功
        return False                # 没找到,返回失败

    def delete(self, todo_id: int) -> bool:   # 删除待办的方法
        before = len(self.items)    # 记录删除前的数量
        self.items = [t for t in self.items if t.id != todo_id]   # 过滤掉要删除的 ID
        if len(self.items) != before:   # 如果数量变了(即删除成功)
            self._save()            # 保存到文件
            return True             # 返回成功
        return False                # 没找到,返回失败


def format_todo(t: Todo) -> str:    # 格式化单个待办为字符串的函数
    status = "✓" if t.done else "○"  # 完成显示对勾,未完成显示圆圈
    pri = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(t.priority, " ")   # 优先级对应表情
    due = f" [截止:{t.due}]" if t.due else ""   # 有截止日期则显示
    return f"  [{status}] #{t.id:<3} {pri} {t.title}{due}"   # 拼接并返回格式化字符串


def main():                          # 主函数
    parser = argparse.ArgumentParser(description="命令行 Todo 工具")   # 创建参数解析器
    sub = parser.add_subparsers(dest="cmd", required=True)   # 添加子命令,必须指定

    # add
    p_add = sub.add_parser("add", help="添加待办")   # 添加 add 子命令
    p_add.add_argument("title")      # 标题参数(必填)
    p_add.add_argument("-p", "--priority", choices=["low", "medium", "high"], default="medium")   # 优先级选项
    p_add.add_argument("-d", "--due", help="截止日期 YYYY-MM-DD")   # 截止日期选项

    # list
    p_list = sub.add_parser("list", help="查看待办")   # 添加 list 子命令
    p_list.add_argument("--pending", action="store_true")   # 只看未完成的开关
    p_list.add_argument("--done", action="store_true")   # 只看已完成的开关

    # done
    p_done = sub.add_parser("done", help="标记完成")   # 添加 done 子命令
    p_done.add_argument("id", type=int)   # 待办 ID 参数

    # delete
    p_del = sub.add_parser("delete", help="删除")   # 添加 delete 子命令
    p_del.add_argument("id", type=int)   # 待办 ID 参数

    args = parser.parse_args()       # 解析命令行参数
    store = TodoStore()              # 创建存储对象(会自动加载数据)

    if args.cmd == "add":            # 如果是 add 命令
        t = store.add(args.title, args.priority, args.due)   # 添加待办
        print(f"已添加 #{t.id}: {t.title}")   # 打印添加结果
    elif args.cmd == "list":         # 如果是 list 命令
        items = store.list(args.pending, args.done)   # 获取待办列表
        if not items:                # 如果没有待办
            print("暂无待办")        # 打印提示
        else:                        # 否则
            for t in items:          # 遍历每个待办
                print(format_todo(t))   # 打印格式化后的待办
    elif args.cmd == "done":         # 如果是 done 命令
        if store.complete(args.id):  # 如果标记成功
            print(f"已完成 #{args.id}")   # 打印成功
        else:                        # 否则
            print(f"未找到 #{args.id}")   # 打印未找到
    elif args.cmd == "delete":       # 如果是 delete 命令
        if store.delete(args.id):    # 如果删除成功
            print(f"已删除 #{args.id}")   # 打印成功
        else:                        # 否则
            print(f"未找到 #{args.id}")   # 打印未找到


if __name__ == "__main__":           # 当脚本直接运行时
    main()                           # 调用主函数
