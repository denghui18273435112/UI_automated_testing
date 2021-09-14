#-*- conding:utf-8 -*-
#@File      :product.py
#@Time      : 10:06
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import time
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium


#模板
    # def kinds_standards(self):
    #     """
    #     首页-数字概览
    #     :return:
    #     """
    #     try:
    #         pass
    #     #截图/校验部分/用于判断用例是否通过/定位不到抛异常
    #     except BaseException as error:
    #         self.Data["actual_result"] = self.Data["location_fail_hint"]+error
    #     self.driver.screenShots()
    #     alluer(self.Data)
    #     return self.Data["actual_result"]

class home:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        self.driver.screenShots()
        time.sleep(5)
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def overview_digital(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'数字概览')]")
            CXJHZRS=self.driver.text_acquire("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS = int(CXJHZRS.split("/")[0])
            ZJHRS = int(CXJHZRS.split("/")[1])
            CL=int(self.driver.text_acquire("span:nth-child(2) > span.value"))
            ZL=int(self.driver.text_acquire("span:nth-child(3) > span.value"))
            YCX=int(self.driver.text_acquire("span:nth-child(4) > span.value"))
            WCX=int(self.driver.text_acquire("span:nth-child(5) > span.value"))
            ZDBZCX = self.driver.text_acquire("div:nth-child(2) > div > div.container  span:nth-child(1) > span.total")
            ZDB = int(ZDBZCX.split("/")[0])
            ZCX = int(ZDBZCX.split("/")[1])
            YDB=int(self.driver.text_acquire("div:nth-child(2)  div.container  span:nth-child(2) > span.value"))
            WDB=int(self.driver.text_acquire("div:nth-child(2)  div.container  span:nth-child(3) > span.value"))
            if ZJHRS==(CL+ZL) and ZYCXRS==YCX and WCX==(ZJHRS-ZYCXRS) and ZDB==YDB and ZCX==(YDB+WDB) and WDB==(ZCX-YDB):
                self.Data["actual_result"] = True
            else:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def charts(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'数字概览')]")
            self.driver.click("div  div.top > div:nth-child(2) > div span")
            self.driver.click("//li/span[contains(text(),\"线上\")]")
            self.driver.click("#app > div > div.container.main-right.scroll-bar > div.wrapper")
            self.driver.click("#app > div > div.container.main-right.scroll-bar")
            self.driver.click("div.wrapper > div.line div.right-wrapper > div > span.chart.active")
            self.driver.click("div.condition.conditions > div.right-wrapper > div > span.tables")
            self.driver.click("div.right-wrapper > div:nth-child(1) > span")
            self.driver.click("div.right-wrapper > div:nth-child(2) > span.chart")
            self.driver.click("div.left-wrapper > div:nth-child(1) div > span > span > i")
            self.driver.click("//li/span[contains(text(),\"达标走势\")]")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def kinds_standards(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'数字概览')]")
            CXJHZRS=self.driver.text_acquire("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS = int(CXJHZRS.split("/")[0])
            self.driver.Page_scrolling()
            sum_new = 0
            for x in range(1,5):
                dingwei = self.driver.text_acquire("div.pies > div:nth-child(2)  div:nth-child({}) > div > span:nth-child(1)".format(x))
                sum_new += int(dingwei.split(":")[1])
            if  sum_new!=ZYCXRS:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def student_details(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'学员详情')]")
            gongsi = self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div > span")
            name = self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tr:nth-child(1) > td.el-table_1_column_2.is-center > div > span")
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input",name,ifhuiche=True)
            gongsi_new  =self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div > span")
            if  gongsi != gongsi_new:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input",gongsi,ifhuiche=True)
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input"," ",ifhuiche=True)
            for x in range(0,6):
                kecheng = ["B类：新型寿险产品销售培训","D类：新型寿险和车险销售培训","C类：车险产品销售培训","车险业务知识","新型寿险业务知识","A类：基础保险销售业务知识培训"]
                self.driver.drop_down_box("div.condition-wrapper  div:nth-child(2) > div.el-select > div > span","//li/span[contains(text(),\"{}\")]".format(kecheng[x]))
            for xx in range(0,2):
                dabiao =["未达标","已达标"]
                self.driver.drop_down_box("div:nth-child(3) > div.el-select > div.el-input.el-input--suffix > span > span > i","//li/span[contains(text(),\"{}\")]".format(dabiao[xx]))
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def company_data(self):
        """
        首页-数字概览
        :return:
        """
        try:
             self.driver.zzl_click("//span[contains(text(),'公司数据')]")
             self.driver.zzl_click("div.top20.table-area > div.tabs > span.tables > svg","css")
             self.driver.zzl_click("div.top20.table-area > div.tabs > span.chart >svg","css")
             self.driver.FEBCS_CCSKK("div.condition > div > div > div:nth-child(1) > div > input",
                                     self.driver.text_acquire(" table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div"),ifhuiche=True)
             self.driver.zzl_click("div.condition > div > div > div:nth-child(2) > span","css")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def tabulate_data(self):
        """
        首页-数字概览
        :return:
        """
        try:
            self.driver.click("//span[contains(text(),'汇总数据')]")
            CXRS = self.driver.text_acquire("tbody  tr td:nth-child(2) div")
            if int(CXRS)!=0:
                self.Data["actual_result"] =="有数据没问题"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]