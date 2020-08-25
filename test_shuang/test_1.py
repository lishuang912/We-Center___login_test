import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email


class TestWeCenter(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/yongli.xlsx'
    locator_login_btn = (By.XPATH, '/html/body/div[1]/div/div[4]/a[1]')

    locator_login_user_name = (By.XPATH, '//*[@id="aw-login-user-name"]')
    locator_login_passwd = (By.XPATH, '//*[@id="aw-login-user-password"]')
    locator_login_sumbit = (By.XPATH, '//*[@id="login_submit"]')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_click_login(self):
        # datas = ExcelReader(self.excel)
        # print(datas)
        # correct
        self.driver.find_element(*self.locator_login_btn).click()
        time.sleep(3)
        # assert '登录' in self.driver.title
        self.driver.find_element(*self.locator_login_user_name).send_keys('admin')
        self.driver.find_element(*self.locator_login_passwd).send_keys('admin123!@#')
        self.driver.find_element(*self.locator_login_sumbit).click()
        logger.info(self.driver.title)


if __name__ == '__main__':
    # unittest.main()
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='We Center社区问答_测试报告', description='html报告')
        runner.run(TestWeCenter('test_click_login'))
    e = Email(title='We Center登录测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='18252068105@163.com',
              server='smtp.qq.com',
              sender='1336181723@qq.com',
              password='pinxywnwmdzsihac',
              path=report
              )
    e.send()
