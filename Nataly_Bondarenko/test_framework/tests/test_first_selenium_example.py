import pytest
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.config_parser import ReadConfig


def test_login(open_login_page):
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())
    # main_page = login_page.login('standard_user', 'secret_sauce')
    assert main_page.is_page_logo_displayed() is True, "User was not logged-in"
