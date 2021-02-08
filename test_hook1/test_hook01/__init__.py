# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/714:24
# 开发工具: PyCharm
from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    #如果yaml文件中ids有中文，不适用下面方法显示乱码。name指用例路径，nodeid指名字
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')

        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    # items.reverse() #倒序