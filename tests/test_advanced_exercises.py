"""高级篇练习 - 单元测试

测试:
- 迷你 ORM
- 异步爬虫(mock 版)
- 依赖注入容器
"""

import sys
import asyncio
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "03_advanced" / "exercises"))

from ex01_mini_orm import User, IntegerField, StringField
from ex03_di_container import Container, Logger, Database, UserService


# ---- 迷你 ORM 测试 ----
class TestMiniORM:
    def setup_method(self):
        User._storage.clear()

    def test_create_user(self):
        u = User(id=1, name="Tom", age=18)
        assert u.id == 1
        assert u.name == "Tom"
        assert u.age == 18

    def test_save_and_find(self):
        User(id=1, name="Tom", age=18).save()
        User(id=2, name="Jerry", age=20).save()
        u = User.find(1)
        assert u is not None
        assert u.name == "Tom"
        assert len(User.all()) == 2

    def test_delete(self):
        u = User(id=1, name="Tom").save()
        assert len(User.all()) == 1
        u.delete()
        assert len(User.all()) == 0

    def test_type_validation(self):
        with pytest.raises((TypeError, ValueError)):
            User(id="not_an_int", name="Tom")

    def test_string_max_length(self):
        long_name = "a" * 100
        with pytest.raises(ValueError):
            User(id=1, name=long_name)

    def test_default_value(self):
        u = User(id=1, name="Test")
        assert u.age == 0


# ---- DI 容器测试 ----
class TestDIContainer:
    def test_singleton(self):
        c = Container()
        c.register(Logger, singleton=True)
        l1 = c.resolve(Logger)
        l2 = c.resolve(Logger)
        assert l1 is l2

    def test_transient(self):
        c = Container()
        c.register(Logger, singleton=False)
        l1 = c.resolve(Logger)
        l2 = c.resolve(Logger)
        assert l1 is not l2

    def test_dependency_injection(self):
        c = Container()
        c.register(Logger)
        c.register(Database)
        c.register(UserService)
        svc = c.resolve(UserService)
        assert isinstance(svc, UserService)
        assert isinstance(svc.db, Database)
        assert isinstance(svc.logger, Logger)

    def test_parent_child(self):
        parent = Container()
        parent.register(Logger)
        child = Container(parent=parent)
        child.register(UserService)
        child.register(Database)
        svc = child.resolve(UserService)
        assert svc is not None
        assert svc.logger is parent.resolve(Logger)

    def test_unregistered(self):
        c = Container()
        with pytest.raises(KeyError):
            c.resolve(Logger)


# ---- 异步爬虫测试(mock) ----
class TestAsyncCrawler:
    @pytest.mark.asyncio
    async def test_crawler_runs(self):
        from ex02_async_crawler import AsyncCrawler
        urls = [f"https://test.com/{i}" for i in range(3)]
        crawler = AsyncCrawler(urls, max_concurrent=2)
        await crawler.run()
        assert len(crawler.results) == 3
        for url in urls:
            assert url in crawler.results
            assert crawler.results[url]["ok"] is True
