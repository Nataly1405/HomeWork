from selenium.webdriver.common.by import By

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
