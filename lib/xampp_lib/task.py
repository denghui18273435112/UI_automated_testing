#-*- conding:utf-8 -*-
#@File      :task.py
#@Time      : 11:49
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.Base import *
from  tools.selenium import selenium


class task:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        id =Verify_database_data("select * from zt_project","deleted","0")["id"]
        self.driver.url_skip(str(Data["URL"])+str(id)+".html")

    def add_task(self):
        self.driver.click("#mainMenu > div.btn-toolbar.pull-right > a.btn.btn-primary > i")
        self.driver.pullDown_frame("#type_chosen > a > div:nth-child(2)",self.data["task_type"])
        self.data["task_name"] = self.data["task_name"]+time_YmdHMS()
        self.driver.input_text("#name",self.data["task_name"])
        self.driver.screenShots()
        self.driver.click("submit")
        Judgment_Reporting(self.Data,"select * from zt_task","name",self.data["task_name"])

