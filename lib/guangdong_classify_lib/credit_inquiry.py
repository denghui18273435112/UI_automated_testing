#-*- conding:utf-8 -*-
#@File      :credit_inquiry.py
#@Time      : 18:23
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from config.fixed_options import *
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium
import time

class credit_inquiry:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def inquire(self):
        """
        培训学分查询
        :return:
        """
        try:
            self.driver.FEBCS_CCSKK("input[placeholder=\"请选择所属机构\"]","中国人寿保险股份有限公司广东省分公司")
            self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)")
            for index in range(len(check_range)):
                self.driver.pull_down_choose("div div:nth-child(2)>div.el-select>div>span",
                                             "//ul/li/*[contains(text(),\"{}\")]".format(check_range[index]),type="CSS_XPATH")
            for index in range(len(year)):
                self.driver.pull_down_choose("div div:nth-child(3)>div.el-select>div>span",
                                             "//ul/li/*[contains(text(),\"{}\")]".format(year[index]),type="CSS_XPATH")
            for index in range(len(course_name)):
                self.driver.pull_down_choose("div div:nth-child(4) > div.el-select > div > span",
                                             "//ul/li/*[contains(text(),\"{}\")]".format(course_name[index]),type="CSS_XPATH")
            for index in range(len(reach_status)):
                self.driver.drop_down_box("div div:nth-child(5) > div.el-select > div > span ",
                                          "//li/span[contains(text(),\"{}\")]".format(reach_status[index]))
            for index in range(len(certificate_type)):
                self.driver.drop_down_box("div div:nth-child(7) > div.el-select > div > span",
                                          "//li/span[contains(text(),\"{}\")]".format(certificate_type[index]))
            for index in range(len(training_method)):
                self.driver.pull_down_choose("div div:nth-child(9) > div.el-select > div > span",
                                          "//li/span[contains(text(),\"{}\")]".format(training_method[index]),type="CSS_XPATH")
            # for index in range(len(units)):
            #     self.driver.pull_down_choose("div div:nth-child(10)>div.el-select>div>span",
            #                               "body>div>div>div.el-select-dropdown__wrap.el-scrollbar__wrap>ul>li:nth-child({})".format(index+1))
            self.driver.FEBCS_CCSKK("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]","张金玲",ifhuiche=True)
            self.driver.FEBCS_CCSKK("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]","431281198107266025",ifhuiche=True)

        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]