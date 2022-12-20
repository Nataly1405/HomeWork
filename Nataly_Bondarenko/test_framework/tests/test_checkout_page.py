import pytest
from Auto_Lessons.HomeWork.Nataly_Bondarenko.test_framework.utilities.config_parser import ReadConfig


@pytest.mark.regression
@pytest.mark.checkout
def test_set_values_and_continue(open_checkout_page, env):
    """
    A method to verify that we are able to go to the overview page from the checkout page
    """
    overview_page = open_checkout_page. \
        set_checkout_info(env.first_name, env.last_name, env.zip).click_continue_button()
    assert overview_page.is_payment_information_displayed() is True, \
        "User didn't succeed to forwarded to overview page"


def test_set_values_and_continue_test(open_checkout_page, env):
    """
    A method to verify that we are able to go to the overview page from the checkout page
    """
    overview_page = open_checkout_page. \
        set_checkout_info(env.first_name, env.last_name, env.zip).click_continue_button()
    assert overview_page.is_payment_information_displayed() is True, \
        "User didn't succeed to forwarded to overview page"


@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize("first_name_value, last_name_value, zip_value",
                         [("", "", ""), ("", f'{ReadConfig.get_last_name()}', f'{ReadConfig.get_zip()}'),
                          ("", f'{ReadConfig.get_last_name()}', "")],
                         ids=["no values", "empty first_name, last name, zip code", "empty first_name,"
                                                                                    "last name,empty zip code"])
def test_invalid_checkout_empty_values(open_checkout_page, first_name_value, last_name_value, zip_value):
    """
    A method to verify error message if we try to go to the overview page from the checkout page:
     1. if all values in information box are empty
     2. if name field is empty
     3. if empty and zip code fields are empty
    Expected result: error msg with text: "Error: First Name is required"
    """
    checkout_page = open_checkout_page
    checkout_page.set_first_name(first_name_value).set_last_name(last_name_value).set_zip(zip_value). \
        click_continue_button()
    assert checkout_page.error_message_on_invalid_checkout("Error: First Name is required") is True, \
        "Error message on empty values or empty username only, was not displayed"


@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize("first_name_value, last_name_value, zip_value",
                         [(f'{ReadConfig.get_first_name()}', "", ""),
                          (f'{ReadConfig.get_first_name()}', "", f'{ReadConfig.get_zip()}')],
                         ids=["first_name, empty last name, zip code",
                              "first_name,  empty last name, empty zip code"])
def test_invalid_checkout_empty_last_name(open_checkout_page, first_name_value, last_name_value, zip_value):
    """
    A method to verify error message if we try to go to the overview page from the checkout page:
     1. if name and zip code fields in information box are empty
     2. if lat name field is empty
     Expected result: error msg with text: "Error: Last Name is required"
    """
    checkout_page = open_checkout_page
    checkout_page.set_first_name(first_name_value).set_last_name(last_name_value).set_zip(zip_value). \
        click_continue_button()
    assert checkout_page.error_message_on_invalid_checkout("Error: Last Name is required") is True, \
        "Error message on empty last name value was not displayed"


@pytest.mark.regression
@pytest.mark.checkout
def test_invalid_checkout_empty_zip(open_checkout_page, env):
    """
    A method to verify that we are not able to go to the overview page from the checkout page
     if the zip code field is empty
     Expected result: error msg with text: "Error: Postal Code is required"
    """
    checkout_page = open_checkout_page
    checkout_page.set_first_name(env.first_name).set_last_name(env.last_name).set_zip("").click_continue_button()
    assert checkout_page.error_message_on_invalid_checkout("Error: Postal Code is required") is True, \
        "Error message on empty zip value was not displayed"


@pytest.mark.regression
@pytest.mark.checkout
def test_logout_from_checkout_page(open_checkout_page, open_login_page):
    """
    A method to verify that we are able to logout from the checkout page
    """
    open_checkout_page.click_menu_button().click_logout_button()
    login_page = open_login_page
    assert login_page.is_login_button_displayed() is True, "The logout button from checkout page doesn't work"


@pytest.mark.regression
@pytest.mark.checkout
def test_go_to_cart_page_over_cart_link(open_checkout_page, open_cart_page):
    """
    A method to verify that we are able to go back to the cart page over cart link from the checkout page
    """
    open_checkout_page.click_cart_button()
    cart_page = open_cart_page
    assert cart_page.is_cart_item_displayed() is True, "The cart link from checkout page doesn't work"
