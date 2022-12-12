from selenium.webdriver.common.by import By

# Xpath:
# Login Page
username_input = (By.XPATH, '//*[@id="user-name"]')
password_input = (By.XPATH, '//*[@id="password"]')
login_button = (By.XPATH, '//*[@id="login-button"]')
error_message = (By.XPATH, '//*[@data-test="error"]')


# Main Page
app_logo = (By.XPATH, '//*[@class="app_logo"]')
menu_button = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
menu_page = (By.XPATH, '//*[@class ="bm-menu"]')
product_sort_container = (By.XPATH, '//*[@class="product_sort_container"]')
first_item_name = (By.XPATH, '//*[@class="inventory_item_name"]')
item_page = (By.XPATH, '//*[@id="root"]')
back_to_products_from_item_page = (By.XPATH, '//*[@id="back-to-products"]')
remove_button_on_maim_page = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
filtered_from_a_to_z = (By.XPATH, '//*[@value="az"]')
filtered_from_z_to_a = (By.XPATH, '//*[@value="za"]')
filtered_by_price_from_low_to_high = (By.XPATH, '//*[@value="lohi"]')
filtered_by_price_from_high_to_low = (By.XPATH, '//*[@value="hilo"]')
first_item_on_the_main_page = (By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
logout = (By.XPATH, '//*[@id="logout_sidebar_link"]')
reset_sidebar_link = (By.XPATH, '//*[@id="logout_sidebar_link"]')

# Item Page
add_to_cart_on_item_page = (By.XPATH, '//*[@class="btn btn_primary btn_small btn_inventory"]')
remove_on_item_page = (By.XPATH, '//*[@class="btn btn_secondary btn_small btn_inventory"]')
cart_link_on_item_page = (By.XPATH, '//*[@class="shopping_cart_link"]')

# Cart Page
cart_page_title = (By.XPATH, '//*[@class ="title"]')
add_to_cart = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
cart_link = (By.XPATH, '//*[@class="shopping_cart_link"]')
cart_item = (By.XPATH, '//*[@class="cart_item_label"]')
remove_first_item_from_cart = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
from_cart_to_item_page = (By.XPATH, '//*[@class="inventory_item_name"]')
continue_shopping = (By.XPATH, '//*[@id="continue-shopping"]')
checkout = (By.XPATH, '//*[@id="checkout"]')

# Checkout page: client information
checkout_info = (By.XPATH, '*[@class="checkout_info"]')
first_name_input = (By.XPATH, '//*[@id="first-name"]')
last_name_input = (By.XPATH, '//*[@id="last-name"]')
zip_input = (By.XPATH, '//*[@id="postal-code"]')
data_error = (By.XPATH, '//*[@data-test="error"]')
error = (By.XPATH, '//*[@class="error-button"]')
error_message_checkout_inf_empty_values = (By.XPATH, '//*[@data-test="error"]')
cancel_button = (By.XPATH, '//*[@id="cancel"]')
continue_button = (By.XPATH, '//*[@id="continue"]')

# Overview page: payment
payment_information = (By.XPATH, '//*[@class="summary_value_label"]')
summary_subtotal = (By.XPATH, '//*[@class="summary_subtotal_label"]')
summary_tax = (By.XPATH, '//*[@class="summary_tax_label"]')
total = (By.XPATH, '//*[@class="summary_total_label"]')
finish_button = (By.XPATH, '//*[@id="finish"]')
cancel_on_payment_page = (By.XPATH, '//*[@class="btn btn_secondary back btn_medium cart_cancel_link"]')

# Footer
twitter = (By.XPATH, '//*[@class="social_twitter"]')
facebook = (By.XPATH, '//*[@class="social_facebook"]')
linkedin = (By.XPATH, '//*[@class="social_linkedin"]')
