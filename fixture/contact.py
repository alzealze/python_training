from selenium.webdriver.common.by import By


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
        wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_main_page()
        # Выбрать первый контакт
        wd.find_element(By.NAME, "selected[]").click()
        # Удалить выбранный первый контакт
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # Подтверждение удаления контакта
        wd.switch_to.alert.accept()
        self.open_main_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_main_page()
        # Нажимаем Edit первого контакта
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # Редактируем контакт
        self.fill_contact_form(new_contact_data)
        # Нажимаем Update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_main_page()
