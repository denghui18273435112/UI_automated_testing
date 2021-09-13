import pytest
from tools.Base import *
import os
if __name__ == "__main__":
    #测试使用
    #pytest.main(["-s","./testcase/guangdong_classify/test_query_inquire.py","--alluredir", result_path()])

    #正式使用
    pytest.main(["-s","./testcase/guangdong_classify/",
                  '-m','test or test',
                 "--alluredir", result_path()])
