# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("Б40", "python", "python_comment"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
