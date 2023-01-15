from __future__ import annotations

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.locators import locators_Xpath
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.overview_page import OverviewPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.decorators import auto_add_step
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from typing import Union


@auto_add_step
class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_first_name_field_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.first_name_input)

    # def is_checkout_info_is_displayed(self) -> bool:
    #     return self.is_displayed(locators_Xpath.checkout_info)

    def click_continue_button(self) -> OverviewPage:
        self.click(locators_Xpath.continue_button)
        return OverviewPage(self._driver)

    def set_first_name(self, first_name_value: str) -> CheckoutPage:
        self.send_keys(locators_Xpath.first_name_input, first_name_value)
        return self

    def set_last_name(self, last_name_value: str) -> CheckoutPage:
        self.send_keys(locators_Xpath.last_name_input, last_name_value)
        return self

    def set_zip(self, zip_value: Union[int, str]) -> CheckoutPage:
        self.send_keys(locators_Xpath.zip_input, zip_value)
        return self

    def set_checkout_info(self, first_name_value: str, last_name_value: str,
                          zip_value: Union[int, str]) -> CheckoutPage:
        self.set_first_name(first_name_value).set_last_name(last_name_value).set_zip(zip_value)
        return CheckoutPage(self._driver)

    def error_message_on_invalid_checkout(self, text: str) -> bool:
        return self.wait_until_element_value(locators_Xpath.error_message, text)

    def click_cancel_button(self) -> CheckoutPage:
        self.click(locators_Xpath.cancel_button)
        return self

    def click_menu_button(self) -> CheckoutPage:
        self.click(locators_Xpath.menu_button)
        return self

    def click_logout_button(self) -> CheckoutPage:
        self.click(locators_Xpath.logout)
        return self

    # def click_cart_button(self) -> CartPage:
    #     self.click(locators_Xpath.cart_link_on_item_page)
    #     #return self
    #     return CartPage(self._driver)

    def click_cart_button(self) -> CheckoutPage:
        self.click(locators_Xpath.cart_link_on_item_page)
        return self
