# 入门篇测试题

## 一、选择题

### 1. 下列哪个不是 Python 的基本数据类型?
- A. int
- B. float
- C. char
- D. bool

### 2. 下面代码的输出是?
```python
print(7 // 2, 7 % 2, 7 / 2)
```
- A. 3 1 3.5
- B. 3 1 3
- C. 3.5 1 3.5
- D. 3 2 3.5

### 3. 下列哪个是不可变类型?
- A. list
- B. dict
- C. set
- D. tuple

### 4. 下面哪个写法是错误的?
- A. `for i in range(10):`
- B. `for i in [1,2,3]:`
- C. `for i in 10:`
- D. `for k, v in {"a":1}.items():`

### 5. 下列哪个函数用于读取用户输入?
- A. input()
- B. raw_input()
- C. read()
- D. get()

### 6. 关于 Python 函数,下列说法错误的是?
- A. 可以有多个 return
- B. 默认参数必须放在位置参数之前
- C. 支持 *args 和 **kwargs
- D. 函数也是对象

## 二、代码阅读题

### 1. 输出是什么?
```python
def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))
print(f(2))
print(f(3))
```

### 2. 输出是什么?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
c = a.copy()
c.append(5)
print(a, c)
```

### 3. 输出是什么?
```python
for i in range(3):
    pass
else:
    print("done")
```

## 三、编程题

### 1. 编写函数 is_prime(n) 判断素数

### 2. 编写函数 reverse_words(s) 反转字符串中单词顺序
- 输入:"hello world python"
- 输出:"python world hello"

### 3. 编写函数 merge_dicts(*dicts) 合并多个字典,后面的覆盖前面的
- merge_dicts({"a":1}, {"a":2, "b":3}) -> {"a":2, "b":3}

### 4. 写一个函数统计文本中各单词频率,返回 Counter
- 忽略大小写和标点

## 四、参考答案

(完成练习后查看)

<details>
<summary>选择题答案</summary>

1. C  2. A  3. D  4. C  5. A  6. B
</details>

<details>
<summary>代码阅读答案</summary>

1. `[1]`, `[1, 2]`, `[1, 2, 3]` (默认参数只初始化一次)
2. `[1, 2, 3, 4]`, `[1, 2, 3, 4] [1, 2, 3, 4, 5]`
3. `done` (循环正常结束时执行 else)
</details>
