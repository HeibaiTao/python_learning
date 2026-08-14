"""进阶篇练习 - 单元测试

测试:
- 扑克牌类
- LRU 缓存
- 表达式求值器
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "02_intermediate" / "exercises"))

from ex02_lru_cache import LRUCache
from ex03_expression_eval import calc


# ---- LRU Cache 测试 ----
class TestLRUCache:
    def test_basic(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        assert c.get(1) == 1
        c.put(3, 3)
        assert c.get(2) == -1
        c.put(4, 4)
        assert c.get(1) == -1
        assert c.get(3) == 3
        assert c.get(4) == 4

    def test_update(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(1, 10)
        assert c.get(1) == 10
        assert len(c.cache) == 1

    def test_zero_capacity(self):
        with pytest.raises(ValueError):
            LRUCache(0)

    def test_large(self):
        c = LRUCache(1000)
        for i in range(2000):
            c.put(i, i * 2)
        assert len(c.cache) == 1000
        assert c.get(1999) == 3998
        assert c.get(0) == -1

    @pytest.mark.parametrize("operations,results", [
        ([("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2)],
         [None, None, 1, None, -1]),
        ([("put", 1, 1), ("get", 1), ("get", 2)],
         [None, 1, -1]),
    ])
    def test_param(self, operations, results):
        c = LRUCache(2)
        for op, expected in zip(operations, results):
            if op[0] == "put":
                c.put(op[1], op[2])
            else:
                assert c.get(op[1]) == expected


# ---- 表达式求值测试 ----
class TestExpressionEval:
    def test_simple(self):
        assert calc("1 + 2") == 3

    def test_multiplication_priority(self):
        assert calc("1 + 2 * 3") == 7

    def test_parentheses(self):
        assert calc("(1 + 2) * 3") == 9

    def test_unary_minus(self):
        assert calc("-1 + 2") == 1

    def test_division(self):
        assert calc("10 / 2") == 5

    def test_subtraction(self):
        assert calc("10 - 2 * 3") == 4

    def test_nested_parentheses(self):
        assert calc("((1+2)*(3+4))") == 21

    def test_spaces(self):
        assert calc("  1 +   2  *  3  ") == 7

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calc("1 / 0")

    def test_invalid_char(self):
        with pytest.raises(ValueError):
            calc("1 + x")

    def test_unclosed_paren(self):
        with pytest.raises(ValueError):
            calc("(1 + 2")

    @pytest.mark.parametrize("expr,expected", [
        ("2 + 3 * 4", 14),
        ("(2 + 3) * 4", 20),
        ("100 / 5 / 2", 10),
        ("1 + 2 + 3 + 4 + 5", 15),
    ])
    def test_param(self, expr, expected):
        if isinstance(expected, type(Exception)):
            with pytest.raises(expected):
                calc(expr)
        else:
            assert calc(expr) == expected
