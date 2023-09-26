class Group:
    """для создания группы на http://localhost/addressbook/"""
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class Contact:
    """для создания контакта на http://localhost/addressbook/"""
    def __init__(self, firstname, lastname, mobile, nickname):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.nickname = nickname
