import allure

from tools.Base import *
from tools.Yaml_read import Yaml_read


def alluer(inData):
        """
        :param inData 表格数据
        :return:
        """
        allure.dynamic.feature(inData["module"])
        allure.dynamic.story(inData["name"])
        #allure.dynamic.title(inData["标题"])
        allure.attach( "<font color='red' style='font-size: 20px;'>{}</font><Br/>".format(inData["data"]),"操作的数据",allure.attachment_type.HTML)
        desc = "<font color='red'>当前执行时间: </font> {}<Br/>" \
               "<font color='red'>用例编号（test_id）: </font> {}<Br/>" \
               "<font color='red'>模块（module）: </font>{}<Br/>" \
               "<font color='red'>标题_名称（name）: </font>{}<Br/>" \
               "<font color='red'>优先级（priority）: </font>{}<Br/>" \
               "<font color='red' >URL: </font>{}<Br/>"\
               "<font color='red' >前置条件（preposition）: </font>{}<Br/>"\
               "<font color='red' >预期结果（expected_result）: </font>{}<Br/>"\
               "<font color='red' >实际结果（actual_result）: </font>{}<Br/>"\
                "<font color='red' >操作详情（assert_fail_hint）: </font>{}<Br/>"\
                "<font color='red' >定位失败原因（location_fail_hint）: </font>{}<Br/>"\
               "<font color='red' >操作的数据（data）: </font>{}<Br/>"\
            .format(
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    inData["test_id"],
                    inData["module"],
                    inData["name"],
                    inData["priority"],
                    Yaml_read("all.yaml","login")["new_url"]+inData["URL"],
                    inData["preposition"],
                    inData["expected_result"],
                    inData["actual_result"],
                    inData["assert_fail_hint"],
                    inData["location_fail_hint"],
                    inData["data"])
        allure.dynamic.description(desc)