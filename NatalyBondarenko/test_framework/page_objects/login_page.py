from __future__ import annotations

from NatalyBondarenko.test_framework.page_objects.main_page import MainPage
from NatalyBondarenko.test_framework.utilities.decorators import auto_add_step
from NatalyBondarenko.test_framework.utilities.web_ui.base_page import BasePage
from NatalyBondarenko.test_framework.page_objects.locators import locators_Xpath
from typing import Union


@auto_add_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_user_name(self, user_name_value: Union[int, str]) -> LoginPage:
        self.send_keys(locators_Xpath.username_input, user_name_value)
        return self

    def set_password(self, password_value: Union[int, str]) -> LoginPage:
        self.send_keys(locators_Xpath.password_input, password_value)
        return self

    def click_login_button(self) -> LoginPage:
        self.click(locators_Xpath.login_button)
        return self

    def login(self, user_name_value: Union[int, str], password_value: Union[int, str]) -> MainPage:
        self.set_user_name(user_name_value).set_password(password_value).click_login_button()
        return MainPage(self._driver)

    def error_message_on_invalid_login(self, text: str) -> bool:
        return self.wait_until_element_value(locators_Xpath.error_message, text)

    def is_login_button_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.login_button)
