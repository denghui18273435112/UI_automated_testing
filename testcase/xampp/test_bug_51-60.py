import pytest

from lib.xampp_lib.bug import bug
from tools.Yaml_read import Yaml_read


class Test_bug(object):

    @pytest.mark.run(order=51)
    def test_add_bug(self,driver):
        bug(driver,Yaml_read("test_bug.yaml","test_add_bug")).add_bug()

    @pytest.mark.run(order=52)
    def test_update_bug(self,driver):
        bug(driver,Yaml_read("test_bug.yaml","test_update_bug")).update_bug()

    @pytest.mark.run(order=53)
    def test_delete_bug(self,driver):
        bug(driver,Yaml_read("test_bug.yaml","test_delete_bug")).delete_bug()




