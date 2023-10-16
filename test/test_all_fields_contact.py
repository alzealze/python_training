from random import randrange
from test.test_phones import merge_phones_like_on_home_page


def test_all_fields_on_home_page(app):
    random_contact = randrange(len(app.contact.get_contact_list()))
    all_info_contact_from_home_page = app.contact.get_contact_list()[random_contact]
    all_info_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_contact)
    assert all_info_contact_from_home_page.firstname == all_info_contact_from_edit_page.firstname
    assert all_info_contact_from_home_page.lastname == all_info_contact_from_edit_page.lastname
    assert all_info_contact_from_home_page.all_addresses_from_home_page == all_info_contact_from_edit_page.address
    assert all_info_contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(all_info_contact_from_edit_page)
    assert all_info_contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(all_info_contact_from_edit_page)
    print("AAAAAAAAAAA", all_info_contact_from_home_page.firstname)
    print("BBBBBBBBBBB", all_info_contact_from_edit_page.firstname)


def merge_emails_like_on_home_page(contact):
    # из всех емейлов убираем емейлы==None,затем убираем пустые строки и остатки склеиваем
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))
