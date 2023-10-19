from sys import maxsize


class Contact:
    """для создания контакта на http://localhost/addressbook/"""
    def __init__(self, firstname=None, lastname=None, mobile=None, nickname=None, id=None, homephone=None,
                 workphone=None, secondaryphone=None, all_phones_from_home_page=None, address=None,
                 all_emails_from_home_page=None, email=None, email2=None, email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.nickname = nickname
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        return "%s:%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.mobile, self.nickname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize
