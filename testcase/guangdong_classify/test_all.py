#-*- conding:utf-8 -*-
#@File      :test_credit_inquiry.py
#@Time      : 18:21
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.all import all
from tools.Yaml_read import Yaml_read

def setup_module():
    print("\n全局前")
def teardown_module():
    print("全局后")

class Test_all(object):
    """
    账号管理模块
    """
    def setup_class(self):
        print("Test_foodManagement类中运行的前置")
    def teardown_class(self):
        print("Test_foodManagement类中运行的后置")
    def setup_method(self):
        print("Test_foodManagement方法中运行的前置")
    def teardown_method(self):
        print("Test_foodManagement方法中运行的后置")

    #@pytest.mark.skip
    @pytest.mark.priority_middle
    @pytest.mark.run(order=8)
    def test_query_inquire(self,driver):
        """
        培训记录统计模块-查询、按钮操作
        :param driver:
        :return:
        """
        assert_result = all(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True ==assert_result

    @pytest.mark.priority_tall
    @pytest.mark.test
    @pytest.mark.run(order=25)
    def test_account_management_inquire(self,driver):
        """
        账号管理模块-查询操作
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_inquire")).account_management_inquire()
        assert True ==assert_result

