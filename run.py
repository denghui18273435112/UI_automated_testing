import pytest
from tools.Base import *
import os
if __name__ == "__main__":
    #测试使用
    #pytest.main(["-s","./testcase/guangdong_classify/test_query_inquire.py","--alluredir", result_path()])

    #正式使用
    pytest.main(["-s","./testcase/guangdong_classify/",
                  # '-m','test or test',
                 "--alluredir", result_path()])
    # os.system("allure generate {0} -o {1} --clean".format(result_path(), report_path()))
    # os.system("allure serve {}".format(result_path()))
    #    @pytest.mark.test