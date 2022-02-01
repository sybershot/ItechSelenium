from typing import List

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base_pages.base_page import BasePage
from config.base_test import consts


class YandexSearchPage(BasePage):
    pager_locator = By.CLASS_NAME, 'pager__item_kind_next'
    search_query_locator = By.XPATH, '//*[@id="text"]'
    search_results_locator = By.CLASS_NAME, "serp-item"
    ad_locator = By.XPATH, ".//span[contains(text(), 'Реклама')]"

    def wait_for_search_results(self, timeout=consts.TIMEOUT):
        self.wait_for_element(self.pager_locator)

    def search(self, query):
        search_query: WebElement = self.driver.find_element(*self.search_query_locator)
        search_query.click()
        search_query.send_keys(query)
        search_query.send_keys(Keys.ENTER)

    def iterate_results(self, expected_key):
        results: List[WebElement] = self.driver.find_elements(*self.search_query_locator)
        for element in results:
            ads_attrib = element.find_elements(*self.ad_locator)
            if ads_attrib:
                continue
            yield element
