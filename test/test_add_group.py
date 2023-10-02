# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("Б40", "python", "python_comment"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
