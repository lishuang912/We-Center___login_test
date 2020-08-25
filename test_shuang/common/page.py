from test_shuang.common.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.log import logger


class Page(Browser):
    # 更多的封装请自己动手...
    def __init__(self, page=None, browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        """查找单一元素"""
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(args))
            # log.logger.info('The page of %s had already find the element %s'%(self,loc))
            # return self.driver.find_element(*loc)
        except Exception as e:
            logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            # logger.info('The page of %s had already find the element %s' % (self, args))
            return self.driver.find_element(*args)

    def find_elements(self, *args):
        """查找一组元素"""
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(args))
            # log.logger.info('The page of %s had already find the element %s' % (self, loc))
            # return self.driver.find_elements(*loc)
        except Exception as e:
            logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            # logger.info('The page of %s had already find the element %s' % (self, args))
            return self.driver.find_elements(*args)