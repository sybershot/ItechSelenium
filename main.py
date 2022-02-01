from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.base_test.consts import PYTHON_KEY, JAVA_KEY
from page_objects.yandex_search_page import YandexSearchPage
import tests.yandex_tests as ya_tests

if __name__ == '__main__':

    gecko_service = Service('./resources/geckodriver.exe')
    driver = webdriver.Firefox(service=gecko_service)

    try:
        yandex_po = YandexSearchPage(driver)
        ya_tests.search_and_validate(yandex_po, PYTHON_KEY)
        ya_tests.search_and_validate(yandex_po, JAVA_KEY)

    finally:
        driver.close()
