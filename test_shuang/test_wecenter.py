import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

URL = "http://39.105.34.27/project2/?/"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')
# 点击登陆后
# 等待进入新的界面----登陆界面

locator_login_btn = (By.XPATH, '/html/body/div[1]/div/div[4]/a[1]')

locator_login_user_name = (By.XPATH, '//*[@id="aw-login-user-name"]')
locator_login_passwd = (By.XPATH, '//*[@id="aw-login-user-password"]')
locator_login_sumbit = (By.XPATH, '//*[@id="login_submit"]')
# locator_su = (By.ID, 'su')
# locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.implicitly_wait(3)
driver.find_element(*locator_login_btn).click()
assert '登录' in driver.title

driver.find_element(*locator_login_user_name).send_keys('admin')
driver.find_element(*locator_login_passwd).send_keys('admin23!@#')
driver.find_element(*locator_login_sumbit).click()
time.sleep(2)
errorMessage = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/form/ul/li[3]')
err = driver.find_element(*errorMessage).text
print(err)
time.sleep(2)
'''
locator_post = (By.XPATH, '//*[@id="header_publish"]')
ele_post = driver.find_element(*locator_post)

action = ActionChains(driver)
action.move_to_element(ele_post).perform()

locator_post_question = (By.LINK_TEXT, '问题')
# locator_post_question = (By.XPATH, '/html/body/div[1]/div/div[5]/div/ul/li[1]/form/a')
driver.find_element(*locator_post_question).click()
assert '发布' in driver.title

# 问题标题
locator_question_title = (By.XPATH, '//*[@id="question_contents"]')
driver.find_element(*locator_question_title).send_keys('test')


# 下拉框
locator_select = (By.XPATH, '//*[@id="question_form"]/div/div[1]/div[1]/div[2]')
driver.find_element(*locator_select).click()
locator_select_c = (By.XPATH, '//*[@id="question_form"]/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]/a')
driver.find_element(*locator_select_c).click()



# s = Select(ele_select)
# s.select_by_visible_text("啦啦啦")

# 问题补充
# frame_ref = (By.XPATH, '//*[@id="cke_1_contents"]')
# driver.switch_to.frame(frame_ref)
# locator_text = (By.XPATH, '/html/body')
# driver.find_element(*locator_text).send_keys('abcdefg')

time.sleep(2)
locator_confirm_submit = (By.XPATH, '//*[@id="publish_submit"]')
driver.find_element(*locator_confirm_submit).click()
time.sleep(1)
try:
    driver.find_element_by_xpath('/html/body/div[8]/div').text
except:
    print('success')


# assert 'test_double' in driver.title
# print('发布成功！')
driver.quit()
'''
driver.quit()