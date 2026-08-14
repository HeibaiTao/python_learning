"""通用工具函数"""


def safe_input(prompt: str, caster=str, error_msg="输入无效,请重试"):   # 安全输入函数,持续提示直到合法
    """安全输入:持续提示直到得到合法值"""
    while True:                      # 无限循环,直到输入合法
        try:                         # 尝试转换输入
            return caster(input(prompt))   # 读取输入并用 caster 转换,成功则返回
        except (ValueError, TypeError):   # 如果转换失败
            print(error_msg)         # 打印错误提示,继续循环


def truncate(text: str, max_len: int = 30, suffix: str = "...") -> str:   # 字符串截断函数
    """字符串截断"""
    if len(text) <= max_len:         # 如果长度不超过上限
        return text                  # 直接返回原文
    return text[: max_len - len(suffix)] + suffix   # 截断并加上省略号


def format_duration(seconds: float) -> str:   # 把秒数格式化为友好显示的函数
    """把秒数格式化为友好显示"""
    if seconds < 1:                  # 如果小于 1 秒
        return f"{seconds * 1000:.0f}ms"   # 转成毫秒显示
    if seconds < 60:                 # 如果小于 1 分钟
        return f"{seconds:.2f}s"     # 保留两位小数显示秒
    m, s = divmod(int(seconds), 60)  # 计算分钟和剩余秒数
    return f"{m}m{s}s"               # 返回"分+秒"格式


def confirm(prompt: str, default: bool = False) -> bool:   # 确认提示函数
    """确认提示"""
    suffix = "[Y/n]" if default else "[y/N]"   # 根据默认值显示提示(大写表示默认)
    ans = input(f"{prompt} {suffix}: ").strip().lower()   # 读取用户输入并去空格转小写
    if not ans:                      # 如果用户直接回车(无输入)
        return default               # 返回默认值
    return ans in ("y", "yes")       # 输入 y 或 yes 返回 True,否则 False


if __name__ == "__main__":           # 当脚本直接运行时
    print(truncate("Hello World, this is a long string", 15))   # 演示字符串截断
    print(format_duration(0.123))    # 演示毫秒格式化
    print(format_duration(75.5))     # 演示分秒格式化
