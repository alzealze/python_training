from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="firstname_test", lastname="lastname_test", address="address_test", mobile="mobile_test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group("groupname_test", "header_test", "footer_test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    if contact in orm.get_contact_not_in_group(group):
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    assert contact in orm.get_contact_not_in_group(group)
