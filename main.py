from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from page_objects.yandex_search_page import YandexSearch

PYTHON_KEYS = "python"
JAVA_KEYS = "java"

GECKO_SERVICE = Service('./resources/geckodriver.exe')
DRIVER = webdriver.Firefox(service=GECKO_SERVICE)

if __name__ == '__main__':

    try:
        yandex_po = YandexSearch(DRIVER)
        yandex_po.search(PYTHON_KEYS)
        yandex_po.validate(PYTHON_KEYS)
        yandex_po.search(JAVA_KEYS)
        yandex_po.validate(JAVA_KEYS)

    finally:
        DRIVER.close()
