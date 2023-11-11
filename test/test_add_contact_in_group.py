from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group("groupname_test", "header_test", "footer_test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if len(orm.get_contact_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="firstname_test", lastname="lastname_test", address="address_test",
                                   mobile="mobile_test"))
    contacts = orm.get_contact_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in orm.get_contact_in_group(group)
