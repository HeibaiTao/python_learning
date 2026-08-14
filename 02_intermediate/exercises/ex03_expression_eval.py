"""练习 3:简单的表达式求值器

题目描述:
    实现一个能计算四则运算的函数
    - 支持 + - * / 和括号
    - 输入字符串,如 "1 + 2 * (3 - 4)"
    - 返回浮点数结果

进阶:支持一元负号、空白符、错误提示

提示:
    - 可以用两个栈:数字栈和操作符栈
    - 优先级:* / 高于 + -
    - 遇到 '(' 直接入栈,遇到 ')' 计算到 '(' 为止
"""


def calc(expr: str) -> float:  # 定义 calc 函数,接收表达式字符串,返回浮点数结果
    """计算四则运算表达式"""
    num_stack = []  # 数字栈,存放操作数
    op_stack = []  # 操作符栈,存放运算符和括号
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # 运算符优先级表,数值越大优先级越高

    def apply_op():  # 定义内部函数,从栈中弹出一个运算符和两个操作数进行计算
        b = num_stack.pop()  # 弹出第二个操作数(后入栈的)
        a = num_stack.pop()  # 弹出第一个操作数(先入栈的)
        op = op_stack.pop()  # 弹出运算符
        if op == "+":  # 如果是加法
            num_stack.append(a + b)  # 计算和并压栈
        elif op == "-":  # 如果是减法
            num_stack.append(a - b)  # 计算差并压栈
        elif op == "*":  # 如果是乘法
            num_stack.append(a * b)  # 计算积并压栈
        elif op == "/":  # 如果是除法
            if b == 0:  # 如果除数为 0
                raise ZeroDivisionError("除数不能为 0")  # 抛出除零异常
            num_stack.append(a / b)  # 计算商并压栈

    i = 0  # 字符串索引,从 0 开始
    n = len(expr)  # 表达式总长度
    while i < n:  # 遍历每个字符
        ch = expr[i]  # 取当前字符

        if ch.isspace():  # 如果是空白字符
            i += 1  # 跳过
            continue  # 进入下一轮循环

        if ch.isdigit() or ch == ".":  # 如果是数字或小数点
            # 解析数字(可能多位/小数)
            j = i  # 用 j 标记数字开始位置
            while j < n and (expr[j].isdigit() or expr[j] == "."):  # 连续读取数字和小数点
                j += 1  # j 后移
            num_stack.append(float(expr[i:j]))  # 把截取的数字字符串转成 float 压栈
            i = j  # i 直接跳到数字末尾
            continue  # 进入下一轮循环

        if ch in "+-*/":  # 如果是运算符
            # 处理一元负号
            if ch == "-" and (i == 0 or expr[i-1] in "(+-*/"):  # 如果是开头或左括号/运算符后的负号
                num_stack.append(0.0)  # 在数字栈压入 0,把一元负号转成 0 - x
            # 当栈顶有运算符且不是左括号,且栈顶优先级 >= 当前运算符时,先计算栈顶
            while op_stack and op_stack[-1] != "(" and \
                  precedence.get(op_stack[-1], 0) >= precedence[ch]:
                apply_op()  # 先计算栈顶运算符
            op_stack.append(ch)  # 当前运算符入栈

        elif ch == "(":  # 如果是左括号
            op_stack.append(ch)  # 左括号直接入栈

        elif ch == ")":  # 如果是右括号
            while op_stack and op_stack[-1] != "(":  # 不断计算直到遇到左括号
                apply_op()  # 计算栈顶运算符
            if not op_stack:  # 如果栈空了还没遇到左括号
                raise ValueError("括号不匹配")  # 抛出括号不匹配异常
            op_stack.pop()  # 弹出 "("

        else:  # 其他字符
            raise ValueError(f"非法字符: {ch!r}")  # 抛出非法字符异常

        i += 1  # 索引后移一位

    while op_stack:  # 处理完后若操作符栈还有运算符
        if op_stack[-1] == "(":  # 如果栈顶是左括号
            raise ValueError("括号未闭合")  # 抛出括号未闭合异常
        apply_op()  # 计算剩余运算符

    if len(num_stack) != 1:  # 如果数字栈中不止一个数
        raise ValueError("表达式不合法")  # 抛出表达式不合法异常
    return num_stack[0]  # 返回最终结果


if __name__ == "__main__":  # 判断是否作为主程序运行
    tests = [  # 测试用例列表,每项为(表达式, 期望结果)
        ("1 + 2", 3),  # 简单加法
        ("1 + 2 * 3", 7),  # 乘法优先
        ("(1 + 2) * 3", 9),  # 括号改变优先级
        ("10 - 2 * 3", 4),  # 减法和乘法
        ("((1+2)*(3+4))", 21),  # 嵌套括号
        ("-1 + 2", 1),  # 一元负号
    ]
    for expr, expected in tests:  # 遍历每个测试用例
        got = calc(expr)  # 调用 calc 计算实际结果
        status = "OK" if abs(got - expected) < 1e-6 else "FAIL"  # 用浮点误差判断是否通过
        print(f"  [{status}] {expr!r} = {got}  (期望 {expected})")  # 打印测试结果
