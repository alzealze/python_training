# -*- coding: utf-8 -*-
from group import Contact
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from application import ApplicationCont


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.appcont = ApplicationCont()
        return

    def test_add_contact(self):
        self.appcont.login(username="admin", password="secret")
        self.appcont.create_contact(Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
        self.appcont.logout()


    def tearDown(self):
        self.appcont.destroycont()


if __name__ == "__main__":
    unittest.main()
