# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/1910:14
# 开发工具: PyCharm
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By



class TestTouchAction():
     def setup(self):
         option=webdriver.ChromeOptions()
         option.add_experimental_option('w3c',False)
         self.driver=webdriver.Chrome(options=option)
         self.driver.implicitly_wait(5)
         self.driver.maximize_window()

     def teardown(self):
         self.driver.quit()

     def test_touchAction(self):
         self.driver.get("https://www.baidu.com")
         element1=self.driver.find_element(By.ID,"kw")
         element1.send_keys("selenium测试")
         element2=self.driver.find_element(By.ID,'su')
         action=TouchActions(self.driver)
         action.tap(element2)
         action.scroll_from_element(element1,0,10000)
         action.perform()

