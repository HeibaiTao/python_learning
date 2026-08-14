# 高级篇测试题

## 一、选择题

### 1. 关于元类,下列说法正确的是?
- A. 所有类的元类都是 `type`
- B. 元类用于创建类对象
- C. `metaclass` 关键字定义元类
- D. 以上都对

### 2. 描述符协议包括?
- A. `__get__`, `__set__`, `__delete__`
- B. `__getattr__`, `__setattr__`, `__delattr__`
- C. `__getattribute__`, `__set__`, `__delete__`
- D. `__get__`, `__set__`

### 3. asyncio 中用于并发运行多个任务的是?
- A. asyncio.run()
- B. asyncio.gather()
- C. asyncio.create_task()
- D. asyncio.wait()

### 4. 关于 async/await 描述错误的是?
- A. async def 定义协程
- B. await 只能在 async 函数中使用
- C. 协程本质是线程
- D. asyncio.run() 是入口函数

### 5. Protocol 的作用是?
- A. 数据校验
- B. 结构化子类型
- C. 多继承
- D. 性能优化

### 6. 下列哪个不是设计模式?
- A. Singleton
- B. Factory
- C. Observer
- D. Pythonic

## 二、代码阅读题

### 1. 下面代码的输出?
```python
class Meta(type):
    def __new__(mcs, name, bases, ns):
        ns["added"] = "from meta"
        return super().__new__(mcs, name, bases, ns)

class A(metaclass=Meta):
    pass

print(A.added)
```

### 2. 下面代码的输出?
```python
import asyncio

async def task(i, delay):
    await asyncio.sleep(delay)
    return i * 2

async def main():
    tasks = [task(i, 0.1 - i*0.02) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

### 3. 下面描述符的输出?
```python
class Desc:
    def __get__(self, obj, objtype=None):
        return "got"
    def __set__(self, obj, value):
        print(f"set {value}")

class A:
    x = Desc()

a = A()
a.x = 10
print(a.x)
print(A.x)
```

## 三、设计题

### 1. 设计一个线程安全的计数器类
- 支持 increment / decrement / value
- 用 threading.Lock 保证线程安全
- 用魔法方法使其支持 `len()` 和 `bool()`

### 2. 实现一个支持事件回调的 EventEmitter
- on(event, callback): 注册
- emit(event, *args): 触发
- off(event, callback): 注销
- 异步支持(可选)

### 3. 设计一个插件系统
- 插件基类定义接口
- 装饰器自动注册
- 主程序动态加载和调用

## 四、参考答案

<details>
<summary>选择题答案</summary>

1. D  2. A  3. B  4. C  5. B  6. D
</details>

<details>
<summary>代码阅读答案</summary>

1. `from meta`
2. `[0, 2, 4, 6, 8]`(并发执行)
3. `set 10`, `got`, `got`(描述符的 get 在类/实例上行为)
</details>

## 五、综合项目题

请实现一个**简易的 KV 数据库**,支持:
- put(key, value) / get(key) / delete(key)
- 持久化到 JSON 文件
- TTL(过期时间)
- 线程安全
- 提供命令行接口(put/get/keys/expire/flush)

完成后请补充测试用例(pytest)。
