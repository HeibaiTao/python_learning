"""练习 2:LRU 缓存

题目描述:
    实现一个 LRU(最近最少使用)缓存
    - 容量固定
    - get(key) 时:命中返回 value,并将 key 标记为最近使用;未命中返回 -1
    - put(key, value) 时:
        * 容量已满则淘汰最久未使用
        * key 已存在则更新值并标记为最近使用

提示:
    - 借助 collections.OrderedDict 实现,它的 move_to_end 方法很方便
    - 关注 get/put 的时间复杂度
"""

from collections import OrderedDict  # 从 collections 导入 OrderedDict,有序字典


class LRUCache:  # 定义 LRUCache 类,实现最近最少使用缓存
    def __init__(self, capacity: int):  # 构造方法,接收容量参数
        if capacity <= 0:  # 如果容量非正
            raise ValueError("capacity 必须为正整数")  # 抛出异常
        self.capacity = capacity  # 保存容量
        self.cache = OrderedDict()  # 创建空的有序字典作为缓存

    def get(self, key):  # 定义 get 方法,根据键取值
        if key not in self.cache:  # 如果键不在缓存中
            return -1  # 未命中返回 -1
        # 移动到末尾表示"最近使用"
        self.cache.move_to_end(key)  # 把该键移到末尾,表示最近使用过
        return self.cache[key]  # 返回对应的值

    def put(self, key, value):  # 定义 put 方法,存入键值对
        if key in self.cache:  # 如果键已存在
            self.cache.move_to_end(key)  # 先移到末尾,标记为最近使用
        self.cache[key] = value  # 存入或更新值(新键会自动加到末尾)
        if len(self.cache) > self.capacity:  # 如果超出容量
            # 弹出最久未使用(第一个)
            self.cache.popitem(last=False)  # 弹出第一个元素(最久未使用)

    def __repr__(self):  # 定义 __repr__,返回缓存的可读表示
        return f"LRUCache({dict(self.cache)})"  # 返回形如 LRUCache({1:1, 2:2}) 的字符串


if __name__ == "__main__":  # 判断是否作为主程序运行
    cache = LRUCache(2)  # 创建容量为 2 的 LRU 缓存
    cache.put(1, 1)  # 存入键 1 值 1
    cache.put(2, 2)  # 存入键 2 值 2
    print(cache)             # {1:1, 2:2}
    print(cache.get(1))      # 1, 1 变成最近使用
    cache.put(3, 3)          # 淘汰 key=2
    print(cache)             # {1:1, 3:3}
    print(cache.get(2))      # -1 (已淘汰)
    cache.put(4, 4)          # 淘汰 key=1
    print(cache)             # {3:3, 4:4}
