from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Auto_Lessons.HomeWork.NatalyBondarenko.HW17.credentials import base_url, user_name, password
from Auto_Lessons.HomeWork.NatalyBondarenko.HW17.locators import username_input, password_input, \
    login_button, logout, menu_button


def test_login():
    chrome_driver = Chrome('chromedriver.exe')
    wait = WebDriverWait(chrome_driver, 10)
    chrome_driver.get(base_url)
    chrome_driver.maximize_window()

    user_name_element = wait.until(EC.presence_of_element_located(username_input))
    user_name_element.send_keys(user_name)

    password_element = wait.until(EC.presence_of_element_located(password_input))
    password_element.send_keys(password)

    login_button_element = wait.until(EC.presence_of_element_located(login_button))
    login_button_element.click()

    go_to_menu = wait.until(EC.presence_of_element_located(menu_button))
    go_to_menu.click()

    logout_button_element = wait.until(EC.presence_of_element_located(logout))
    is_logout_button = logout_button_element.is_displayed()

    assert is_logout_button is True, 'User was not login'
