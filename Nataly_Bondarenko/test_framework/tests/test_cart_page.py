import pytest


@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping(return_main_page, open_cart_page_with_item):
    """
    A method to verify that we are able to continue shopping from the cart page
    """
    main_page = return_main_page
    open_cart_page_with_item.click_on_continue_shopping_button()
    assert main_page.is_page_logo_displayed() is True, "The `Continue shopping` button doesn't work"


@pytest.mark.regression
@pytest.mark.cart
def test_move_to_item_page(open_cart_page_with_item, return_item_page):
    """
    A method to verify that we are able to move to item page from the cart page
    """
    item_page = return_item_page
    open_cart_page_with_item.go_to_item_page_from_cart()
    assert item_page.is_item_page_is_displayed() is True, "text"


@pytest.mark.regression
@pytest.mark.cart
def test_go_to_checkout(open_cart_page_with_item):
    """
    A method to verify that we are able to go to checkout page from the cart page
    """
    cart_page = open_cart_page_with_item.go_to_checkout()
    assert cart_page.is_first_name_field_is_displayed() is True, "The `checkout` button doesn't work"


@pytest.mark.regression
@pytest.mark.cart
def test_logout_from_cart_page(open_cart_page, open_login_page):
    """
    A method to verify that we are able to logout from the cart page
    """
    open_cart_page.click_menu_button().click_logout_button_cart()
    login_page = open_login_page
    assert login_page.is_login_button_is_displayed() is True, "Logout doesn't work from cart page"


@pytest.mark.regression
@pytest.mark.cart
@pytest.mark.xfail(reason="Jira: FIX-12345")
def test_error_on_go_to_checkout_with_empty_cart(open_cart_page):
    """
    A method to verify that we are not able to go to checkout page with empty cart
    """
    cart_page = open_cart_page.go_to_checkout()
    assert cart_page.is_first_name_field_is_displayed() is True, "User can not go to checkout with empty cart"
