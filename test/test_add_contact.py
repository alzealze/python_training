from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))


def test_add_empy_contact(app):
    app.contact.create(Contact(firstname="", lastname="", mobile="", nickname=""))
