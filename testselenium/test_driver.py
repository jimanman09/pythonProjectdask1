# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/910:56
# 开发工具: PyCharm
import selenium
from selenium import webdriver

def test_driver():
    driver= webdriver.Chrome()
    driver.get("https://www.baidu.com")

