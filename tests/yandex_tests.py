from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.base_test.consts import PYTHON_KEY, JAVA_KEY
import steps.yandex_steps as ya_steps

if __name__ == '__main__':

    gecko_service = Service('resources/geckodriver.exe')
    driver = webdriver.Firefox(service=gecko_service)

    try:
        ya_steps.search_and_validate(driver, PYTHON_KEY)
        ya_steps.search_and_validate(driver, JAVA_KEY)

    finally:
        driver.close()
