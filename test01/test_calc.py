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
        dataf = yaml.safe_load(f)
        print("dataf",dataf)
        data_int=dataf['add']['int']['datas']
        data_int_ids=dataf['add']['int']['ids']
        data_float = dataf['add']['float']['datas']
        data_float_ids = dataf['add']['float']['ids']
        data_div_nonzero = dataf['div']['nonzero']['datas']
        data_div_nonzero_ids = dataf['div']['nonzero']['ids']
        data_div_zero = dataf['div']['zero']['datas']
        data_div_zero_ids = dataf['div']['zero']['ids']
        return (data_int,data_int_ids,data_float,data_float_ids,
                data_div_nonzero,data_div_nonzero_ids,data_div_zero,data_div_zero_ids)


class TestCalculator:

    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc=Calculator()

    def teardown_class(self):
        print("结束计算")

    data1: list = get_datas()

    # @pytest.mark.search
    #参数化
    @pytest.mark.parametrize("a,b,result",data1[0],ids=data1[1])
    def test_add_int(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result ==self.calc.add(a,b)
        # assert result == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,result", data1[2], ids=data1[3])
    def test_add_float(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == round(self.calc.add(a, b),2)


    #for循环

    # def test_add1(self):
    #     datas = [[1, 1, 2], [100, 200,300], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])
    #todo:
    #@pytest.mark.login
    @pytest.mark.parametrize("a,b,result",data1[6],ids=data1[7])
    def test_div(self,a,b,result):
        with pytest.raises(ZeroDivisionError):
            print(f"a={a},b={b},result={result}")
            assert result== round(self.calc.div(a,b),2)








