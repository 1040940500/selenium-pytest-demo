import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.settings import CONFIG

@pytest.fixture(scope="module")
def driver():
    service = Service(CONFIG["chromedriver_path"])
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(CONFIG['url'])
    yield driver
    driver.quit()
