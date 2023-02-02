import pytest
from Auto_Lessons.HomeWork.NatalyBondarenko.test_framework.utilities.config_parser import ReadConfig


@pytest.mark.regression
@pytest.mark.login
def test_login(open_login_page, env):
    """
    A method to verify that we are able to login
    """
    login_page = open_login_page
    main_page = login_page.login(env.user_name, env.password)
    assert main_page.is_page_logo_displayed() is True, "User was not logged-in"


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize("user_name_value, password_value", [("", ""), ("", f'{ReadConfig.get_password()}')],
                         ids=["no values", "no user_name, correct password"])
def test_invalid_login_empty_values(open_login_page, user_name_value, password_value):
    """
    A method to verify error message on invalid login if:
            1. both fields: "Username" and "Password" are empty.
            2. Only field: "Username"  is empty
    Expected result: we got error msg with text: "Epic sadface: Username is required"
    """
    login_page = open_login_page
    login_page.set_user_name(user_name_value).set_password(password_value).click_login_button()
    assert login_page.error_message_on_invalid_login("Epic sadface: Username is required") is True, \
        "Error message on empty values or empty username only, was not displayed"


@pytest.mark.regression
@pytest.mark.login
def test_invalid_login_empty_password(open_login_page, env):
    """
    A method to verify error message on invalid login if:
            1. Only field: "Password"  is empty
    Expected result: we got error msg with text: "Epic sadface: Password is required"
    """
    login_page = open_login_page
    login_page.set_user_name(env.user_name).set_password("").click_login_button()
    assert login_page.error_message_on_invalid_login("Epic sadface: Password is required") is True, \
        "Error message on empty password was not displayed"


@pytest.mark.regression
@pytest.mark.login
def test_error_message_on_locked_out_user(open_login_page, env):
    """
    A method to verify error message for locked out user:
            1. Enter "locked_out_user_name" and "password"
    Expected result: we got error msg with text: "Epic sadface: Sorry, this user has been locked out"
    """
    login_page = open_login_page
    login_page.set_user_name(env.locked_out_user_name).set_password(env.password).click_login_button()
    assert login_page.error_message_on_invalid_login("Epic sadface: Sorry, this user has been locked out") is True, \
        "Error message for locked out user was not displayed"


@pytest.mark.regression
@pytest.mark.login
def test_error_message_for_unregistered_user(open_login_page):
    """
    A method to verify error message for unregistered user:
            1. Enter username and password of an unregistered user
    Expected result: error msg with text: "Epic sadface: Username and password do not match any user in this service"
    """
    login_page = open_login_page
    login_page.set_user_name("test").set_password("test").click_login_button()
    assert login_page.error_message_on_invalid_login \
               ("Epic sadface: Username and password do not match any user in this service") is True, \
        "Error message for unregistered user was not displayed"
