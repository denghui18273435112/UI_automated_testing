import time
import imageio
import pytest
from PIL import Image
from selenium import webdriver
from config.Conf import *
from tools.Base import *
from tools.Yaml_read import Yaml_read
from tools.selenium import selenium
import os
from config.Conf import _file_path
from tools.verification_code import verification_code
from selenium.webdriver import ChromeOptions

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
            if "_截图" in one_1:
                os.remove(get_file_path_photo()+os.sep+"{}".format(one_1))
    except:
        print("\n>>没有可删除的文件>>")
    os.system("pip freeze > requirements.txt")
    #登录
    login=Yaml_read("all.yaml","login")
    #窗口是否可见；False 可见；True 不可见
    option = ChromeOptions()
    option.headless =True
    option.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=option)
    #窗口可见
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(login["url"])
    time.sleep(5)
    selenium(driver).input_text("请输入账号",login["login_account"])
    selenium(driver).input_text("请输入密码",login["password"])
    while True:
        #获取验证码
        element =driver.find_element_by_css_selector('#app > div > div.container > div > div.form > form > div.el-form-item.verifycode.is-required > div > img') # 定位验证码图片
        left = int(element.location['x'])  # 获取图片左上角坐标x
        top = int(element.location['y'])  # 获取图片左上角y
        right = int(element.location['x'] + element.size['width'])    # 获取图片右下角x
        bottom = int(element.location['y'] + element.size['height'])  # 获取图片右下角y
        path = _file_path + os.sep + 'code.png'  # 生成随机文件名
        driver.save_screenshot(path)    # 截取当前窗口并保存图片
        im = Image.open(path)        # 打开图片
        im = im.crop((left, top, right, bottom))  # 截图验证码
        im.save(path)    # 保存验证码图片
        print(verification_code())

        #手动登录
        # selenium(driver).click("请输入验证码",type="css")
        # time.sleep(2)
        #自动登录
        selenium(driver).input_text("请输入验证码",verification_code())

        selenium(driver).click("span.login-button")
        if selenium(driver).get_url() ==login["login_pass_url"]:
            break
        driver.find_element_by_css_selector('#app > div > div.container > div > div.form > form > div.el-form-item.verifycode.is-required > div > img').click()
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