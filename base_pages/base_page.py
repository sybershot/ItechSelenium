from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.base_test import consts
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def go_to_home_page(self, url):
        return self.driver.get(url)

    def wait_for_element(self, element_locator, timeout=consts.TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element_locator))
