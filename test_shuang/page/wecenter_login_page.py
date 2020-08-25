from selenium.webdriver.common.by import By
from test_shuang.common.page import Page
from utils.log import logger


class WeCenterLoginPage(Page):

    locator_login_btn = (By.XPATH, '/html/body/div[1]/div/div[4]/a[1]')

    locator_login_user_name = (By.XPATH, '//*[@id="aw-login-user-name"]')
    locator_login_passwd = (By.XPATH, '//*[@id="aw-login-user-password"]')
    locator_login_sumbit = (By.XPATH, '//*[@id="login_submit"]')
    errorMessage = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/form/ul/li[3]')

    def go_to_login(self):
        """跳转登录界面"""
        self.find_element(*self.locator_login_btn).click()
        return self

    def input_message(self, username, passwd):
        """输入用户名密码"""
        self.find_element(*self.locator_login_user_name).send_keys(username)
        self.find_element(*self.locator_login_passwd).send_keys(passwd)

    def login_click(self):
        self.find_element(*self.locator_login_sumbit).click()

    def get_failed_text(self):
        info = self.find_element(*self.errorMessage).text
        logger.info('login failed : %s' % info)
        return info
