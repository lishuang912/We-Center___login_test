from selenium.webdriver.common.by import By
from test_shuang.common.page import Page
from utils.log import logger


class WeCenterLoginPage(Page):
    locator_login_btn = (By.XPATH, '/html/body/div[1]/div/div[4]/a[1]')

    def go_to_login(self):
        """跳转登录界面"""
        self.find_element(*self.locator_login_btn).click()

