from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
    app.session.logout()
