import pytest


@pytest.mark.regression
@pytest.mark.main
def test_open_burger_menu(open_main_page):
    """
    A method to verify that we are able to open burger menu from main page
    """
    main_page = open_main_page
    main_page.click_menu_button()
    assert main_page.is_menu_page_is_displayed() is True, "The menu page was not open"


@pytest.mark.regression
@pytest.mark.main
def test_open_cart(open_main_page):
    """
    A method to verify that we are able to open cart from main page
    """
    main_page = open_main_page
    main_page.click_cart_button()
    assert main_page.is_cart_page_title_is_displayed() is True, "The cart page was not open"


@pytest.mark.regression
@pytest.mark.main
def test_add_item_to_cart(open_main_page):
    """
    A method to verify that we are able to add item to the cart from main page
    """
    main_page = open_main_page
    main_page.click_add_to_cart_button().click_cart_button()
    assert main_page.is_cart_item_list_is_displayed() is True, "The item from main paige was not added to the cart"


@pytest.mark.regression
@pytest.mark.main
def test_check_remove_from_main_page(open_main_page):
    """
    A method to verify that we are able to remove item from main page
    """
    main_page = open_main_page
    main_page.click_add_to_cart_button().click_remove_button_on_main_page()
    assert main_page.is_add_to_cart_is_displayed() is True, "The item was not removed"


@pytest.mark.regression
@pytest.mark.main
def test_logout(open_main_page, open_login_page):
    """
    A method to verify that we are able to logout from the site from main page
    """
    main_page = open_main_page
    main_page.click_menu_button().click_logout_button()
    login_page = open_login_page
    assert login_page.is_login_button_is_displayed() is True, "The user didn't succeed to logout from main page"
