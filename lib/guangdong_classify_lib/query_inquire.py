#-*- conding:utf-8 -*-
#@File      :query_inquire.py
#@Time      : 10:32
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import time
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium

class query_inquire:
    def     __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        time.sleep(5)
        self.driver.screenShots()
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def query_inquire(self):
        """
        培训学分查询-操作
        :return:
        """
        try:
            self.driver.zzl_company_inquire(self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(1) span"))
            self.driver.zzl_pull_down_inquire(2,"仅限本机构")
            self.driver.zzl_pull_down_inquire(2,"本机构及下级")
            self.driver.zzl_pull_down_inquire(4,"A类：基础保险销售业务知识培训")
            self.driver.zzl_pull_down_inquire(3,"2020")
            self.driver.zzl_pull_down_inquire(3,"2021")
            self.driver.zzl_pull_down_inquire(7,"身份证")
            self.driver.zzl_pull_down_inquire(9,"线上")
            self.driver.zzl_pull_down_inquire(10,"其他第三方")
            self.driver.zzl_text_input("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]",
                                       self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(2) span"),type="css")
            self.driver.zzl_text_input("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]",
                                       self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(4) span"),type="css")
            self.driver.zzl_click("查询",type="xpath_starts-with")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]
