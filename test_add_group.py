# -*- coding: utf-8 -*-
from application import Application
from group import Group, Contact
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


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
    app.logout()
