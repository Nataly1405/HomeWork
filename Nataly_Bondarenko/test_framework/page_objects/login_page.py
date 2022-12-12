from __future__ import annotations

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.main_page import MainPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.locators import locators_Xpath


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_user_name(self, user_name_value) -> LoginPage:
        self.send_keys(locators_Xpath.username_input, user_name_value)
        return self

    def set_password(self, password_value) -> LoginPage:
        self.send_keys(locators_Xpath.password_input, password_value)
        return self

    def click_login_button(self) -> LoginPage:
        self.click(locators_Xpath.login_button)
        return self

    def login(self, user_name_value, password_value) -> MainPage:
        self.set_user_name(user_name_value).set_password(password_value).click_login_button()
        return MainPage(self._driver)

    def is_empty_values_error_message_displayed(self) -> bool:
        return self.is_displayed_error_message(locators_Xpath.error_message,
                                               error_msg="Epic sadface: Username is required")

    def is_empty_password_error_message_displayed(self) -> bool:
        return self.is_displayed_error_message(locators_Xpath.error_message,
                                               error_msg="Epic sadface: Password is required")

    def is_error_message_on_locked_out_user_displayed(self) -> bool:
        return self.is_displayed_error_message(locators_Xpath.error_message,
                                               error_msg="Epic sadface: Sorry, this user has been locked out")

    def is_error_message_for_unregistered_user(self) -> bool:
        return self.is_displayed_error_message(locators_Xpath.error_message,
                                               error_msg="Epic sadface: Username and password"
                                                         " do not match any user in this service")

    def is_login_button_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.login_button)
