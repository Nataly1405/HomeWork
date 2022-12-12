import pytest


@pytest.mark.regression
@pytest.mark.item
def test_click_on_item_and_open_item_page(open_main_page):
    """
    A method to verify that we are able to click on item and go to the item page
    """
    main_page = open_main_page
    item_page = main_page.click_on_first_item()
    assert item_page.is_item_page_is_displayed() is True, "The item page information was not open"


@pytest.mark.regression
@pytest.mark.item
def test_back_to_products_from_item_page(return_main_page, open_item_page):
    """
    A method to verify that we are able to go back to the products on main page from the item_page
    """
    maim_page = return_main_page
    open_item_page.click_back_to_products()
    assert maim_page.is_item_page_is_displayed() is True, "The button `Back to products` on item page doesn't work"


@pytest.mark.regression
@pytest.mark.item
def test_add_to_cart_on_item_page(open_item_page):
    """
    A method to verify that we are able to add item to the cart from the item page
    """
    item_page = open_item_page.click_add_to_cart_on_item_page_button()
    assert item_page.is_remove_button_is_displayed() is True, "The button `Add to cart`on item page doesn't work"


@pytest.mark.regression
@pytest.mark.item
def test_remove_on_item_page(open_item_page):
    """
    A method to verify that we are able to remove item from the item page
    """
    item_page = open_item_page.click_add_to_cart_on_item_page_button().click_on_remove_on_item_page()
    assert item_page.is_add_to_cart_is_displayed_on_item_page() is True, \
        "The button `Add to cart`on item page doesn't work"


@pytest.mark.regression
@pytest.mark.item
def test_open_cart_page(open_item_page):
    """
    A method to verify that we are able to open the cart page from the item page
    """
    item_page = open_item_page.click_add_to_cart_on_item_page_button().click_on_cart_item_page()
    assert item_page.is_cart_page_title_is_displayed() is True, "The cart button on main page doesn't work"


@pytest.mark.regression
@pytest.mark.item
def test_logout_from_main_pge(open_login_page, open_item_page):
    """
    A method to verify that we are able to logout from the item page
    """
    open_item_page.click_menu_item_page().click_logout_item_page()
    login_page = open_login_page
    assert login_page.is_login_button_is_displayed() is True, "The logout button on item paige doesn't work"
