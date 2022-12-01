from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __main_page_logo = (By.XPATH, '//*[@class="app_logo"]')

    def is_page_logo_displayed(self):
        return self.is_displayed(self.__main_page_logo)
