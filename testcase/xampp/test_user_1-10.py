import pytest

from lib.xampp_lib.user import user
from tools.Yaml_read import Yaml_read


class Test_user(object):

    @pytest.mark.run(order=1)
    def test_user_add(self,driver):
        user(driver,Yaml_read("test_user.yaml","test_user_add")).user_add()

    @pytest.mark.run(order=2)
    def test_user_update(self,driver):
        user(driver,Yaml_read("test_user.yaml","test_user_update")).user_dupdate()

    @pytest.mark.run(order=3)
    def test_user_delete(self,driver):
        user(driver,Yaml_read("test_user.yaml","test_user_delete")).user_delete()




