import allure
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
        # print("dataf",dataf)
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

@pytest.fixture()
def get_instance():
    print("开始计算：")
    calc = Calculator()
    yield calc
    print("结束计算！")

@pytest.fixture(params=get_datas()[0],ids=get_datas()[1])
def get_data_with_fixture(request):
    yield request.param
    # return data_f

# def test_get_data_fixture(get_data_with_fixture):
#     print("fixture_data:",get_data_with_fixture)

@pytest.fixture(params=get_datas()[2],ids=get_datas()[3])
def get_dataf_with_fixture(request):
    yield request.param
    # return data_f

@pytest.fixture(params=get_datas()[4],ids=get_datas()[5])
def get_datad_with_fixture(request):
    yield request.param
    # return data_f

@allure.feature("计算器")
class TestCalculator:

    # #前置条件
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc=Calculator()
    #
    # def teardown_class(self):
    #     print("结束计算")

    # data1: list = get_datas()

    # @pytest.mark.search
    #参数化
    # @pytest.mark.parametrize("a,b,result",data1[0],ids=data1[1])
    def test_add_int(self,get_instance,get_data_with_fixture):
        r:list = get_data_with_fixture
        # print("get_data_with_fixture",get_data_with_fixture)
        print(f"a={r[0]},b={r[1]},result={r[2]}")
        assert r[2] ==get_instance.add(r[0],r[1])
        # assert result == self.calc.add(a,b)
    @allure.title("相加_{get_dataf_with_fixture[0]_{get_dataf_with_fixture[1]}") #测试数据展示
    @allure.story("小数相加功能")
    def test_add_float(self,get_instance,get_dataf_with_fixture):
        rf = get_dataf_with_fixture
        print(f"a={rf[0]},b={rf[1]},result={rf[2]}")
        assert rf[2] == get_instance.add(rf[0], rf[1])

    #for循环

    # def test_add1(self):
    #     datas = [[1, 1, 2], [100, 200,300], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])
    #todo:
    #@pytest.mark.login
    # @pytest.mark.parametrize("a,b,result",data1[6],ids=data1[7])
    def test_div(self,get_instance,get_datad_with_fixture):
        with pytest.raises(ZeroDivisionError):
            rd = get_datad_with_fixture
            print(f"a={rd[0]},b={rd[1]},result={rd[2]}")
            assert rd[2] == get_instance.div(rd[0], rd[1])







