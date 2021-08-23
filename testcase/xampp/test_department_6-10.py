#-*- conding:utf-8 -*-
#@File      :test_department_6-10.py
#@Time      : 14:56
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest

from lib.xampp_lib.department import department
from tools.Yaml_read import Yaml_read


class Test_department(object):

    @pytest.mark.run(order=6)
    def test_add_department(self,driver):
        department(driver,Yaml_read("department.yaml","test_department_add")).add_department()

    @pytest.mark.run(order=7)
    def test_update_department(self,driver):
        department(driver,Yaml_read("department.yaml","test_department_update")).update_department()



