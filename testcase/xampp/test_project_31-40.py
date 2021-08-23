#-*- conding:utf-8 -*-
#@File      :test_project_31-40.py
#@Time      : 17:39
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest

from lib.xampp_lib.project import project
from tools.Yaml_read import Yaml_read


class Test_project(object):

    @pytest.mark.run(order =31)
    def test_add_project(self,driver):
        project(driver,Yaml_read("test_project.yaml","test_add_project")).add_project()
