"""练习 1:设计一个卡片类体系

题目描述:
    设计一个扑克牌游戏所需的类:
    - Suit(花色):枚举,红桃/方块/梅花/黑桃
    - Card(单张牌):包含花色和点数,支持比较
    - Deck(一副牌):包含 52 张牌,支持洗牌、发牌
    - Hand(手牌):一个玩家手里的牌,支持排序

要求:
    - 使用 enum
    - 用魔术方法实现比较(__lt__, __eq__)
    - 用 random.shuffle 洗牌
"""

import enum  # 导入 enum 模块,用于定义枚举
import random  # 导入 random 模块,用于洗牌
from functools import total_ordering  # 导入 total_ordering 装饰器,自动补全比较方法


class Suit(enum.Enum):  # 定义花色枚举 Suit,继承 enum.Enum
    """花色"""
    HEARTS = "H"    # 红心
    DIAMONDS = "D"   # 方块
    CLUBS = "C"      # 梅花
    SPADES = "S"     # 黑桃


@total_ordering  # 用 total_ordering 装饰,只需定义 __eq__ 和 __lt__ 即可获得全部比较方法
class Card:  # 定义 Card 类,表示单张扑克牌
    """单张扑克牌"""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # 点数列表,索引越大牌越大

    def __init__(self, suit: Suit, rank: str):  # 构造方法,接收花色和点数
        self.suit = suit  # 保存花色到实例属性
        self.rank = rank  # 保存点数到实例属性
        self._value = self.RANKS.index(rank)  # 根据点数在 RANKS 中的索引得到比较值

    def __repr__(self):  # 定义 __repr__,返回牌的字符串表示
        return f"{self.suit.value}{self.rank}"  # 返回形如 H10 的字符串

    def __eq__(self, other):  # 定义 == 比较
        if not isinstance(other, Card):  # 如果对方不是 Card 类型
            return NotImplemented  # 返回 NotImplemented,交给对方处理
        return self._value == other._value  # 比较点数值是否相等

    def __lt__(self, other):  # 定义 < 比较
        if not isinstance(other, Card):  # 如果对方不是 Card 类型
            return NotImplemented  # 返回 NotImplemented
        return self._value < other._value  # 比较点数值大小

    def __hash__(self):  # 定义哈希值,使 Card 可作为字典键或集合元素
        return hash((self.suit, self.rank))  # 用花色和点数组成的元组计算哈希


class Deck:  # 定义 Deck 类,表示一副牌
    """一副牌"""
    def __init__(self):  # 构造方法,生成一副完整的牌
        self._cards = [Card(s, r) for s in Suit for r in Card.RANKS]  # 双重循环生成 52 张牌

    def __len__(self):  # 定义 len() 行为
        return len(self._cards)  # 返回牌的数量

    def __iter__(self):  # 定义迭代行为
        return iter(self._cards)  # 返回牌列表的迭代器

    def shuffle(self):  # 定义洗牌方法
        random.shuffle(self._cards)  # 用 random.shuffle 原地打乱牌的顺序

    def deal(self, n=1):  # 定义发牌方法,默认发 1 张
        if n > len(self._cards):  # 如果要发的数量超过剩余牌数
            raise ValueError("牌不够了")  # 抛出异常
        dealt = self._cards[:n]  # 取前 n 张作为发出的牌
        self._cards = self._cards[n:]  # 剩余的牌保留在牌堆
        return dealt  # 返回发出的牌列表


class Hand:  # 定义 Hand 类,表示玩家手牌
    """手牌"""
    def __init__(self, owner="Player"):  # 构造方法,默认玩家名 Player
        self.owner = owner  # 保存玩家名
        self.cards = []  # 初始化空的手牌列表

    def add(self, card: Card):  # 定义添加手牌方法
        self.cards.append(card)  # 把牌追加到手牌列表

    def sort(self):  # 定义排序方法
        self.cards.sort()  # 利用 Card 的 __lt__ 对手牌排序

    def __repr__(self):  # 定义 __repr__,返回手牌信息
        return f"{self.owner} 的手牌: {self.cards}"  # 返回玩家名和手牌列表


if __name__ == "__main__":  # 判断是否作为主程序运行
    deck = Deck()  # 创建一副新牌
    print(f"新牌共 {len(deck)} 张")  # 打印牌的数量
    deck.shuffle()  # 洗牌
    hand1 = Hand("玩家1")  # 创建玩家 1 的手牌
    hand2 = Hand("玩家2")  # 创建玩家 2 的手牌
    for _ in range(5):  # 循环 5 轮
        hand1.add(deck.deal(1)[0])  # 给玩家 1 发 1 张牌
        hand2.add(deck.deal(1)[0])  # 给玩家 2 发 1 张牌
    hand1.sort()  # 对玩家 1 的手牌排序
    hand2.sort()  # 对玩家 2 的手牌排序
    print(hand1)  # 打印玩家 1 的手牌
    print(hand2)  # 打印玩家 2 的手牌
