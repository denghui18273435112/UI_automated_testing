#-*- conding:utf-8 -*-
#@File      :test_query_inquire.py
#@Time      : 10:30
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.query_inquire import query_inquire
from tools.Yaml_read import Yaml_read


class Test_query_inquire(object):
    """
    培训记录查询模块
    """
    #@pytest.mark.skip
    @pytest.mark.run(order=8)
    def test_query_inquire(self,driver):
        """
        培训记录查询相关操作
        :param driver:
        :return:
        """
        assert_result = query_inquire(driver,Yaml_read("all.yaml","query_inquire")).query_inquire()
        assert True ==assert_result

