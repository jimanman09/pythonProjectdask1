# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/817:03
# 开发工具: PyCharm
import allure


def test_attach_text():
    allure.attach("这事一个文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这事一个htmlbody</body>","测试body",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("文件路径",name="",attachment_type=allure.attachment_type.JPG)