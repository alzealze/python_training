import random
# from random import randrange
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    group.id = Group(name="New group")
    group.name = "New group"
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
#    old_groups[group.id] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

"""
def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
"""


# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_name", header="header_test"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="test_name", header="New header")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
