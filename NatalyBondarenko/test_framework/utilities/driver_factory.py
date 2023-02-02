from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as C_Options
from selenium.webdriver.firefox.options import Options as F_Options
from selenium.webdriver.edge.options import Options as E_Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=True, chrome_option=C_Options()):
        if int(driver_id) == DriverFactory.CHROME:
            chrome_option == C_Options()
            if is_headless:
                chrome_option.add_argument('--headless')
                chrome_option.add_argument('--no-sandbox')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
