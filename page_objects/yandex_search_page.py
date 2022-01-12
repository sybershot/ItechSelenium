from typing import List

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base_pages.yandex_base_page import YandexBasePage


class YandexSearch(YandexBasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def wait_for_search_results(self, timeout=5):
        self.wait_for_element((By.CLASS_NAME, 'pager__item_kind_next'))

    def search(self, query):
        search_query: WebElement = self.driver.find_element(By.XPATH, '//*[@id="text"]')
        search_query.click()
        search_query.send_keys(query)
        search_query.send_keys(Keys.ENTER)

    def validate(self, expected_key):
        results: List[WebElement] = self.driver.find_elements(By.CLASS_NAME, "serp-item")
        for element in results:
            ads_attrib = element.find_elements(By.XPATH,".//span[contains(text(),'Реклама')]")
            if ads_attrib:
                continue
            try:
                assert expected_key in element.text.lower()
            except AssertionError:
                print(f"Assertion error. Can't find {expected_key!r} in {element.text.lower()!r}!")
