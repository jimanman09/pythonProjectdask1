# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/513:46
# 开发工具: PyCharm

#pytest --reruns 5 失败重跑5次
#pytest --reruns 5 --reruns-delay 1 失败间隔1秒重跑一次，重跑5次
import pytest

@pytest.mark.flaky(reruns=5,reruns_delay=2) #方法2，同命令执行重跑。更灵活，可以重跑某个方法
def test_reruns():
    assert 2== 1