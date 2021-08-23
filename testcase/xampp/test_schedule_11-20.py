import  pytest

from lib.xampp_lib.schedule import schedule
from tools.Yaml_read import Yaml_read


class Test_schedule(object):

    @pytest.mark.run(order=11)
    def test_add_schedule(self, driver):
        schedule(driver,Yaml_read("test_schedule.yaml","test_add_schedule")).add_schedule()

    @pytest.mark.run(order=12)
    def test_update_schedule(self, driver):
        schedule(driver,Yaml_read("test_schedule.yaml","test_update_schedule")).update_schedule()

    @pytest.mark.run(order=13)
    def test_del_schedule(self, driver):
        schedule(driver,Yaml_read("test_schedule.yaml","test_delete_schedule")).del_schedule()




