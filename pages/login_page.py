from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CONFIG

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, CONFIG['classes']['login_input']))
        )
        inputs = self.driver.find_elements(By.CLASS_NAME, CONFIG['classes']['login_input'])
        inputs[0].send_keys(CONFIG["username"])
        inputs[1].send_keys(CONFIG["password"])
        login_btn = self.driver.find_element(By.CLASS_NAME, CONFIG['classes']['login_button'])
        login_btn.click()
