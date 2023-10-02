class Group:
    """для создания группы на http://localhost/addressbook/"""
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer
