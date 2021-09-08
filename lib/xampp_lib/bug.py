#-*- conding:utf-8 -*-
#@File      :bug.py
#@Time      : 13:30
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import  time

from tools.Base import *
from tools.selenium import selenium


class bug:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        id = Verify_database_data("select * from zt_product","deleted","0")["id"]
        self.driver.url_skip(str(Data["URL"])+str(id)+".html")

    def add_bug(self):
        self.driver.click("提Bug")
        self.driver.pullDown_frame("#product_chosen > a > div:nth-child(2)",self.data["product"])
        self.driver.pullDown_frame("#module_chosen > a > div:nth-child(2)",self.data["module"])
        #self.driver.pullDown_frame("#project_chosen > a > div:nth-child(2)",self.data["project"])
        #self.driver.text_input("#openedBuild_chosen","主干",Enter=True)
        self.driver.drop_down_box("#openedBuild_chosen > ul > li > input","#openedBuild_chosen > div > ul > li", 0)
        # self.driver.click("加载所有用户")
        # self.driver.pullDown_frame("#assignedTo_chosen > a > div:nth-child(2)","admin")
        self.driver.input_text("deadline",self.driver.time_current_Ymd())
        self.driver.drop_down_box("#type_chosen > a > div:nth-child(3)","//*[@id=\"type_chosen\"]/div/ul/li[1]")
        self.driver.drop_down_box("#os_chosen > a > div:nth-child(2)","//*[@id=\"os_chosen\"]/div/ul/li[2]")
        self.driver.drop_down_box("#browser_chosen > a > div:nth-child(2)","//*[@id=\"browser_chosen\"]/div/ul/li[2]")
        self.data["bug_title"] = self.data["bug_title"]+self.driver.time_current_YmdHMS()
        self.driver.input_text("#title", self.data["bug_title"])
        self.driver.upload_inputType("#dataform > table > tbody > tr:nth-child(10) > td > div > div > input[type='file']")
        self.driver.screenShots()
        self.driver.click("submit")
        time.sleep(1)
        Judgment_Reporting(self.Data,"select * from  zt_bug","title",self.data["bug_title"])

    def  update_bug(self):
        self.driver.click("#bugList > tbody > tr:nth-child(1) > td.c-actions > a:nth-child(4) > i")
        self.data["bug_title"] = self.data["bug_title"]+self.driver.time_current_YmdHMS()
        self.driver.input_text("#title", self.data["bug_title"])
        self.driver.screenShots()
        self.driver.click("submit")
        time.sleep(1)
        self.driver.screenShots()
        Judgment_Reporting(self.Data,"select * from  zt_bug","title",self.data["bug_title"])

    def delete_bug(self):
        self.data["delete_data"] = self.driver.text_data("#bugList > tbody > tr:nth-child(1) > td.c-title.text-left > a")
        self.driver.click("#bugList > tbody > tr:nth-child(1) > td.c-title.text-left > a")
        self.driver.click("#mainContent > div.main-col.col-8 > div.main-actions > div > a:nth-child(11) >i")
        self.driver.browser_pop_up()
        time.sleep(1)
        self.driver.screenShots()
        Judgment_Reporting(Data=self.Data,sql="select * from  zt_bug",field_names="title",delete_data=self.data["delete_data"],delete_type="假删除")





