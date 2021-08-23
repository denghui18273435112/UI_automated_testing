#-*- conding:utf-8 -*-
#@File      :schedule.py
#@Time      : 16:04
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.selenium import selenium
from tools.Allure import *
from tools.Base import  Judgment_Reporting

class schedule:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(Data["URL"])

    def add_schedule(self):
        self.driver.click("create")
        self.driver.nested_page("iframe-triggerModal")
        #self.driver.input_text("data",data["date"])
        self.driver.drop_down_box("type","//*[@id='type']/*[text()='{}']".format(self.data["type"]))
        self.driver.drop_down_box("pri","//*[@id='pri']/*[text()='{}']".format(self.data["priority"]))
        self.data["describe"] = self.data["describe"]+self.driver.time_current_YmdHMS()
        self.driver.input_text("#dataform > table > tbody > tr:nth-child(6) > td > div.nameBox.required >input.form-control",self.data["describe"])
        self.driver.drop_down_box("#status_chosen > a > div:nth-child(2)","//*[@id=\"status_chosen\"]//*[text()=\"{}\"]".format(self.data["state"]))
        # self.driver.input_text("begin_chosen",data["start_date"])
        # self.driver.input_text("end_chosen",data["end_daye"])
        if self.data["private_affair"] ==True:
            self.driver.click("private")
        self.driver.screenShots("添加日程信息;截图-")
        self.driver.click("保存")
        time.sleep(2)
        Judgment_Reporting(self.Data,"select * from  zt_todo ","name",self.data["describe"])

    def update_schedule(self):
        schedule_data = self.driver.text_data("#todoList > tbody > tr:nth-child(1) > td.c-name > a")
        self.driver.click("#todoList > tbody > tr:nth-child(1) > td.c-actions > a:nth-child(4)")
        self.driver.nested_page("iframe-triggerModal")
        self.driver.screenShots("添加日程信息;截图-")
        self.driver.click("保存")
        time.sleep(2)
        Judgment_Reporting(self.Data,"select * from  zt_todo ","name",schedule_data)

    def del_schedule(self):
        self.data["delete_data"] = self.driver.text_data("#todoList > tbody > tr:nth-child(1) > td.c-name > a")
        self.driver.click("#todoList > tbody > tr:nth-child(1) > td.c-actions > a:nth-child(5) > i")
        self.driver.browser_pop_up()
        self.driver.screenShots("添加日程信息;截图-")
        time.sleep(2)
        Judgment_Reporting(self.Data,"select * from  zt_todo ","name",self.data["delete_data"],"真删除")




