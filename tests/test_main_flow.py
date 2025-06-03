from pages.login_page import LoginPage
from utils.logger import log
from config.settings import CONFIG

def test_login_flow(driver):
    log("开始测试登录流程", CONFIG['log_file'])
    login_page = LoginPage(driver)
    login_page.login()
    assert "qljc" in driver.current_url
