# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/715:02
# 开发工具: PyCharm
import pytest


@pytest.mark.parametrize('name',['张三','李四'])
def test_hk(name):
    print(name)