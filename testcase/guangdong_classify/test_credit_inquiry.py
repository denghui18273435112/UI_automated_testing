#-*- conding:utf-8 -*-
#@File      :test_credit_inquiry.py
#@Time      : 18:21
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.credit_inquiry import credit_inquiry
from tools.Yaml_read import Yaml_read
class Test_credit_inquiry(object):
    #@pytest.mark.skip
    @pytest.mark.run(order=8)
    def test_inquire(self,driver):
        assert_result = credit_inquiry(driver,Yaml_read("all.yaml","inquire")).inquire()
        assert True ==assert_result