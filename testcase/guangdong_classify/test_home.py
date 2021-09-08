import pytest

from lib.guangdong_classify_lib.home import home
from tools.Yaml_read import Yaml_read


class Test_home(object):
    #@pytest.mark.skip
    @pytest.mark.run(order=1)
    def test_overview_digital(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","overview_digital")).overview_digital()
        assert True ==assert_result
    #@pytest.mark.skip
    @pytest.mark.run(order=2)
    def test_charts(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","charts")).charts()
        assert True ==assert_result
    #@pytest.mark.skip
    @pytest.mark.run(order=3)
    def test_kinds_standards(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","kinds_standards")).kinds_standards()
        assert True ==assert_result
    #@pytest.mark.skip
    @pytest.mark.run(order=4)
    def test_student_details(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","student_details")).student_details()
        assert True ==assert_result
    #@pytest.mark.skip
    @pytest.mark.run(order=5)
    def test_company_data(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","company_data")).company_data()
        assert True ==assert_result
    #@pytest.mark.skip
    @pytest.mark.run(order=6)
    def test_tabulate_data(self,driver):
        assert_result = home(driver,Yaml_read("all.yaml","tabulate_data")).tabulate_data()
        assert True ==assert_result





