from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("Aleksandr_test", "Zemskov_test", "9998887766_test", "alze_test"))
    app.session.logout()
