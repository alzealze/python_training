from model.contact import Contact

def test_all_contacts_on_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test", address="test", email="test", email2="test",
                                   email3="test", mobile="test", homephone="test", workphone="test",
                                   secondaryphone="test"))
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    print("contacts_ui = ", contacts_ui)
    print("contacts_db = ", contacts_db)
    assert contacts_ui == contacts_db
