#-*- conding:utf-8 -*-
#@File      :test_submission.py
#@Time      : 16:11
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest
from lib.guangdong_classify_lib.submission import submission
from tools.Yaml_read import Yaml_read
class Test_submission(object):
    #@pytest.mark.skip
    @pytest.mark.run(order=7)
    def test_submission(self,driver):
        """
        培训计划报送
        :param driver:
        :return:
        """
        assert_result = submission(driver,Yaml_read("all.yaml","submission_inquire")).submission_inquire()
        assert True ==assert_result