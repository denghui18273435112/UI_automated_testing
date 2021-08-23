#-*- conding:utf-8 -*-
#@File      :test_task_51-60.py
#@Time      : 11:47
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest

from lib.xampp_lib.task import  task
from tools.Yaml_read import Yaml_read


class Test_task(object):

    @pytest.mark.run(order = 51)
    def test_task_add(self,driver):
        task(driver,Yaml_read("test_task.yaml","test_task_add")).add_task()