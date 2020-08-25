import os, time, unittest, ddt, logging
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test_shuang.page.wecenter_login_page import WeCenterLoginPage


@ddt.ddt
class TestWeCenter(unittest.TestCase):
    URL = Config().get('URL')
    excelPath = DATA_PATH + '/yongli.xlsx'
    reader = ExcelReader(excelPath, sheet='login', title_line=True)

    def setUp(self):
        self.driver = WeCenterLoginPage().get(url=self.URL)
        self.driver.go_to_login()

    def tearDown(self):
        self.driver.close()

    @ddt.data(*reader.data)
    def test_click_login(self, data):
        username, passwd, err_message = tuple(data)
        self.driver.input_message(username=username, passwd=passwd)
        self.driver.login_click()
        try:
            inf = self.driver.get_failed_text()
            self.assertIn(err_message, inf)
            self.driver.save_screen_shot()
            logging.info("未登录成功，提示信息正确！")
        except:

            logger.info('登陆成功！')
            print(11111111)


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
