# _*_ coding utf-8 _*_
# 开发人员: PC
# 开发时间: 2021/2/714:26
# 开发工具: PyCharm
# replace with your username:
from setuptools import setup
setup(
    name='test_hook01',
    url='https://github.com/xxx/test_hook1',
    version='1.0',
    author="nana",
    author_email='418974188@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['test_hook01'],
    keywords=[
        'pytest', 'py.test', 'test_hook01',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'test_hook1 = test_hook01',
        ]
    },
    zip_safe=False
)