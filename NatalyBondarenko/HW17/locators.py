from selenium.webdriver.common.by import By

# Find and write 30 different XPATH and 15 CSS locators
# web site: https://www.saucedemo.com/

# Xpath:
# Login Page
username_input = (By.XPATH, '//*[@id="user-name"]')
password_input = (By.XPATH, '//*[@id="password"]')
login_button = (By.XPATH, '//*[@id="login-button"]')
error_message_on_wrong_password = (By.XPATH, '//*[@class="error-message-container"]')

# Main Page
menu_button = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
product_sort_container = (By.XPATH, '//*[@class="product_sort_container"]')
filtered_from_a_to_z = (By.XPATH, '//*[@value="az"]')
filtered_from_z_to_a = (By.XPATH, '//*[@value="za"]')
filtered_by_price_from_low_to_high = (By.XPATH, '//*[@value="lohi"]')
filtered_by_price_from_high_to_low = (By.XPATH, '//*[@value="hilo"]')
first_item_on_the_main_page = (By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
logout = (By.XPATH, '//*[@id="logout_sidebar_link"]')
reset_sidebar_link = (By.XPATH, '//*[@id="logout_sidebar_link"]')

# Shopping cart
add_to_cart = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
shopping_cart_link = (By.XPATH, '//*[@class="shopping_cart_link"]')
inventory_item_name = (By.XPATH, '//*[@class="inventory_item_name"]')
remove_from_cart = (By.XPATH, '//*[@id="remove-sauce-labs-onesie"]')
continue_shopping = (By.XPATH, '//*[@id="continue-shopping"]')
checkout = (By.XPATH, '//*[@id="checkout"]')

# Checkout page: client information
first_name_input = (By.XPATH, '//*[@id="first-name"]')
last_name_input = (By.XPATH, '//*[@id="last-name"]')
postal_code_input = (By.XPATH, '//*[@id="postal-code"]')
data_error = (By.XPATH, '//*[@data-test="error"]')
cancel_button = (By.XPATH, '//*[@id="cancel"]')
continue_button = (By.XPATH, '//*[@id="continue"]')

# Checkout page: payment
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

# CSS
# Login Page
css_username_input = (By.CSS_SELECTOR, '#user-name')
css_password = (By.CSS_SELECTOR, '#password')
css_login_button = (By.CSS_SELECTOR, '#login-button')
css_error_message_on_wrong_password = (By.CSS_SELECTOR, '[data-test="error"]')

# Main Page
css_menu_button = (By.CSS_SELECTOR, '#react-burger-menu-btn')

# Shopping cart
css_add_to_cart_first_item = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
css_shopping_cart_link = (By.CSS_SELECTOR, '[class="shopping_cart_link"]')
css_remove_from_cart = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
css_continue_shopping = (By.CSS_SELECTOR, '#continue-shopping')
css_checkout = (By.CSS_SELECTOR, '#checkout')

# Checkout page: client information
css_first_name_input = (By.CSS_SELECTOR, '#first-name')
css_last_name_input = (By.CSS_SELECTOR, '#last-name')
css_postal_code_input = (By.CSS_SELECTOR, '#postal-code')
css_data_error = (By.CSS_SELECTOR, '[data-test="error"]')
css_cancel_button = (By.CSS_SELECTOR, '#cancel')
css_continue_button = (By.CSS_SELECTOR, '#continue')
