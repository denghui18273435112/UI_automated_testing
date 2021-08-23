#-*- conding:utf-8 -*-
#@File      :department.py
#@Time      : 14:57
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.selenium import selenium
from tools.Base import Judgment_Reporting
import time
class department:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(Data["URL"])

    def add_department(self):
         self.driver.input_text("#depts\[\]:nth-child(1)",self.data["department"])
         self.driver.click("#submit")
         self.driver.screenShots("添加部门结构;截图-")
         time.sleep(5)

    def update_department(self):
         self.driver.click("#deptTree > li > div > a:nth-child(2) > i")
         self.driver.drop_down_box("#manager_chosen > a > span","#manager_chosen > div > ul > li")
         self.driver.click("#submit")
         time.sleep(5)