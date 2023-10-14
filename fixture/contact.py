from selenium.webdriver.common.by import By
from model.contact import Contact


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
        if not (wd.current_url.endswith("localhost/addressbook/" or "/index.php") and len(wd.find_elements(By.NAME, "add")) > 0):
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

    def select_contacts_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_first_contacts(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def modify_first_contact(self):
        self.select_edit_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_main_page()
        self.select_edit_contact_by_index(index)
        # Редактируем контакт
        self.fill_contact_form(new_contact_data)
        # Нажимаем Update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_main_page()
        self.contact_cache = None

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def select_edit_first_contact(self):
        wd = self.app.wd
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
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id))
        return list(self.contact_cache)
