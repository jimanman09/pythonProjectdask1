# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/315:31
# 开发工具: PyCharm
from datetime import *
import time
import pytest

@pytest.fixture(scope='module')
def login():
    print('开始测试：')
    day=date.today()
    yield day

    print("结束")


# @pytest.mark.usefixtures("get_username")
def test_search(login):
    print('今天是-')
    print(login)



def test_cart(login):
    print('添加到购物车')