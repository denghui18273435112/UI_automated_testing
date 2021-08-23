#-*- conding:utf-8 -*-
#@File      :test_product_21-30.py
#@Time      : 10:05
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import pytest

from lib.xampp_lib.product import product
from tools.Yaml_read import Yaml_read


class Test_product(object):

    @pytest.mark.run(order =21)
    def test_add_product(self,driver):
        product(driver,Yaml_read("test_product.yaml","test_add_product")).add_product()
