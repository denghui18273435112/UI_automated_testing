import time
import imageio
import pytest
from selenium import webdriver
from config.Conf import *
from tools.Base import *
from tools.Yaml_read import Yaml_read
from tools.selenium import selenium
import os

@pytest.fixture(scope="session",autouse=True)
def driver():
    """
    前置：删除report/result的文件信息；登录并返回浏览器驱动
    后置：关闭浏览器
    :return:
    """
    #清空报告文件夹下的垃圾文件
    try:
        for one in os.listdir(result_path()):
            if "environment.properties" not in one:
                os.remove(result_path()+os.sep+"{}".format(one))
        for one_1 in os.listdir(get_file_path_photo()):
            os.remove(get_file_path_photo()+os.sep+"{}".format(one_1))
    except:
        print("\n>>没有可删除的文件>>")
    os.system("pip freeze > requirements.txt")
    #登录
    login=Yaml_read("all.yaml","login")
    #窗口是否可见；False 可见；True 不可见
    # option = ChromeOptions()
    # option.headless =False
    # option.add_argument('window-size=1920x1080')
    # driver = webdriver.Chrome(options=option)
    #窗口可见
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(login["url"])
    selenium(driver).input_text("请输入账号",login["login_account"])
    selenium(driver).input_text("请输入密码",login["password"])
    while True:
        #手动登录
        selenium(driver).click("请输入验证码",type="css")
        time.sleep(2)
        #自动登录
        #selenium(driver).input_text("请输入验证码",login["code"])
        selenium(driver).click("span.login-button")
        if selenium(driver).get_url() ==login["login_pass_url"]:
            break
    yield driver
    driver.quit()

    #截图进行拼接生成gif
    image_list=[]
    for one in os.listdir(photo):
        image_list.append(photo+os.sep+"/{}".format(one))
    gif_name = BASE_DIR+'\\自动化拼接.gif'
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.8)