#-*- conding:utf-8 -*-
#@File      :user.py
#@Time      : 15:03
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.selenium import selenium
import time
from tools.Yaml_read import Yaml_read
from tools.Allure import *
from config.Conf import *
from tools.MysqlUitl import *
from tools.Base import  Judgment_Reporting

class user:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(Data["URL"])

    def user_add(self):
        self.driver.click("#mainMenu > div.btn-toolbar.pull-right > a.btn.btn-primary")
        self.driver.pullDown_frame("#dept_chosen > a > div:nth-child(2)",self.data["parts_thereof"])
        self.driver.input_text("account", self.data["account"] + "{}".format(self.driver.time_current_YmdHMS()))
        self.driver.input_text("#password1", self.data["password1"])
        self.driver.input_text("#password2", self.data["password2"])
        self.data["realname"] = self.data["realname"]+ "{}".format(self.driver.time_current_YmdHMS())
        self.driver.input_text("realname", self.data["realname"])
        self.driver.text_input("#join",self.driver.time_current_Ymd(),Enter=True,empty=True)
        self.driver.pullDown_frame("#role","//*[@id='role']/*[text()='{}']".format(self.data["position"]),joint=False)
        self.driver.pullDown_frame("#group_chosen > a > div:nth-child(3)",self.data["jurisdiction"],matching_mode=False)

        self.driver.input_text("email", self.data["email"])
        self.driver.input_text("commiter", self.data["commiter"])
        if self.data["sex"] == "男":
            self.driver.click("genderm")
        else:
            self.driver.click("genderf")
        self.driver.input_text("verifyPassword", self.data["verifyPassword"])
        self.driver.screenShots("添加用户信息;截图-")
        self.driver.click("submit")
        Judgment_Reporting(self.Data,"select * from  zt_user ","realname",self.data["realname"])


    def user_dupdate(self):
        self.driver.click("#userList > tbody > tr:nth-child(2) > td.c-actions > a:nth-child(2)")
        self.data["realname"] = self.data["realname"]+ "{}".format(self.driver.time_current_YmdHMS())
        self.driver.input_text("#realname",  self.data["realname"])
        self.driver.input_text("#password1",self.data["password1_2"])
        self.driver.input_text("#password2",self.data["password1_2"])
        self.driver.Page_scrolling(1000)
        self.driver.input_text("verifyPassword",self.data["verifyPassword"])
        self.driver.screenShots("修改用户信息;截图-")
        self.driver.click("#submit")
        Judgment_Reporting(self.Data,"select * from  zt_user ","realname", self.data["realname"])

    def user_delete(self):
        self.data["delete_data"] = self.driver.text_data("#userList > tbody > tr:nth-child(2) > td:nth-child(3)")
        self.driver.click("#userList > tbody > tr:nth-child(2) > td.c-actions > a.btn.iframe")
        self.driver.nested_page("iframe-triggerModal")
        self.driver.input_text("verifyPassword",self.data["verifyPassword"])
        self.driver.screenShots("删除用户信息;截图-")
        self.driver.click("submit")
        Judgment_Reporting(self.Data,"select * from  zt_user ","account",self.data["delete_data"],"假删除")






