#-*- conding:utf-8 -*-
#@File      :project.py
#@Time      : 17:40
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.Base import *
from tools.selenium import selenium


class project:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.project_name = ""

    def add_project(self):
        self.driver.url_skip(self.Data["URL"])
        self.driver.click("#pageActions > div > a")
        self.data["project_name"] = self.data["project_name"]+time_YmdHMS()
        self.project_name = self.data["project_name"]
        self.data["project_code"] = self.data["project_code"]+time_YmdHMS()
        self.driver.input_text("#name",self.data["project_name"])
        self.driver.input_text("#code",self.data["project_code"])
        self.driver.click(" tr:nth-child(3) > td:nth-child(3) > label:nth-child(2)")
        self.driver.input_text("#team",self.data["team"])
        self.driver.click_two("#products0_chosen > a > div:nth-child(2)","//*[@id='products0_chosen']/div/ul/li[contains(text(),'{}')]".format(self.data["product"]))
        self.driver.Page_scrolling()
        self.driver.click("#submit")
        #self.driver.click("#tipsModal > div.modal-header > a > i")
        self.driver.screenShots()
        Judgment_Reporting(self.Data,"select * from zt_project","name",self.data["project_name"])




