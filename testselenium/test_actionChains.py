# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/1816:00
# 开发工具: PyCharm
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class TestActionChains():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element1=self.driver.find_element_by_xpath("//input[@value='click me']")
        element2 = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element3 = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action=ActionChains(self.driver)
        action.click(element1)
        action.context_click(element3)
        action.double_click(element2)
        action.perform()
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        element=self.driver.find_element(By.CSS_SELECTOR,'#u1 span')
        # ele=self.driver.find_element_by_link_text("设置")
        action=ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @pytest.mark.skip
    def test_dragDrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag=self.driver.find_element(By.CSS_SELECTOR,'#dragger')
        ele_drop=self.driver.find_element_by_xpath("/html/body/div[2]")
        sleep(5)
        action=ActionChains(self.driver)
        sleep(5)
        # 3钟实现方法：
        # action.drag_and_drop(ele_drag,ele_drop).perform()
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        action.click_and_hold(ele_drag).move_to_element(ele_drop)

    def test_keyboard(self):
        self.driver.get("https://email.163.com/")
        WebDriverWait(self.driver,100).until(expected_conditions.element_to_be_clickable((By.NAME,'email')))
        ele_input=self.driver.find_element(By.CSS_SELECTOR,'[name=email]')
        ele_input.click()
        action=ActionChains(self.driver)

        action.send_keys("jinagirl09").pause(2)
        action.send_keys(keys.SPACE).pause(2)
        action.send_keys("@163.com").pause(2)
        action.send_keys(keys.Backspace).pause(2)
        action.perform()

