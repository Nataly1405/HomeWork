import pytest

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.item_page import ItemPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.login_page import LoginPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.main_page import MainPage
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


@pytest.fixture()
def return_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture()
def open_item_page(open_main_page):
    item_page = open_main_page.click_on_first_item()
    return item_page


@pytest.fixture()
def return_item_page(create_driver):
    return ItemPage(create_driver)


@pytest.fixture()
def open_cart_page(open_main_page):
    cart_page = open_main_page.click_cart_button()
    return cart_page


@pytest.fixture()
def open_cart_page_with_item(open_main_page):
    main_page = open_main_page
    main_page.click_add_to_cart_button()
    cart_page = main_page.click_cart_button()
    return cart_page


@pytest.fixture()
def open_checkout_page(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    checkout_page = cart_page.go_to_checkout()
    return checkout_page


@pytest.fixture()
def open_overview_page(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.set_checkout_info(ReadConfig.get_first_name(), ReadConfig.get_last_name(), ReadConfig.get_zip())
    overview_page = checkout_page.click_continue_button()
    return overview_page
