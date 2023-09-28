# -*- coding: utf-8 -*-
from model.group import Group, Contact


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("Б40", "python", "python_test"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
    app.session.logout()
