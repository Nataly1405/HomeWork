from __future__ import annotations

from NatalyBondarenko.test_framework.page_objects.locators import locators_Xpath
from NatalyBondarenko.test_framework.utilities.web_ui.base_page import BasePage


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_first_item_located(self) -> bool:
        return self.is_located(locators_Xpath.first_item_name_on_page)

    def click_back_to_products(self) -> ItemPage:
        self.click(locators_Xpath.back_to_products_from_item_page)
        return self

    def click_add_to_cart(self) -> ItemPage:
        self.click(locators_Xpath.add_to_cart_on_item_page)
        return self

    def is_remove_button_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.remove_on_item_page)

    def click_on_remove_button(self) -> ItemPage:
        self.click(locators_Xpath.remove_on_item_page)
        return self

    def is_add_to_cart_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.add_to_cart_on_item_page)

    def click_on_cart(self) -> ItemPage:
        self.click(locators_Xpath.cart_link_on_item_page)
        return self

    def is_cart_page_title_displayed(self) -> bool:
        return self.is_displayed(locators_Xpath.cart_page_title)

    def click_menu(self) -> ItemPage:
        self.click(locators_Xpath.menu_button)
        return self

    def click_logout(self) -> ItemPage:
        self.click(locators_Xpath.logout)
        return self
