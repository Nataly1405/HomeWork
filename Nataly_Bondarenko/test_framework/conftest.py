import pytest
import json

from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.CONSTANTS import ROOT_DIR
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.item_page import ItemPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.login_page import LoginPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.page_objects.main_page import MainPage
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.configurations import Configurations
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.driver_factory import DriverFactory


@pytest.fixture()
def env():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def create_driver(env):
    driver = DriverFactory.create_driver(driver_id=env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_main_page(open_login_page, env):
    return open_login_page.login(env.user_name, env.password)


@pytest.fixture()
def init_main_page(create_driver):
    """
    This function initializes the main page in order to avoid circular import
    """
    return MainPage(create_driver)


@pytest.fixture()
def open_item_page(open_main_page):
    item_page = open_main_page.click_on_first_item()
    return item_page


@pytest.fixture()
def init_item_page(create_driver):
    """
    This function initializes the item page in order to avoid circular import
    """
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
