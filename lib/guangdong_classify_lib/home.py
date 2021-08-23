#-*- conding:utf-8 -*-
#@File      :product.py
#@Time      : 10:06
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.Allure import alluer
from tools.selenium import selenium
import time
class home:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data

    def overview_digital(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'数字概览')]")
            CXJHZRS=self.driver.text("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS = int(CXJHZRS.split("/")[0])
            ZJHRS = int(CXJHZRS.split("/")[1])
            CL=int(self.driver.text("span:nth-child(2) > span.value"))
            ZL=int(self.driver.text("span:nth-child(3) > span.value"))
            YCX=int(self.driver.text("span:nth-child(4) > span.value"))
            WCX=int(self.driver.text("span:nth-child(5) > span.value"))
            ZDBZCX = self.driver.text("div:nth-child(2) > div > div.container  span:nth-child(1) > span.total")
            ZDB = int(ZDBZCX.split("/")[0])
            ZCX = int(ZDBZCX.split("/")[1])
            YDB=int(self.driver.text("div:nth-child(2)  div.container  span:nth-child(2) > span.value"))
            WDB=int(self.driver.text("div:nth-child(2)  div.container  span:nth-child(3) > span.value"))
            if ZJHRS==(CL+ZL) and ZYCXRS==YCX and WCX==(ZJHRS-ZYCXRS) and ZDB==YDB and ZCX==(YDB+WDB) and WDB==(ZCX-YDB):
                self.Data["actual_result"] = True
            else:
                self.Data["actual_result"] = False
        except BaseException as error:
            self.Data["actual_result"] = "定位过程中出现元素丢失。原因:{}".format(error)
        #截图/校验部分/用于判断用例是否通过
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def charts(self):
        """
        首页-数字概览
        :return:
        """
        try:
            for x in range(1,2):
                ss = ["线下","线上"]
                self.driver.click("div  div.top > div:nth-child(2) > div span")
                self.driver.click("//li/span[contains(text(),\"{}\")]".format(ss[x-1]))
            self.driver.Page_scrolling(100000)

            self.driver.click("#app > div > div.container.main-right.scroll-bar")
            self.driver.click("div.wrapper > div.line div.right-wrapper > div > span.chart.active")
            self.driver.click("div.condition.conditions > div.right-wrapper > div > span.tables")
            self.driver.click("div.right-wrapper > div:nth-child(1) > span")
            self.driver.click("div.right-wrapper > div:nth-child(2) > span.chart")
            self.driver.click("div.left-wrapper > div:nth-child(1) div > span > span > i")
            self.driver.click("//li/span[contains(text(),\"达标走势\")]")

        except BaseException as error:
            self.Data["actual_result"] = "定位过程中出现元素丢失。原因:{}".format(error)
        #截图/校验部分/用于判断用例是否通过
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]
