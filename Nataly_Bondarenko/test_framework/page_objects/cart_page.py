from __future__ import annotations

import allure

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.checkout_page import CheckoutPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.item_page import ItemPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.decorators import auto_add_step
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.locators import locators_Xpath


@auto_add_step
class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_continue_shopping_button(self) -> CartPage:
        self.click(locators_Xpath.continue_shopping)
        return self

    # def remove_item_from_cart(self) -> CartPage:
    #     self.click(locators_Xpath.remove_first_item_from_cart)
    #     return self

    def is_cart_item_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.cart_item)

    def go_to_item_page(self) -> ItemPage:
        self.click(locators_Xpath.from_cart_to_item_page)
        return ItemPage(self._driver)

    def go_to_checkout(self) -> CheckoutPage:
        self.click(locators_Xpath.checkout)
        return CheckoutPage(self._driver)

    def click_menu_button(self) -> CartPage:
        self.click(locators_Xpath.menu_button)
        return self

    def click_logout_button(self) -> CartPage:
        self.click(locators_Xpath.logout)
        return self

    def is_cart_page_title_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.cart_page_title)
