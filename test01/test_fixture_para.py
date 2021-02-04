# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/415:19
# 开发工具: PyCharm
import pytest


@pytest.fixture(params=["marry","shoes"])
def login(request):
    print("登录成功")
    yield request.param

def test_search(login):
    print("输入 网址 关键字")
    print(login)


