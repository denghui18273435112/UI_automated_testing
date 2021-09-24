#-*- conding:utf-8 -*-
#@File      :test_credit_inquiry.py
#@Time      : 18:21
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.all import all
from tools.Yaml_read import Yaml_read

class Test_all(object):
    @pytest.mark.priority_middle
    @pytest.mark.run(order=11)
    def test_query_inquire(self,driver):
        """
        培训记录统计
        :param driver:
        :return:
        """
        assert_result =all(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True ==assert_result

    @pytest.mark.priority_tall
    @pytest.mark.test
    @pytest.mark.run(order=12)
    def test_account_management_inquire(self,driver):
        """
        账号管理-查询操作
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_inquire")).account_management_inquire()
        assert True == assert_result

