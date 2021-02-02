# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/213:41
# 开发工具: PyCharm
import yaml


def test_yamlData():
    with open("../testDatas/yamlData.yml",encoding='utf-8') as f:
        datas=yaml.safe_load(f)
        print(datas)





