from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    gecko_service = Service('./resources/geckodriver.exe')
    driver = webdriver.Firefox(service=gecko_service)
    try:
        driver.get("http://www.yandex.by")
        assert "Яндекс" in driver.title
        search_query: WebElement = driver.find_element(By.XPATH, '//*[@id="text"]')
        search_query.click()
        search_query.send_keys('python')
        search_query.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 5)
        content = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]')))
        assert content  # Trigger wait driver, because it's a lazy thing
        assert "нашлось" in driver.title
        assert "python.org" in driver.page_source, "Failed to find python.org link in search results!"

    finally:
        driver.close()
