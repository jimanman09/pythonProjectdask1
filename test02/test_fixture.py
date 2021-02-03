# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/315:31
# 开发工具: PyCharm


import pytest


@pytest.fixture()
def login():
    print('登录成功：')
    yield
    print("登出")


@pytest.fixture()
def get_username(login):
    uname="测试认"
    print(uname)
    return uname


@pytest.mark.usefixtures("get_username")
def test_search():
    print('搜索百度')

def test_cart():
    print('添加到购物车')