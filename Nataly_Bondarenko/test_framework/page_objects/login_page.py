from __future__ import annotations

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.main_page import MainPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_name_input = (By.XPATH, '//*[@id="user-name"]')
    __password_input = (By.XPATH, '//*[@id="password"]')
    __login_button = (By.XPATH, '//*[@id="login-button"]')

    def set_user_name(self, user_name_value):
        self.send_keys(self.__user_name_input, user_name_value)
        return self

    def set_password(self, password_value):
        self.send_keys(self.__password_input, password_value)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def login(self, user_name_value, password_value) -> MainPage:
        self.set_user_name(user_name_value).set_password(password_value).click_login_button()
        return MainPage(self._driver)
