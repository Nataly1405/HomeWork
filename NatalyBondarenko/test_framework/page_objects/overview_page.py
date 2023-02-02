from __future__ import annotations

from NatalyBondarenko.test_framework.utilities.web_ui.base_page import BasePage
from NatalyBondarenko.test_framework.page_objects.locators import locators_Xpath


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_payment_information_displayed(self):
        return self.is_displayed(locators_Xpath.payment_information)
