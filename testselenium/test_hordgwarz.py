# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/916:30
# 开发工具: PyCharm
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHordgwarz():
    def setup(self):
        self.driver=selenium.webdriver.Chrome()
        self.driver.implicitly_wait(3) #隐式等待，存在整个生命周期

    def teardown(self):
        self.driver.quit()

    def test_hordgwarz(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1050,708)
        # sleep(2)  直接等待，python自带与selenium无关
        self.driver.find_element(By.XPATH,'//*[@title="有了新帖的活动主题"]').click()
        # sleep(2)

        # def wait(x):
        #     return len(self.driver.find_element(By.XPATH,'//*[@id="ember312"]/thead/tr/th[1]'))>=1
        #
        # WebDriverWait(self.driver,10).until(wait) #隐式等待

        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]'))
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()



        # self.driver.find_element_by_link_text("霍格沃兹测试学院_霍格沃兹测试学院腾讯课堂官网")