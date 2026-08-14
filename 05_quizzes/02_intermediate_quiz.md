# 进阶篇测试题

## 一、选择题

### 1. 关于 Python 继承,下列说法错误的是?
- A. 一个类可以继承多个父类
- B. 子类会继承父类的所有非私有属性和方法
- C. super() 用于调用父类方法
- D. 抽象类可以直接实例化

### 2. 下列哪个不是魔术方法?
- A. `__init__`
- B. `__str__`
- C. `__call__`
- D. `__test__`

### 3. 关于装饰器,下列说法错误的是?
- A. 装饰器本质是一个函数
- B. @functools.wraps 用于保留原函数元信息
- C. 装饰器只能装饰函数
- D. 装饰器可以带参数

### 4. 上下文管理器的协议方法包括?
- A. `__enter__` 和 `__exit__`
- B. `__open__` 和 `__close__`
- C. `__init__` 和 `__del__`
- D. `__enter__` 和 `__leave__`

### 5. 生成器和迭代器的关系?
- A. 完全相同
- B. 生成器是特殊的迭代器
- C. 迭代器是特殊的生成器
- D. 没有任何关系

### 6. 关于 GIL 描述正确的是?
- A. 多线程下同一时刻只有一个线程执行 Python 字节码
- B. GIL 让 Python 多线程对所有任务都更快
- C. GIL 可以被轻易移除
- D. 只能使用 multiprocessing 才能并行

## 二、代码阅读题

### 1. 输出什么?
```python
class A:
    def hello(self): return "A"

class B(A):
    def hello(self): return "B" + super().hello()

class C(A):
    def hello(self): return "C" + super().hello()

class D(B, C): pass

print(D().hello())
print(D.__mro__)
```

### 2. 下面代码的输出?
```python
def deco(func):
    def wrapper(*args, **kwargs):
        print("before")
        r = func(*args, **kwargs)
        print("after")
        return r
    return wrapper

@deco
def add(a, b):
    return a + b

print(add(2, 3))
print(add.__name__)
```

### 3. 下面代码会输出什么?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
print(list(g))
```

## 三、编程题

### 1. 实现一个支持索引访问的循环队列

### 2. 实现一个带 LRU 淘汰的字典

### 3. 用装饰器实现一个单例类

### 4. 实现一个支持 with 语句的计时器

## 四、参考答案

<details>
<summary>选择题答案</summary>

1. D  2. D  3. C  4. A  5. B  6. A
</details>

<details>
<summary>代码阅读答案</summary>

1. `"BCA"`, `(D, B, C, A, object)`
2. `before \n 5 \n after \n wrapper` (注意 `__name__`)
3. `1`, `2`, `[3]` (生成器被消费后无法重置)
</details>
