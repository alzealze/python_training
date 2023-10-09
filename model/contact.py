class Contact:
    """для создания контакта на http://localhost/addressbook/"""
    def __init__(self, firstname=None, lastname=None, mobile=None, nickname=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.nickname = nickname
        self.id = id
