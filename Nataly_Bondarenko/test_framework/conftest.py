import pytest

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.login_page import LoginPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.config_parser import ReadConfig
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_main_page(open_login_page):
    return open_login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())
