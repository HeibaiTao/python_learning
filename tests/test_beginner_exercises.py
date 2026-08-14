"""入门篇练习 - 单元测试

测试:
- 闰年判断
- 回文判断
- 斐波那契数列
- 密码强度检查
- 文件统计工具(需临时文件)
"""

import sys
import tempfile
from pathlib import Path

import pytest

# 加入项目根路径以便导入模块
sys.path.insert(0, str(Path(__file__).parent.parent / "01_beginner" / "exercises"))

from ex02_fibonacci_palindrome import fibonacci, is_palindrome
from ex01_swap_calculator import is_leap_year
from ex03_guess_password import check_password_strength


# ---- 闰年测试 ----
class TestLeapYear:
    def test_normal_leap(self):
        assert is_leap_year(2024) is True

    def test_century_not_leap(self):
        assert is_leap_year(1900) is False

    def test_century_leap(self):
        assert is_leap_year(2000) is True

    def test_common_year(self):
        assert is_leap_year(2023) is False

    @pytest.mark.parametrize("year,expected", [
        (2000, True),
        (2004, True),
        (2001, False),
        (1900, False),
        (0, True),
    ])
    def test_param(self, year, expected):
        assert is_leap_year(year) == expected


# ---- 斐波那契测试 ----
class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == []

    def test_one(self):
        assert fibonacci(1) == [0]

    def test_two(self):
        assert fibonacci(2) == [0, 1]

    def test_ten(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_negative(self):
        assert fibonacci(-5) == []


# ---- 回文测试 ----
class TestPalindrome:
    def test_simple(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello world") is False

    def test_empty(self):
        assert is_palindrome("") is True

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_with_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    @pytest.mark.parametrize("s,expected", [
        ("racecar", True),
        ("hello", False),
        ("12321", True),
        ("No lemon, no melon", True),
    ])
    def test_param(self, s, expected):
        assert is_palindrome(s) == expected


# ---- 密码强度测试 ----
class TestPasswordStrength:
    def test_weak_short(self):
        assert check_password_strength("abc") < 2

    def test_medium(self):
        score = check_password_strength("Password1")
        assert score >= 3

    def test_strong(self):
        score = check_password_strength("P@ssw0rd123!")
        assert score >= 4

    def test_empty(self):
        assert check_password_strength("") == 0

    def test_only_digits(self):
        assert check_password_strength("12345678") < 4

    @pytest.mark.parametrize("pwd,min_score", [
        ("a", 1),
        ("abcdefgh", 2),
        ("ABCDefgh", 3),
        ("ABCD1234", 3),
        ("Abcdefg1!", 4),
    ])
    def test_param(self, pwd, min_score):
        assert check_password_strength(pwd) >= min_score


# ---- 文件统计工具测试 ----
class TestFileStats:
    @pytest.fixture
    def sample_file(self):
        content = "Hello world\nPython is fun\nHello Python\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write(content)
            path = Path(f.name)
        yield path
        path.unlink()

    def test_analyze(self, sample_file):
        sys.path.insert(0, str(Path(__file__).parent.parent / "01_beginner" / "exercises"))
        from ex04_file_stats import analyze_file
        stats = analyze_file(sample_file)
        assert stats["line_count"] == 3
        assert stats["word_count"] == 7
