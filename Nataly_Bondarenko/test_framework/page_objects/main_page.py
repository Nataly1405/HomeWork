from __future__ import annotations

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.cart_page import CartPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.item_page import ItemPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.locators import locators_Xpath


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_page_logo_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.app_logo)

    def click_menu_button(self) -> MainPage:
        self.click(locators_Xpath.menu_button)
        return self

    def is_menu_page_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.menu_page)

    def click_cart_button(self) -> CartPage:
        self.click(locators_Xpath.cart_link)
        return CartPage(self._driver)

    def is_cart_page_title_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.cart_page_title)

    def click_add_to_cart_button(self) -> MainPage:
        self.click(locators_Xpath.add_to_cart)
        return self

    def is_cart_item_list_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.cart_item)

    def click_on_first_item(self) -> ItemPage:
        self.click(locators_Xpath.first_item_name)
        return ItemPage(self._driver)

    def click_remove_button_on_main_page(self) -> MainPage:
        self.click(locators_Xpath.remove_button_on_maim_page)
        return self

    def is_add_to_cart_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.add_to_cart)

    def click_logout_button(self) -> MainPage:
        self.click(locators_Xpath.logout)
        return self

    def is_item_page_is_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.item_page)
