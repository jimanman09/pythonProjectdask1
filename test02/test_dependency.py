# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/515:31
# 开发工具: PyCharm

import pytest

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")

def test_a():

    assert False

@pytest.mark.dependency()

def test_b():

    pass


@pytest.mark.dependency(depends=["test_a"])

def test_c():

    # c 信赖 a，a失败了，c会跳过

    pass


@pytest.mark.dependency(depends=["test_b"])

def test_d():

    pass


@pytest.mark.dependency(depends=["test_b", "test_c"])

def test_e():

    # c跳过，e也跳过

    pass