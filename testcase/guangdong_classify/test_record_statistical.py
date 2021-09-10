#-*- conding:utf-8 -*-
#@File      :test_record_statistical.py
#@Time      : 13:54
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.record_statistical import record_statistical
from tools.Yaml_read import Yaml_read
class Test_record_statistical(object):
    """
    培训记录统计模块
    """
    #@pytest.mark.skip
    @pytest.mark.priority_middle
    @pytest.mark.test
    @pytest.mark.run(order=8)
    def test_query_inquire(self,driver):
        """
        培训记录统计模块-查询、按钮操作
        :param driver:
        :return:
        """
        assert_result = record_statistical(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True ==assert_result

