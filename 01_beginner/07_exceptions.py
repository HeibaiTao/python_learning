"""07 - 异常处理

学习目标:
    - 掌握 try/except/finally
    - 理解异常的传播
    - 学会自定义异常
"""

# ===== 1. 基本异常处理 =====
print("--- 基本异常处理 ---")  # 打印本节标题
try:                         # try 块:尝试执行可能出错的代码
    result = 10 / 0          # 这里会触发除零错误
except ZeroDivisionError as e:  # 捕获除零异常,把异常对象赋值给 e
    print("除零错误:", e)        # 打印错误信息
else:                        # else 块:try 没有发生异常时执行
    print("没有异常,结果是:", result)  # 打印结果(本例不会执行,因为发生了异常)
finally:                     # finally 块:无论是否发生异常都会执行
    print("无论如何都会执行")   # 打印提示信息


# ===== 2. 多种异常 =====
print("\n--- 多种异常 ---")  # 打印多种异常部分标题
def safe_div(a, b):          # 定义安全除法函数
    try:                     # 尝试执行除法
        return a / b         # 返回 a 除以 b 的结果
    except ZeroDivisionError:  # 捕获除零错误
        return "除数不能为0"    # 返回错误提示字符串
    except TypeError:        # 捕获类型错误(比如除数是字符串)
        return "类型错误"      # 返回错误提示字符串
    except Exception as e:        # 兜底  # 捕获所有其他异常(Exception 是所有异常的基类)
        return f"其他错误: {e}"   # 返回其他错误信息

print(safe_div(10, 2))   # 正常除法,打印 5.0
print(safe_div(10, 0))   # 除零,打印"除数不能为0"
print(safe_div(10, "x")) # 类型错误,打印"类型错误"


# ===== 3. 抛出异常 =====
print("\n--- 抛出异常 ---")  # 打印抛出异常部分标题
def set_age(age):            # 定义设置年龄的函数
    if not isinstance(age, int):  # 如果 age 不是整数类型
        raise TypeError("年龄必须是整数")  # 主动抛出 TypeError 异常
    if age < 0 or age > 150:      # 如果年龄小于 0 或大于 150
        raise ValueError("年龄必须在 0-150 之间")  # 主动抛出 ValueError 异常
    return age                # 校验通过,返回年龄

try:                         # 尝试调用 set_age
    set_age(-1)              # 传入非法年龄 -1,会触发 ValueError
except ValueError as e:      # 捕获 ValueError 异常
    print("校验失败:", e)     # 打印错误信息


# ===== 4. 自定义异常 =====
print("\n--- 自定义异常 ---")  # 打印自定义异常部分标题
class InsufficientFundsError(Exception):  # 自定义异常类,继承自 Exception
    """余额不足异常"""                    # 类的文档字符串
    def __init__(self, balance, amount):  # 构造函数,接收余额和取款金额
        super().__init__(f"余额 {balance} 不足,需要 {amount}")  # 调用父类构造函数,设置错误信息
        self.balance = balance            # 保存余额到实例属性
        self.amount = amount              # 保存取款金额到实例属性

class BankAccount:                        # 定义银行账户类
    def __init__(self, balance=0):        # 构造函数,默认余额为 0
        self.balance = balance            # 初始化账户余额

    def withdraw(self, amount):           # 定义取款方法
        if amount > self.balance:         # 如果取款金额大于余额
            raise InsufficientFundsError(self.balance, amount)  # 抛出自定义异常
        self.balance -= amount            # 从余额中扣除取款金额
        return self.balance               # 返回取款后的余额

account = BankAccount(100)                # 创建账户,初始余额 100
try:                                      # 尝试取款
    account.withdraw(200)                 # 尝试取款 200(余额不足)
except InsufficientFundsError as e:       # 捕获自定义异常
    print(str(e))                         # 打印异常信息


# ===== 5. 异常的传播 =====
print("\n--- 异常传播 ---")  # 打印异常传播部分标题
def level3():               # 定义第 3 层函数
    return 1 / 0            # 这里会触发除零错误

def level2():               # 定义第 2 层函数
    return level3()         # 调用 level3,异常会向上传播

def level1():               # 定义第 1 层函数
    return level2()         # 调用 level2,异常继续向上传播

try:                        # 在最外层尝试捕获异常
    level1()                # 调用 level1,异常会从 level3 传播到这
except ZeroDivisionError as e:  # 捕获除零异常
    print("在顶层捕获:", e)     # 打印捕获到的异常信息
    # traceback.print_exc()   # 调试时可打印完整堆栈  # 取消注释可打印完整的调用堆栈信息


# ===== 6. 断言(assert) =====
print("\n--- assert ---")  # 打印 assert 部分标题
def calculate_average(scores):              # 定义计算平均分的函数
    assert len(scores) > 0, "分数列表不能为空"  # 断言:列表不能为空,否则抛出 AssertionError
    return sum(scores) / len(scores)        # 返回平均分

try:                                        # 尝试调用函数
    print(calculate_average([80, 90, 100])) # 正常调用,打印平均分
    print(calculate_average([]))            # 传入空列表,会触发断言失败
except AssertionError as e:                 # 捕获断言异常
    print("断言失败:", e)                    # 打印断言失败信息


# ===== 7. with 上下文与异常安全 =====
print("\n--- with 上下文 ---")  # 打印 with 上下文部分标题
# with 语句确保文件在异常时也能正确关闭
def read_file(path):            # 定义读取文件的函数
    try:                        # 尝试打开并读取文件
        with open(path, "r", encoding="utf-8") as f:  # 用 with 打开文件,确保自动关闭,encoding 指定编码
            return f.read()     # 读取文件全部内容并返回
    except FileNotFoundError:   # 捕获文件不存在的异常
        return None             # 文件不存在时返回 None

print("结果:", read_file("not_exist.txt"))  # 尝试读取不存在的文件,打印 None


if __name__ == "__main__":  # 当本文件被直接运行时才执行下面的代码
    print("\n[练习] 请尝试:")  # 打印练习提示标题
    print("1. 写一个安全整数输入函数,要求用户必须输入合法数字")  # 练习建议 1
    print("2. 自定义异常 InvalidEmailError,用于邮箱校验")        # 练习建议 2
    print("3. 实现一个带重试机制的函数,失败后最多重试3次")        # 练习建议 3
