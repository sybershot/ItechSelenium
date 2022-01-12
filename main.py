from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from page_objects.yandex_search_page import YandexSearch
import tests.yandex_tests as ya_tests


PYTHON_KEYS = "python"
JAVA_KEYS = "java"

GECKO_SERVICE = Service('./resources/geckodriver.exe')
DRIVER = webdriver.Firefox(service=GECKO_SERVICE)

if __name__ == '__main__':

    try:
        yandex_po = YandexSearch(DRIVER)
        ya_tests.search_and_validate(yandex_po, PYTHON_KEYS)
        ya_tests.search_and_validate(yandex_po, JAVA_KEYS)

    finally:
        DRIVER.close()
