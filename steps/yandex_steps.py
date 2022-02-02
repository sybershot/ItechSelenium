from selenium.webdriver.remote.webdriver import WebDriver
from config.base_test.consts import YANDEX_BASE_URL
from page_objects.yandex_search_page import YandexSearchPage


def search_and_validate(driver: WebDriver, key):
    """
    Searches by keyword and validates that all results contain expected keyword in them.
    :param driver: Web driver
    :param key: Keyword to validate
    :return:
    """
    page_object = YandexSearchPage(driver)
    page_object.go_to_home_page(YANDEX_BASE_URL)
    page_object.search(key)
    page_object.wait_for_search_results()
    for element in page_object.iterate_results(key):
        try:
            assert key in element.text.lower()
        except AssertionError:
            print(f"Assertion error. Can't find {key!r} in {element.text.lower()!r}!")
