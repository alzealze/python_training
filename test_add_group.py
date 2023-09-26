# -*- coding: utf-8 -*-
from application import Application
from group import Group
import pytest


@pytest.fixture
def app(request):
    """Создаем, разрушаем, возвращаем фикстуру"""
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("dfgdfg", "dfgdfg", "dfgdfgdfg"))
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()
