from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contacts):
        wd = self.app.wd
        self.open_contact_page()
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
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def return_main_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # Выбрать первый контакт
        wd.find_element(By.NAME, "selected[]").click()
        # Удалить выбранный первый контакт
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # Подтверждение удаления контакта
        wd.switch_to.alert.accept()
        self.return_main_page()
