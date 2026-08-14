"""项目 5:简易聊天机器人

功能:
    - 基于关键词匹配的规则式聊天机器人
    - 支持多轮对话(上下文记忆)
    - 内置打招呼、问答、计算、时间查询等能力
    - 可扩展的技能系统(插件式)

用法:
    python chatbot.py
    然后就可以和它聊天了。输入 quit 退出。
"""

import re                            # 导入正则表达式模块,用于匹配用户输入
import random                        # 导入随机数模块,用于随机选择回复
import datetime                      # 导入日期时间模块,用于查询时间和日期
from dataclasses import dataclass    # 从 dataclasses 导入 dataclass 装饰器,简化数据类定义
from typing import Callable, Optional   # 从 typing 导入类型提示工具


@dataclass                           # 数据类装饰器,自动生成 __init__ 等方法
class Skill:                         # 定义一个聊天技能类
    """一个聊天技能"""
    name: str                        # 技能名称
    pattern: str           # 正则匹配用户输入   # 用于匹配用户输入的正则表达式
    handler: Callable[[dict], str]   # 处理函数,接收匹配对象,返回回复字符串


class ChatBot:                       # 聊天机器人主类
    """简易聊天机器人"""

    def __init__(self, name="小助手"):   # 初始化方法,可自定义机器人名字
        self.name = name             # 保存机器人名字
        self.skills: list[Skill] = []   # 技能列表,初始为空
        self.context = {             # 上下文字典,用于多轮对话记忆
            "user_name": None,       # 用户姓名,初始未知
            "last_topic": None,      # 上一轮对话的话题
            "message_count": 0,      # 已收到的消息总数
        }
        self._register_default_skills()   # 注册默认技能

    # ===== 技能注册 =====
    def add_skill(self, skill: Skill):   # 添加自定义技能的方法
        self.skills.append(skill)    # 把技能加入技能列表

    def _register_default_skills(self):   # 注册默认技能的方法
        """注册默认技能(按优先级顺序)"""
        self.skills = [              # 按优先级顺序设置技能列表
            Skill("问候", r"^(你好|嗨|hi|hello|嗨喽|你好啊|早上好|晚上好)", self._greet),   # 问候技能
            Skill("名字", r"(你叫什么|你是谁|你的名字)", self._introduce),   # 询问机器人名字
            Skill("问用户姓名", r"(我叫|我的名字是|我是)(.+)", self._remember_name),   # 记住用户姓名
            Skill("问时间", r"(几点了|什么时间|现在时间|时间)", self._tell_time),   # 查询时间
            Skill("问日期", r"(今天几号|什么日期|星期几|今天周几)", self._tell_date),   # 查询日期
            Skill("计算", r"计算(.+)", self._calculate),   # 计算数学表达式
            Skill("讲笑话", r"(讲个笑话|笑话|逗我)", self._tell_joke),   # 讲笑话
            Skill("帮助", r"(帮助|help|你能做什么|功能)", self._help),   # 帮助说明
            Skill("天气", r"(天气|气温)", self._weather),   # 天气查询
            Skill("情绪_开心", r"(开心|高兴|棒|太好了|好耶)", self._happy),   # 用户开心时的回应
            Skill("情绪_难过", r"(难过|伤心|不开心|郁闷)", self._sad),   # 用户难过时的回应
            Skill("感谢", r"(谢谢|感谢|thx|thanks|xiexie)", self._thanks),   # 感谢回应
            Skill("再见", r"(再见|拜拜|quit|exit|88|晚安)", self._goodbye),   # 再见回应
        ]

    # ===== 技能实现 =====
    def _greet(self, match) -> str:  # 问候技能的处理函数
        greetings = [                # 候选问候语列表
            f"你好呀!我是{self.name} 😊",
            "嗨!今天过得怎么样?",
            "你好!有什么我可以帮你的吗?",
        ]
        if self.context["user_name"]:   # 如果知道用户名字
            greetings = [g.replace("你好", f"{self.context['user_name']},你好") for g in greetings]   # 在问候中加入名字
        return random.choice(greetings)   # 随机返回一条问候语

    def _introduce(self, match) -> str:   # 自我介绍技能的处理函数
        return (f"我叫{self.name},是一个简单的聊天机器人。\n"   # 返回自我介绍文本
                f"我会聊天、计算、查时间、讲笑话等。\n"
                f"输入'帮助'看看我能做什么~")

    def _remember_name(self, match) -> str:   # 记住用户名字的处理函数
        name = match.group(2).strip(" 。！!")   # 提取用户名字并去除首尾标点空格
        self.context["user_name"] = name   # 把名字存入上下文
        return f"好的,{name}!很高兴认识你 😄"   # 返回确认回复

    def _tell_time(self, match) -> str:   # 查询时间的处理函数
        now = datetime.datetime.now() # 获取当前时间
        return f"现在是 {now.strftime('%H:%M:%S')}"   # 返回格式化的时间字符串

    def _tell_date(self, match) -> str:   # 查询日期的处理函数
        now = datetime.datetime.now() # 获取当前日期时间
        weekdays = ["一", "二", "三", "四", "五", "六", "日"]   # 星期中文映射
        return (f"今天是 {now.strftime('%Y年%m月%d日')} "   # 返回格式化日期和星期
                f"星期{weekdays[now.weekday()]}")

    def _calculate(self, match) -> str:   # 计算技能的处理函数
        expr = match.group(1).strip() # 提取要计算的表达式
        try:                          # 尝试计算
            # 安全限制:只允许数字和运算符
            if not re.match(r"^[\d+\-*/().\s]+$", expr):   # 如果包含非法字符
                return "抱歉,我只能计算简单的数学表达式哦"   # 返回提示
            result = eval(expr, {"__builtins__": {}}, {})   # 安全地计算表达式(禁用内置函数)
            return f"{expr} = {result}"   # 返回计算结果
        except ZeroDivisionError:     # 如果除以 0
            return "除数不能为 0 哦~"   # 返回提示
        except Exception as e:        # 如果其他异常
            return f"计算失败了: {e}"   # 返回错误信息

    def _tell_joke(self, match) -> str:   # 讲笑话的处理函数
        jokes = [                     # 笑话列表
            "为什么程序员喜欢黑色?因为彩色会有 bug。",
            "一个 SQL 语句走进酒吧,看到两张表,问:'我能 join 你们吗?'",
            "为什么程序员分不清万圣节和圣诞节?因为 Oct 31 == Dec 25。",
            "我跟我的代码说:'你有 bug',它回答:'那叫特性'。",
            "有 10 种人:懂二进制的和不懂的。",
        ]
        return random.choice(jokes)   # 随机返回一个笑话

    def _help(self, match) -> str:    # 帮助技能的处理函数
        return ("我能做这些事:\n"      # 返回帮助说明
                "  💬 日常聊天 - 打招呼、问名字、聊情绪\n"
                "  ⏰ 查时间 - 问'几点了'、'今天几号'\n"
                "  🧮 算算术 - 说'计算 1+2*3'\n"
                "  😄 讲笑话 - 说'讲个笑话'\n"
                "  🌤 聊天气 - 说'天气怎么样'\n"
                "输入 'quit' 或 '再见' 退出")

    def _weather(self, match) -> str: # 天气技能的处理函数
        return "抱歉,我现在还连不上网,查不了真实天气 😅\n但我猜今天是个好日子!"   # 返回固定回复

    def _happy(self, match) -> str:   # 用户开心时的处理函数
        responses = ["太好了!😄", "开心就好~", "我也很开心!", "真棒!"]   # 候选回复
        return random.choice(responses)   # 随机返回一条

    def _sad(self, match) -> str:     # 用户难过时的处理函数
        responses = [                 # 候选安慰回复
            "怎么了?要不要说说看?",
            "别难过,抱抱~ 🤗",
            "心情不好的话,我给你讲个笑话吧!",
            "一切都会好起来的~",
        ]
        return random.choice(responses)   # 随机返回一条

    def _thanks(self, match) -> str:  # 感谢技能的处理函数
        responses = ["不客气~", "能帮到你就好 😊", "小事一桩!", "随时找我~"]   # 候选回复
        return random.choice(responses)   # 随机返回一条

    def _goodbye(self, match) -> str: # 再见技能的处理函数
        name = self.context.get("user_name") or "朋友"   # 获取用户名字,没有则用"朋友"
        return f"再见,{name}!👋 期待下次再聊~"   # 返回告别语

    # ===== 响应生成 =====
    def respond(self, message: str) -> str:   # 生成回复的方法
        self.context["message_count"] += 1   # 消息计数加 1
        message = message.strip()      # 去除输入首尾空格
        if not message:                # 如果输入为空
            return "你说什么?我没听清~"   # 返回提示

        for skill in self.skills:      # 按优先级遍历所有技能
            m = re.search(skill.pattern, message, re.IGNORECASE)   # 用正则匹配用户输入(忽略大小写)
            if m:                      # 如果匹配成功
                self.context["last_topic"] = skill.name   # 记录当前话题
                return skill.handler(m)   # 调用对应处理函数并返回回复

        # 兜底回复
        fallbacks = [                  # 没匹配到任何技能时的兜底回复
            "嗯...这个问题我暂时还不会回答呢",
            "有意思,能再说详细点吗?",
            "我还在学习中,这个我不太懂~",
            "这个问题有点难到我了 😅",
            "要不我们换个话题?",
        ]
        return random.choice(fallbacks)   # 随机返回一条兜底回复

    # ===== 运行 =====
    def run(self):                    # 启动交互模式的方法
        """启动交互模式"""
        print(f"[{self.name}] 你好!我是{self.name},输入 quit 退出。")   # 打印欢迎信息
        print(f"[{self.name}] 试试说'你好'、'讲个笑话'、'计算 1+2*3' 看看~")   # 打印使用提示
        while True:                   # 对话主循环
            try:                      # 尝试读取用户输入
                user_input = input("你: ").strip()   # 读取并去空格
            except (EOFError, KeyboardInterrupt):   # 如果遇到结束符或 Ctrl+C
                print(f"\n[{self.name}] 再见!👋")   # 打印告别
                break                 # 退出循环

            if not user_input:        # 如果输入为空
                continue              # 跳过本轮,继续下一次输入

            response = self.respond(user_input)   # 生成回复
            print(f"[{self.name}] {response}")   # 打印回复

            if self.context.get("last_topic") == "再见":   # 如果上一轮话题是再见
                break                 # 退出对话循环


if __name__ == "__main__":           # 当脚本直接运行时
    bot = ChatBot()                  # 创建聊天机器人实例
    bot.run()                        # 启动机器人交互
