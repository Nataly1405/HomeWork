from __future__ import annotations


from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.locators import locators_Xpath


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_payment_information_is_displayed(self):
        return self.is_displayed(locators_Xpath.payment_information)
