##项目一 ：第一次课堂作业

##TOKEN:
-  5c78b79857af526a21fd85e56386a68cc0dcb5b8

##课堂笔记
- 课程贴地址：https://ceshiren.com/t/topic/9879 9936
- git  http://ceshiren.com/t/topic/7405
- 参考链接
- allure 下载地址https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.5/  
 - 命名规范： https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id16
## windows 上读取yml文件要加encoding='utf-8'
 def test_yamlData():
    with open("../testDatas/yamlData.yml",encoding='utf-8') as f:
        datas=yaml.safe_load(f)
        print(datas)
  
- ids 给结果重命名 ids=['','',''']
## 运行文件不在同一个文件夹下：
  sys.path.append('..')
  print(sys.path)
  
- yaml yaml.safe_load(open("../testDatas/yamlData.yml", encoding='utf-8'))
  或者 with open("../testDatas/yamlData.yml", encoding='utf-8') as f:
       dataf=yaml.safe_load(f)
  windows 需要加encoding='utf-8'
  
- round(a,2) 数值a如果是小数，取小数后2位
- with pytest.raises(ZeroDivisionError):
  相当于 try: 
        except
  
## pytest_fixture() 的2钟用法,@pytest.fixture()
def login(): 
  - def search(login):
  - @pytest.mark.usefixtures("login") 
    def search()
  - 多个fixture，由内向外执行
  - fixture可以调用另一个fixture
  - yield 相当于return 在执行用例完成后返回yield信息  
  - conftest 文件名固定，首先被加载，主要存放fixtrue hook函数，就近生效;创建在包中 有__init__文件  
## fixtrue 参数使用：
  - @pytest.fixture(params=["marry","shoes"])
def login(request):
    print("登录成功")
    yield request.param

def test_search(login):
    print("输入 网址 关键字")
    print(login)

## pytest.assume
- assume 可以执行全部的断言，无论正确与否，assert 按顺序执行，断言错误即中断

## pytest-rerunfailures
- pytest --reruns 5 失败重跑5次
- pytest --reruns 5 --reruns-delay 1 失败间隔1秒重跑一次，重跑5次
- @pytest.mark.flaky(reruns=5,reruns_delay=2) 方法2，同命令执行重跑。更灵活，可以重跑某个方法

- --setup-show 查看执行过程  e.g pytest test_a.py --setup-show

## pytest-dependency
- @pytest.mark.dependency(depends=["test_b", "test_c"])

##代码---本地git仓库---远程git仓库
- 安装git bash
- 创建自己git账号 
- git init
- commit  上传到本地git仓库
- github网站https://github.com/new创建代码仓库
  https://github.com/jimanman09/pythonProjectDask01，https://github.com/jimanman09/pythonProjectDask01.git
- 关联本地和远程仓库
- push 本地上传到远程
  

- gitee

## hook函数构造打包
- 参考地址：https://packaging.python.org/tutorials/packaging-projects/
- 打包需要先安装 setuptools，
pip install wheel
- 打包命令：python setup.py sdist bdist_wheel    
- 安装 pip install 安装包名
- 卸载 pip uninstall test_hook01

## allure安装及使用
- 下载包，解压执行bin下的bat文件
- 配置path环境变量：把bin路径添加到path
- 安装allure-pytest
- 生成报告命令
pytest test.py --allure-features="aa" -vs --alluredir=./result1
allure serve ./result1
-  jdk也要安装，并且配置java环境变量 

##作业地址：
- https://github.com/jimanman09/pythonProjectdask1/ 




