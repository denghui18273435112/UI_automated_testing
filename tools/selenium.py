from selenium.webdriver.common.keys import Keys
from config.Conf import ConfigYaml
from selenium.webdriver.support.select import Select
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from tools.WinUpLoadFile import upload_files
import allure
from datetime import datetime
from config.Conf import *
from tools.WinUpLoadFile import upload_files
import os
from tools.logUtil import my_log
from tools.Base import *
from tools.Yaml_read import Yaml_read
class selenium(object):
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver= driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def resfresh(self):
        """
        刷新页面
        @return:
        """
        self.driver.refresh()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def clear(self):
        """
        清空文本数据
        :return:
        """
        self.driver.clear()

    def get_url(self):
        """
        获取当前页面的url
        :return:
        """
        return self.driver.current_url

    def click(self):
        """
        点击
        :return:
        """
        self.driver.click()

    def send_keys(self,content):
        """
        文本输入
        :param content:
        :return:
        """
        self.driver.send_keys(content)

    def text(self,location):
        """
        根据定位获取文本信息
        :param location:
        :return:
        """
        dingwei = self.driver.find_element_by_css_selector(location)
        return dingwei.text

    #
    def find_element_by_id(self,id):
        self.driver.find_element_by_id(id)
    def find_element_by_name(self,name):
        self.driver.find_element_by_name(name)
    def find_element_by_class_name(self,class_name):
        self.driver.find_element_by_class_name(class_name)
    def find_element_by_link_text(self,name):
        self.driver.find_element_by_link_text(name)
    def find_element_by_partial_link_text(self,name):
        self.driver.find_element_by_partial_link_text(name)
    def find_element_by_xpath(self,name):
        self.driver.find_element_by_xpath(name)
    def find_element_by_css_selector(self,name):
        self.driver.find_element_by_css_selector(name)




    def jietu(self,filePath):
        """
        截图
        @param filePath:
        @parm file_path:截图后文件存放的位置
        @return:
        """
        file_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +os.sep+"file"
        self.driver.get_screenshot_as_file(get_file_path()+os.sep+filePath)

    def screenShots(self, name_screenshot="截图"):
        """
        截图
        @param name_screenshot:截图名称或图片名称
        @return:
        """
        #截图并读取，写入进入allure报告中 file:切图文件的名称;name_screenshot:在allure中显示测试步骤标题; allure.attachment_type.PNG allure步骤的类型
        file_name=get_file_path_photo()+os.sep + "\\{}_{}.png".format(time_YmdHMS(), name_screenshot)
        self.driver.get_screenshot_as_file(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, name_screenshot+time_YmdHMS(), allure.attachment_type.PNG)


    def roll(self,location="right",up="500"):
        """
        仅限于页面自带的进度条
        location: tElementsByClassName定位
        @return:
        """
        self.driver.execute_script( 'document.getElementsByClassName("{}")[0].scrollTop={}'.format(location,up))
        time.sleep(0.5)


    def editor_upload_photo(self,location1="i.w-e-icon-image",location2="i.w-e-icon-upload2",photo="banner.png"):
        """
        编辑器中上传图片
        @param location1:定位编辑器图片上传位置
        @param location2: 定位图片上传位置
        @param photo: 图片文件的名称
        @return:
        """
        self.driver.find_element_by_css_selector(location1).click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(location2).click()
        time.sleep(0.5)
        upload_files(photo)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)





        time.sleep(1)

    def FEBCS_CCSKK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S-回车
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector(location).send_keys(content)
        self.driver.find_element_by_css_selector(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def input_text(self, location, content,fushu=None, Enter=None):
        """
        文本输入
       @param location: 文本定位
       @param content: 输入内容
       @param Enter: 是否回车；传入为0回车；Enter=None不回车
       @return:
       """
        if fushu ==None:
            time.sleep(1)
            if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_element_by_css_selector("input[placeholder=\"{0}\"]".format(location))
            elif ">" in location or "#" in location:
                new_driver = self.driver.find_element_by_css_selector(location)
            elif location.isalpha() == True:
                new_driver = self.driver.find_element_by_id(location)
            new_driver.click()
            new_driver.clear()
            new_driver.send_keys(content)
            if Enter == 0:
                new_driver.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(10)
        else:
            time.sleep(1)
            if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_elements_by_css_selector("input[placeholder=\"{0}\"]".format(location))[fushu]
            elif ">" in location or "#" in location:
                new_driver = self.driver.find_elements_by_css_selector(location)[fushu]
            elif location.isalpha() == True:
                new_driver = self.driver.find_elements_by_id(location)[fushu]
            new_driver.click()
            new_driver.clear()
            new_driver.send_keys(content)
            if Enter == 0:
                new_driver.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(10)

    def send_key(self,content,Enter=None):
        """
        单纯输入
        :param Enter:
        :return:
        """
        self.driver.send_keys(content)
        if Enter == 0:
            self.driver.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)


    def test_input_id(self, location, content):
        """
        id类型的文本输入
        :param location:  id定位
        :param content:   输入的内容
        :return:
        """
        new_location = self.driver.find_element_by_id(location)
        new_location.click()
        new_location.clear()
        new_location.send_keys(content)

    def test_id(self, location):
        """
        id类型进行点击
        :param location:  id定位
        :return:
        """
        new_location = self.driver.find_element_by_id(location)
        new_location.click()

    def  text_data(self,location):
        """
        获取列表的文本数据
        :param location:位置
        :return:
        """
        return  self.driver.find_element_by_css_selector(location).text

    def select_pullDown_frame(self,location,option):
        """
        标准的select下拉框选项
        :param location:位置
        :param option:  根据索引、下拉框值
        :return:
        """
        if  option.isalpha() == True:
            Select(self.driver.find_element_by_css_selector(location)).select_by_visible_text(option)
        if isinstance(option,int) == True:
            Select(self.driver.find_element_by_css_selector(location)).select_by_index()


    def drop_down_box(self, location, location1, weizhi=None):
        """
        下拉框选择
        分两步：第一步点击弹出下拉框；第二步：选择下拉框选项
        备注：都支持复数
        @param location:第一步点击定位
        @param location1：下拉选项定位，下拉后的选项一般选择用xpath定位；css很难定位到
        @param weizhi: 第一步定位的位置
        @return:
        """

        time.sleep(1)
        if (">" in location or "." in location) and weizhi != None :
            self.driver.find_elements_by_css_selector(location)[int(weizhi)].click()
        elif (">" in location or "." in location) and weizhi == None :
            self.driver.find_element_by_css_selector(location).click()
        elif "/" in location  and weizhi != None :
            self.driver.find_element_by_xpath(location)[int(weizhi)].click()
        elif "/" in location  and weizhi == None :
            self.driver.find_element_by_xpath(location).click()
        elif '\u4e00' <= location <= '\u9fff' and weizhi != None:
            self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location))[int(weizhi)].click()
        elif '\u4e00' <= location <= '\u9fff' and weizhi == None:
            self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location)).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        if weizhi == None:
            if "/" in location1 or "//" in location1:
               self.driver.find_element_by_xpath(location1).click()
            elif '\u4e00' <= location1 <= '\u9fff':
                self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location1)).click()
                #self.driver.find_element_by_xpath("//*[text()=\"{}\"]".format(location1)).click()
            elif location1.isalpha() == True:
                self.driver.find_element_by_id(location1).click()
            elif ">" in location1:
                self.driver.find_element_by_css_selector(location1).click()
            self.driver.implicitly_wait(10)
            time.sleep(1)
        else:
            if "/" in location1 or "//" in location1:
               self.driver.find_elements_by_xpath(location1)[weizhi].click()
            elif '\u4e00' <= location1 <= '\u9fff':
                self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location1))[weizhi].click()
            elif location1.isalpha() == True:
                self.driver.find_elements_by_id(location1)[weizhi].click()
            elif ">" in location1:
                self.driver.find_elements_by_css_selector(location1)[weizhi].click()
            self.driver.implicitly_wait(10)
            time.sleep(1)

    def new_pull_down_choose(self,location,option_name,weizhi=None):
        """
        按钮点击；支持复数定位点击
        @param location:
        @param weizhi:
        @return:
        """
        time.sleep(1)
        if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_element_by_css_selector("input[placeholder={}]".format(location)).click()
        if ">" in location or "=" in location:
                new_driver = self.driver.find_element_by_css_selector(location).click()
        if "/" in location:
                new_driver = self.driver.find_element_by_xpath(location).click()
        time.sleep(0.5)
        new_driver.select_by_visible_text(option_name)
        self.driver.implicitly_wait(10)
        time.sleep(1)

    def pull_down_choose_s(self, location, option_name):
        """
        下拉选择
        @param location:  定位下拉文本框位置
        @param option_name: 下拉选项名称
        @return:
       """
        if '\u4e00' <= location <= '\u9fff':
                self.driver.find_element_by_css_selector("input[placeholder={}]".format(location)).click()
        if ">" in location or "=" in location:
                self.driver.find_element_by_css_selector(location).click()
        if "/" in location:
                self.driver.find_element_by_xpath(location).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"{0}")]'.format(option_name)).click()
        self.driver.implicitly_wait(10)


    def url_skip(self, name):
        """
        url跳转
        @param name: 模块名称
        @return:
        """
        login =Yaml_read("login.yaml")
        time.sleep(2)
        if name == "我的地盘-日程":
            self.driver.get(login["url"]+"/my-todo.html")
        if name == "我的地盘-首页":
            self.driver.get(login["url"]+"/my/")
        if name == "我的地盘-任务":
            self.driver.get(login["url"]+"/my-task.allure-report")
        if name == "我的地盘-Bug":
            self.driver.get(login["url"]+"/my-bug.allure-report")
        if name == "测试-Bug":
            self.driver.get(login["url"]+"/bug-browse-2.html")
        if name =="组织-用户":
            self.driver.get(login["url"]+"/company-browse.html")
        if name=="项目-看板":
            self.driver.get(login["url"]+"/project-kanban-2.allure-report")
        else:
            self.driver.get(login["url"]+name)
        time.sleep(2)


    def execute_script(self,shuxing,id,zhi):
        """
        更改页面属性
        :return:
        """
        if shuxing =="id":
            self.driver.execute_script('document.getElementById({0}).{1}'.format(id,zhi))



    def quit_iframe(self):
        """
        退出iframe嵌套网页 【常用之一】
        :return:
        """
        self.driver.switch_to.default_content()

    def nested_page(self,location):
        """
        进入iframe嵌套网页  【常用之一】
        嵌套页面;弹框;iframe窗口
        name属性、ID属性
        备注：没有可用的id或者name属性时
        可以先按照元素的定位方法，把frame找出来，再整体放到switch_to_frame()中
        内嵌网页后，需要有退出
        :param name:
        :return:
        """
        self.driver.switch_to.frame(location)

    def nested_page1(self,location):
        """
        进入iframe嵌套网页  【常用之一】
        嵌套页面;弹框;iframe窗口
        name属性、ID属性
        备注：没有可用的id或者name属性时
        可以先按照元素的定位方法，把frame找出来，再整体放到switch_to_frame()中
        内嵌网页后，需要有退出
        :param name:
        :return:
        """
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(location))

    def browser_pop_up(self,operation="YES",if_input=None):
        """
        浏览器自带的弹框操作 【常用之一】
        此类弹框无法用F12检测
        :param operation: YES 确认；NO 取消；TEXT 获取文本
        :return:
        """
        time.sleep(1)
        if operation =="YES":
            self.driver.switch_to.alert.accept()
        if operation == "NO":
            self.driver.switch_to.alter.dismisss()
        if operation == "TEXT":
            self.driver.switch_to.alert.text()
        if if_input !=None:
            self.driver.switch_to.alert.send_keys(operation)

    def Page_scrolling(self,location=10000):
        """
        页面滚动条滚动   【常用之一】
        :param location:滚动的位置； 10000：最底部；0：回到顶部
        :return:
        """
        js = 'var action=document.documentElement.scrollTop={}'.format(location)
        self.driver.execute_script(js)
        # js = "window.scrollTo({0},{1})".format(location,location)
        # self.driver.execute_script(js)

    def click_two(self, location,location1):
        """
        两次点击  【常用之一:于下拉选项】
        :param location:
        :param location1:
        :return:
        """
        if "/" in location or "//" in location or "*" in location:
            self.driver.find_element_by_xpath(location).click()
        elif '\u4e00' <= location <= '\u9fff':
            self.driver.find_element_by_xpath("//li[contains(text(),'{}')]".format(location)).click()
        elif location.isalpha() == True:
            self.driver.find_element_by_id(location).click()
        elif ">" in location or "#" in location:
            self.driver.find_element_by_css_selector(location).click()
        if "/" in location1 or "//" in location or "*" in location1:
            self.driver.find_element_by_xpath(location1).click()
        elif '\u4e00' <= location1 <= '\u9fff':
            self.driver.find_element_by_xpath("//li[contains(text(),'{}')]".format(location1)).click()
        elif location1.isalpha() == True:
            self.driver.find_element_by_id(location1).click()
        elif ">" in location1 or "#" in location1:
            self.driver.find_element_by_css_selector(location1).click()

    def click(self, location,type="xpath"):
        """
        点击操作  【常用之一】
        :param location: 定位 ；支持方式:xpthon、id、css
        :return:
        """
        if "/" in location or "//" in location or "*" in location:
            self.driver.find_element_by_xpath(location).click()
        elif '\u4e00' <= location <= '\u9fff' and type=="css":
            self.driver.find_element_by_css_selector("input[placeholder=\"{0}\"]".format(location)).click()
        elif '\u4e00' <= location <= '\u9fff':
            self.driver.find_element_by_xpath("//*[text()=\"{}\"]".format(location)).click()
        elif location.isalpha() == True:
            self.driver.find_element_by_id(location).click()
        elif ">" in location or "#" in location or "." in location :
            self.driver.find_element_by_css_selector(location).click()
        time.sleep(2)


    def pullDown_frame(self,location,option_name,label_name="li",matching_mode=True,joint=True):
        """
        下拉框选择  【常用之一】
        :param location:位置；方式CSS
        :param option_name：选项名称；方式：Xpath
        :param label_name:当前选项所在标签名称；默认：li
        :param matching_mode xpath的text方法支持包含匹配和精准匹配；默认包含匹配
        :param joint :是否对Xpath进行拼接
        :return:一般选项都放在 ul  li 标签上
        """
        self.driver.find_element_by_css_selector(location).click()
        if joint==True:
            if  matching_mode == True:
                self.driver.find_element_by_xpath("//{0}[contains(text(),'{1}')]".format(label_name,option_name)).click()
            else:
                self.driver.find_element_by_xpath("//{0}[text()='{1}']".format(label_name,option_name)).click()
        else:
                self.driver.find_element_by_xpath(option_name).click()

    def text_input(self,location,content,Enter=False,empty=False):
        """
        文本输入  【常用之一】
        :param location: 定位;支持两种定位方式 id  css
        :param content: 输入内容
        :param Enter:  文本框回车
        :param empty:  清空文本框中数据
        :return:
        """
        if location.isalpha() == True:
            text_frame = self.driver.find_elements_by_id(location)
        elif ">" in location or "#" in location:
            text_frame = self.driver.find_element_by_css_selector(location)
        text_frame.click()
        if empty ==True:
            text_frame.clear()
        text_frame.send_keys(content)
        if  Enter == True:
            text_frame.send_keys(Keys.ENTER)

    def  time_current_YmdHMS(self):
        """
        返回年月日时分秒  【常用之一】
        :return:
        """
        return  str(datetime.now().strftime("%Y%m%d%H%M%S"))

    def  time_current_Ymd(self):
        """
        返回年月日时  【常用之一】
        :return:
        """
        return  str(datetime.now().strftime("%Y-%m-%d"))

    def  upload_inputType(self, location, content="banner.png"):
        """
        上传文件   【常用之一】
        :param location: 位置
        :param content:  文件的相对路径
        :return:  input 方式的文件上传
        """
        self.driver.find_element_by_css_selector(location).send_keys(get_file_path()+os.sep+content)

    def upload_noInputType(self, location, photo="banner.png"):
        """
        上传文件  【常用之一】
        @param location1: 定位图片上传位置
        @param photo: 图片文件的名称;直接传file下的文件名称即可
        @return:  非input格式上传
        """
        self.driver.find_element_by_css_selector(location).click()
        time.sleep(1)
        browser_type="chrome"
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"

        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""
        dialog = win32gui.FindWindow("#32770", title)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, get_file_path()+os.sep+photo)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        time.sleep(1)