# -*- coding: utf-8 -*-
from group import Contact
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contacts(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Aleksandr", lastname="Zemskov", mobile="89201234567", nickname="alze"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def returt_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, wd, contacts):
        self.open_contact_page(wd)
        # заполнение формы контакты
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contacts.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contacts.lastname)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contacts.mobile)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contacts.nickname)
        # Подтверждение заполнения формы контакты
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.returt_home_page(wd)

    def open_contact_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
