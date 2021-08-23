#-*- conding:utf-8 -*-
#@File      :product.py
#@Time      : 10:06
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.selenium import selenium
from tools.Base import Judgment_Reporting
import time
class product:

    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(Data["URL"])

    def add_product(self):
        self.driver.click("#main > div > div > p > a")
        self.driver.input_text("#name",self.data["product_name"])
        self.driver.input_text("#code",self.data["product_code"])
        self.driver.click_two("#PO_chosen > a > div:nth-child(3)","//*[@id='PO_chosen']/div/ul/li[contains(text(),'{}')]".format(self.data["product_head"]))
        self.driver.click_two("#QD_chosen > a > div:nth-child(2)","//*[@id='QD_chosen']/div/ul/li[contains(text(),'{}')]".format(self.data["test_head"]))
        self.driver.click_two("#RD_chosen > a > div:nth-child(2)","//*[@id='RD_chosen']/div/ul/li[contains(text(),'{}')]".format(self.data["release_head"]))
        self.driver.click_two("#type","//*[@id='type']/option[contains(text(),'{}')]".format(self.data["product_type"]))

        # self.driver.nested_page("#createForm > table > tbody > tr:nth-child(9) > td > div.ke-container.ke-container-default > div.ke-edit > iframe")
        # self.driver.find_element_by_tag_name("body","dada")
        time.sleep(1)
        self.driver.screenShots()
        self.driver.click("#submit")
        Judgment_Reporting(self.Data,"select * from zt_product","name",self.data["product_name"])

