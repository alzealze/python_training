# -*- coding: utf-8 -*-
from model.group import Group


# data_groups - означет, что будем загружать тестовые данные из модуля groups в пакете data
def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
