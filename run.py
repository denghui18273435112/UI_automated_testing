import pytest
import  os
from tools.Base import *

if __name__ == "__main__":
    #测试使用
    #pytest.main(["-s","./testcase/guangdong_classify/test_home.py","--alluredir", result_path()])

    #正式使用
    pytest.main(["-s","./testcase/guangdong_classify/","--alluredir", result_path()])

    os.system("allure generate {0} -o {1} --clean".format(result_path(), report_path()))
    os.system("allure serve {}".format(result_path()))