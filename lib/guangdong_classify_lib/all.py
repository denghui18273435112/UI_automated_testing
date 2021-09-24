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

class all:
    """
    所有
    """
    def     __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.resfresh()
        self.driver.screenShots()
        time.sleep(5)
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def record_statistical_query_inquire(self):
        """
         培训记录统计模块-查询-操作
        :return:
        """
        try:
            self.driver.zzl_company_inquire("中国人民财产保险股份有限公司广东省分公司")
            self.driver.zzl_pull_down_inquire(2,"2020")
            self.driver.zzl_pull_down_inquire(4,"线下")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_pull_down_inquire(4,"线上")
            self.driver.zzl_pull_down_inquire(5,"本机构")
            self.driver.zzl_pull_down_inquire(7,"已达标")
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

    def account_management_inquire(self):
        """
        账号管理-字段查询、按钮操作
        :return:
        """
        try:
            #操作
            self.driver.zzl_pull_down_inquire(2,type[0])
            self.driver.zzl_pull_down_inquire(3,status[0])
            self.driver.zzl_pull_down_inquire(4,login_status[1])
            #self.driver.zzl_company_inquire(gongsi)
            name = self.driver.text_acquire(column=2)
            self.driver.zzl_text_input("input[placeholder=\"请输入昵称\"]",name,type="css")

            #查询后列表数据判断
            judge_data = [name,login_status[1],status[0]]
            list_position = [2,6,9]
            list_number = int(self.driver.text_acquire(location=" span.el-pagination__total").split(" ")[1])
            if list_number > 10:
                list_number = 10
            for x in range(list_number):
                text_data = []
                for y in list_position:
                    text_data.append(self.driver.text_acquire(row=x+1,column=y))
                if judge_data != text_data:
                    self.Data["actual_result"] = False

            # gongsi = self.driver.text_acquire(column=8)
            # self.driver.zzl_click("查询",type="xpath_starts-with")
            # self.driver.zzl_click("重置",type="xpath_starts-with")
            # self.driver.zzl_click("导出",type="xpath_starts-with")
            # self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
            # self.driver.zzl_click("div.table-area div.export>span:nth-child(3)",type="css")
            # self.driver.zzl_text_input("请输入用户名","denghui00001",type="css_text")
            # self.driver.zzl_text_input("请输入用户昵称","denghui00001",type="css_text")
            # self.driver.zzl_text_input("请输入手机号","18273435112",type="css_text")
            # self.driver.zzl_text_input("请输入新密码","denghui921206",type="css_text")
            # self.driver.zzl_text_input("再次输入密码","denghui921206",type="css_text")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]
