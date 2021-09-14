#-*- conding:utf-8 -*-
#@File      :credit_inquiry.py
#@Time      : 18:23
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import time
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium
from config.fixed_options import *
class credit_inquiry:
    def     __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        self.driver.screenShots()
        time.sleep(5)
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def inquire(self):
        """
        培训学分查询
        :return:
        """
        try:
            self.driver.FEBCS_CCSKK("input[placeholder=\"请选择所属机构\"]",self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(1) span"))
            self.driver.zzl_click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)","css")
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
            self.driver.click("重置",type="starts-with")
            time.sleep(5)
            self.driver.FEBCS_CCSKK("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]",
                                    self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(2) span"),ifhuiche=True)
            self.driver.FEBCS_CCSKK("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]",
                                    self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(4) span"),ifhuiche=True)

        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def operation(self):
        """
        培训学分查询-操作
        :return:
        """
        try:
            self.driver.click("查询",type="starts-with")
            time.sleep(10)
            self.driver.click("重置",type="starts-with")
            time.sleep(10)
            self.driver.click("导出",type="starts-with")
            time.sleep(10)
            #self.driver.input_text("//*/span[starts-with(.,\"前往\")]//input",10,type="xpath",Enter=0)
            self.driver.text_input("//*/span[starts-with(.,\"前往\")]//input",10)
            time.sleep(10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

