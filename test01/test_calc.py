import pytest
#计算器相加功能
import sys
#如果要使用命令行执行，因为calculatorcode.calculator 跟test_calc不在同一个文件夹，不能直接使用命令行。需要append上一个路径来执行
import yaml
from decimal import *

sys.path.append('..')
print(sys.path)

from calculatorcode.calculator import Calculator


def get_datas():
    with open("../testDatas/yamlData.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],datas['add']['ids'],datas['add']['datad'])


class TestCalculator:

    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc=Calculator()

    def teardown_class(self):
        print("结束计算")

    datas: list = get_datas()

    # @pytest.mark.search
    #参数化
    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_add(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result ==round(self.calc.add(a,b),2)
        # assert result == self.calc.add(a,b)
    #for循环

    # def test_add1(self):
    #     datas = [[1, 1, 2], [100, 200,300], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])
    #todo:
    #@pytest.mark.login
    @pytest.mark.parametrize("a,b,result",datas[2],ids=datas[1])
    def test_div(self,a,b,result):
        try:
            print(f"a={a},b={b},result={result}")
            assert result== round(self.calc.div(a,b),2)
        except ZeroDivisionError as e:
            print(e,"除数不能为0！")







