import pytest

from lib.guangdong_classify_lib.home import home
from tools.Yaml_read import Yaml_read


class Test_home(object):
    @pytest.mark.run(order=1)
    def test_overview_digital(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","overview_digital")).overview_digital()
        assert True ==assert_result

    @pytest.mark.run(order=2)
    def test_charts(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","charts")).charts()
        assert True ==assert_result







