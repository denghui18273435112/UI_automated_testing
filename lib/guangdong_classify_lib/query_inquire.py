#-*- conding:utf-8 -*-
#@File      :query_inquire.py
#@Time      : 10:32
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from config.fixed_options import *
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium
import time
class query_inquire:
    def     __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        time.sleep(5)
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def query_inquire(self):
        """
        培训学分查询-操作
        :return:
        """
        try:
            self.driver.zzl_company_inquire("中国人寿保险股份有限公司广东省分公司")
            self.driver.zzl_pull_down_inquire(2,"仅限本机构")
            self.driver.zzl_pull_down_inquire(2,"本机构及下级")
            self.driver.zzl_pull_down_inquire(4,"A类：基础保险销售业务知识培训")
            self.driver.zzl_pull_down_inquire(3,"2020")
            self.driver.zzl_pull_down_inquire(3,"2021")
            self.driver.zzl_pull_down_inquire(7,"身份证")
            self.driver.zzl_pull_down_inquire(9,"线上")
            time.sleep(10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]
