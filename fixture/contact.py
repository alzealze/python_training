from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contacts):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contacts)
        # Подтверждение заполнения формы контакты
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_main_page()
        self.contact_cache = None

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_field_value("firstname", contacts.firstname)
        self.change_field_value("lastname", contacts.lastname)
        self.change_field_value("nickname", contacts.nickname)
        self.change_field_value("mobile", contacts.mobile)

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_firstname).click()
            wd.find_element(By.NAME, field_firstname).clear()
            wd.find_element(By.NAME, field_firstname).send_keys(text)

    def return_main_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/" or "/index.php")
                and len(wd.find_elements(By.NAME, "add")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contacts_by_index(index)
        # Удалить выбранный контакт
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # Подтверждение удаления контакта
        wd.switch_to.alert.accept()
        self.open_main_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        self.select_contacts_by_id(id)
        # Удалить выбранный контакт
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # Подтверждение удаления контакта
        wd.switch_to.alert.accept()
        self.open_main_page()
        self.contact_cache = None

    def select_contacts_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def select_contacts_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_first_contacts(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def modify_first_contact(self):
        self.open_contact_to_edit_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_main_page()
        self.open_contact_to_edit_by_index(index)
        # Редактируем контакт
        self.fill_contact_form(new_contact_data)
        # Нажимаем Update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_main_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_main_page()
        self.open_contact_to_edit_by_id(id)
        # Редактируем контакт
        self.fill_contact_form(contact)
        # Нажимаем Update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_main_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()


    def open_contact_to_edit_first(self):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()

    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                firstname_text = cells[2].text
                lastname_text = cells[1].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobile=mobile,
                       secondaryphone=secondaryphone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobile=mobile, secondaryphone=secondaryphone)
