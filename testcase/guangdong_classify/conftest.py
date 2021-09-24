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
    print("\n>>清空无关图片或文件中....>>\n")
    try:
        for one in os.listdir(result_path()):
            if "environment.properties" not in one:
                os.remove(result_path()+os.sep+"{}".format(one))
        for one_1 in os.listdir(get_file_path_photo()):
            if "_截图" in one_1:
                os.remove(get_file_path_photo()+os.sep+"{}".format(one_1))
    except:
        print("\n>>没有可删除的文件>>\n")
    print("\n>>安装最新插件中.....>>\n")
    os.system("pip freeze > requirements.txt")
    print("\n>>进入UI自动化测试环节.....>>\n")
    #打开浏览器
    # option = ChromeOptions()
    # option.headless =False
    # option.add_argument('window-size=1920x1080')
    # driver = webdriver.Chrome(options=option)

    driver = webdriver.Chrome()
    driver.maximize_window()

    #登录
    login=Yaml_read("all.yaml","login")
    driver.get(login["url"])
    time.sleep(5)
    selenium(driver).input_text("请输入账号",login["login_account"])
    selenium(driver).input_text("请输入密码",login["password"])
    while True:
        #获取验证码截图并保存
        element =driver.find_element_by_css_selector('#app > div > div.container > div > div.form > form > div.el-form-item.verifycode.is-required > div > img')
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        path = _file_path + os.sep + 'code.png'
        driver.save_screenshot(path)
        im = Image.open(path)
        im = im.crop((left, top, right, bottom))
        im.save(path)
        print("\n识别的验证码:{}\n".format(verification_code()))

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

    # print("\n>>自动化测试已结束>>\n")
    # print("\n>>GIF拼接开始,进行中...........>>\n")
    # #截图进行拼接生成gif
    # image_list=[]
    # for one in os.listdir(photo):
    #     image_list.append(photo+os.sep+"/{}".format(one))
    # gif_name = BASE_DIR+'\\自动化拼接.gif'
    # frames = []
    # for image_name in image_list:
    #     frames.append(imageio.imread(image_name))
    # imageio.mimsave(gif_name, frames, 'GIF', duration=0.8)
    # print("\n>>GIF拼接已结束>>\n")