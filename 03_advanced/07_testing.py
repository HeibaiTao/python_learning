"""07 - 测试与调试

学习目标:
    - 掌握 unittest 和 pytest
    - 学会写各种断言
    - 了解 mock、fixture
    - 掌握基本的调试技巧
"""

import unittest  # 导入 unittest 测试框架
from unittest.mock import Mock, patch, MagicMock  # 导入 Mock 相关工具


# ===== 1. unittest =====
print("--- unittest ---")  # 打印本节标题

def add(a, b):  # 定义加法函数
    return a + b  # 返回两数之和

def divide(a, b):  # 定义除法函数
    if b == 0:  # 如果除数为 0
        raise ValueError("除数不能为0")  # 抛出值错误
    return a / b  # 返回商


class TestMath(unittest.TestCase):  # 定义测试类继承 TestCase
    def setUp(self):  # 每个测试方法前执行的钩子
        """每个测试方法前执行"""  # 方法说明
        print(f"  [setUp] 运行 {self._testMethodName}")  # 打印正在运行的方法名

    def tearDown(self):  # 每个测试方法后执行的钩子
        """每个测试方法后执行"""  # 方法说明
        pass  # 此处不做清理

    def test_add(self):  # 测试 add 函数
        self.assertEqual(add(1, 2), 3)  # 断言 1+2 等于 3
        self.assertNotEqual(add(1, 2), 4)  # 断言 1+2 不等于 4

    def test_divide_ok(self):  # 测试正常除法
        self.assertEqual(divide(10, 2), 5)  # 断言 10/2 等于 5

    def test_divide_by_zero(self):  # 测试除以零抛异常
        with self.assertRaises(ValueError):  # 期望抛出 ValueError
            divide(10, 0)  # 调用除以零

    @unittest.skip("演示跳过")  # 装饰器标记跳过
    def test_skipped(self):  # 此测试不会运行
        self.fail("不会执行")  # 如果运行则失败


# ===== 2. pytest 风格(推荐) =====
print("\n--- pytest 风格 ---")  # 打印本节标题
# pytest 用 assert 即可,无需记那么多方法
# 运行:pytest test_module.py -v
def test_add_pytest():  # pytest 风格的测试函数
    assert add(1, 2) == 3  # 直接用 assert 断言
    assert add(0, 0) == 0  # 测试零值

def test_divide_pytest():  # 测试除法
    assert divide(10, 2) == 5  # 断言结果为 5

import pytest  # 导入 pytest

def test_divide_by_zero_pytest():  # 测试除以零
    with pytest.raises(ValueError, match="除数不能为0"):  # 期望异常并匹配信息
        divide(10, 0)  # 触发异常

@pytest.mark.parametrize("a,b,expected", [  # 参数化测试
    (1, 2, 3),  # 用例 1
    (0, 0, 0),  # 用例 2
    (-1, 1, 0),  # 用例 3
    (10, -5, 5),  # 用例 4
])
def test_add_param(a, b, expected):  # 参数化测试函数
    assert add(a, b) == expected  # 断言加法结果


# ===== 3. pytest fixture =====
print("\n--- fixture ---")  # 打印本节标题
@pytest.fixture  # 声明为 fixture
def sample_data():  # 返回测试数据
    return [1, 2, 3, 4, 5]  # 返回示例列表

def test_sum(sample_data):  # 使用 fixture 作为参数
    assert sum(sample_data) == 15  # 断言求和为 15

def test_max(sample_data):  # 使用同一 fixture
    assert max(sample_data) == 5  # 断言最大值为 5


# ===== 4. Mock 对象 =====
print("\n--- mock ---")  # 打印本节标题
# 场景:测试依赖外部 API 的代码
def fetch_user_email(api_client, user_id):  # 模拟获取用户邮箱的函数
    response = api_client.get(f"/users/{user_id}")  # 调用 API 获取响应
    return response.json()["email"]  # 从响应中取出 email


def test_fetch_user_email():  # 测试获取邮箱函数
    # 创建 mock 客户端
    mock_client = Mock()  # 创建 Mock 对象
    mock_client.get.return_value.json.return_value = {"email": "tom@example.com"}  # 设置返回值链

    email = fetch_user_email(mock_client, 123)  # 用 mock 调用

    assert email == "tom@example.com"  # 断言邮箱正确
    mock_client.get.assert_called_once_with("/users/123")  # 断言 get 被调用一次且参数正确
    print("  Mock 测试通过")  # 打印通过信息


test_fetch_user_email()  # 直接运行测试


# ===== 5. patch 装饰器 =====
print("\n--- patch ---")  # 打印本节标题
import os  # 导入 os 模块
def get_env(name):  # 获取环境变量的函数
    return os.environ.get(name)  # 返回指定环境变量

def test_get_env():  # 测试 get_env
    with patch.dict(os.environ, {"MY_VAR": "hello"}):  # 临时给环境变量打补丁
        assert get_env("MY_VAR") == "hello"  # 断言能读到补丁的值
    print("  patch.dict 测试通过")  # 打印通过信息

test_get_env()  # 直接运行测试


# ===== 6. 调试技巧 =====
print("\n--- 调试技巧 ---")  # 打印本节标题
# 1) print 调试:最简单
# 2) assert 断言
# 3) pdb 交互式调试
#    import pdb; pdb.set_trace()
# 4) breakpoint() (Python 3.7+)
# 5) IDE 断点(推荐)
# 6) logging 替代 print

import logging  # 导入日志模块
logging.basicConfig(level=logging.DEBUG)  # 配置日志级别为 DEBUG
logger = logging.getLogger(__name__)  # 创建当前模块的 logger

def buggy_function(x):  # 演示日志的函数
    logger.debug(f"输入: {x}")  # 记录调试日志
    result = x * 2  # 计算结果
    logger.info(f"计算结果: {result}")  # 记录信息日志
    return result  # 返回结果

buggy_function(21)  # 调用函数


# ===== 7. 覆盖率 =====
print("\n--- 覆盖率 ---")  # 打印本节标题
# pip install coverage
# coverage run -m pytest
# coverage report -m
# coverage html


# ===== 8. 异常测试 =====
print("\n--- 异常测试 ---")  # 打印本节标题
def test_exception_message():  # 测试异常信息
    with pytest.raises(ValueError) as exc_info:  # 捕获异常信息
        divide(1, 0)  # 触发异常
    assert "除数" in str(exc_info.value)  # 断言异常信息包含关键字
    print("  异常信息测试通过")  # 打印通过信息

test_exception_message()  # 直接运行测试


if __name__ == "__main__":  # 直接运行本文件时执行
    # 运行 unittest
    unittest.main(argv=[""], exit=False, verbosity=2)  # 运行 unittest 测试,不退出
    print("\n[练习] 请尝试:")  # 打印练习提示
    print("1. 把之前的练习(计算器、LRU 等)加上单元测试")  # 练习题 1
    print("2. 用 pytest + parametrize 全面测试一个排序函数")  # 练习题 2
    print("3. 用 mock 测试一段依赖 requests 的代码(无需网络)")  # 练习题 3
