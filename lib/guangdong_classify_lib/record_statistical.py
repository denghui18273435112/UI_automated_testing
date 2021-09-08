#-*- conding:utf-8 -*-
#@File      :record_statistical.py
#@Time      : 13:56
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import time

from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium


class record_statistical:
    def     __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        time.sleep(5)
        self.driver.screenShots()
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def record_statistical_query_inquire(self):
        """
        查询-操作
        :return:
        """
        try:
            self.driver.zzl_company_inquire("中国人寿保险股份有限公司广东省分公司")
            self.driver.zzl_pull_down_inquire(2,"2020")
            self.driver.zzl_pull_down_inquire(2,"2021")
            self.driver.zzl_pull_down_inquire(4,"线下")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_pull_down_inquire(4,"线上")
            self.driver.zzl_pull_down_inquire(5,"本机构")
            self.driver.zzl_pull_down_inquire(6,"已达标")
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