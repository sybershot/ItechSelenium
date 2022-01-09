from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexSearch():
    YANDEX_URL = "http://www.yandex.by"
    YANDEX_NAME = "Яндекс"

    def __init__(self, driver) -> None:
        self.driver = driver

    def search(self, query):
        self.driver.get(self.YANDEX_URL)
        assert self.YANDEX_NAME in self.driver.title, f"Failed to find {self.YANDEX_NAME} in tab title!"
        search_query: WebElement = self.driver.find_element(By.XPATH, '//*[@id="text"]')
        search_query.click()
        search_query.send_keys(query)
        search_query.send_keys(Keys.ENTER)

    def validate(self, expected_key):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]')))
        found_element = False
        for element in self.driver.find_elements(By.CLASS_NAME, "OrganicTitleContentSpan"):
            if expected_key in element.text.lower():
                found_element = True
                break
        if not found_element:
            print(f"Failed to find {expected_key!r} in search results!")
        else:
            print(f"Successfully found {expected_key!r} in OrganicTitleContentSpan")
