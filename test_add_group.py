# -*- coding: utf-8 -*-
from application import Application
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("dfgdfg", "dfgdfg", "dfgdfgdfg"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("", "", ""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
