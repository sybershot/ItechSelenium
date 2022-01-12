from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexBasePage:
    YANDEX_BASE_URL = "http://www.yandex.by"

    def __init__(self, driver) -> None:
        self.driver = driver

    def go_to_home_page(self):
        return self.driver.get(self.YANDEX_BASE_URL)

    def wait_for_element(self, element_locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element_locator))
