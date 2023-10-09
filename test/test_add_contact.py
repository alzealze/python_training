from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

#def test_add_empy_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(Contact(firstname="", lastname="", mobile="", nickname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)