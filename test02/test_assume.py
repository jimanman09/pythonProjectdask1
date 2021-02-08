# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/514:47
# 开发工具: PyCharm
import pytest
def test_assume():
    # assert 1==2
    # assert 2==2
    # assert 2==3
    pytest.assume(1==2) #assume 可以执行全部的断言，无论正确与否，assert 按顺序执行，断言错误即中断
    pytest.assume(2==2)
    pytest.assume(2==3)

