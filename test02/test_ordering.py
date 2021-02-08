# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/515:01
# 开发工具: PyCharm

import pytest

@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True
