import pytest
from selenium import webdriver
import time
import os
import sys

from common.basepage import Base
from common.loginpage_locators import LoginPageLocator as lg
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\PYcharm\python16")))





#声明他是一个fixture
@pytest.fixture(scope="session")
def d1():
    global driver  # global声明一个全局变量
    driver=webdriver.Chrome()
    driver.get('https://gsm.jdjinsui.com/signin.html?redirect=/monitor/browser')
    driver.maximize_window()
    yield driver

    #后置操作
    print("---------------结束----------------")
    driver.quit()

#声明他是一个fixture
@pytest.fixture(scope="class")
def d2():
    global driver
    driver=webdriver.Chrome()
    driver.get('https://gsm.jdjinsui.com/signin.html?redirect=/monitor/browser')
    driver.maximize_window()
    # 步骤一：输入账号
    Base(d1).send(lg.name_text,text="13547324646")
    #步骤二：输入密码
    Base(d1).send(lg.pwd_text,text="a1234567")
    #步骤三：点击登陆
    Base().click(lg.login_but)
    time.sleep(1.5)
    time.sleep(5)

    yield driver
    #后置操作
    print("---------------结束----------------")
    driver.quit()


#声明他是一个fixture
@pytest.fixture(scope="class")
def d3():
    global driver
    '''
    个人账户点击系统设置
    :return:
    '''
    driver=webdriver.Chrome()
    driver.get('https://gsm.jdjinsui.com/signin.html?redirect=/monitor/browser')
    driver.maximize_window()
    # 步骤一：输入账号
    Base(driver).send(lg.name_text, text="13547324646")
    # 步骤二：输入密码
    Base(driver).send(lg.pwd_text, text="a1234567")
    # 步骤三：点击登陆
    Base(driver).click(lg.login_but)
    time.sleep(1.5)
    time.sleep(5)
    #鼠标移动到个人账户
    Base(driver).move_to_element(lg.zh)
    #点击系统设置
    Base(driver).finds(lg.zh_xllb)[1].click()
    time.sleep(3)
    yield driver
    #后置操作
    print("---------------结束----------------")
    driver.quit()




@pytest.fixture()
def sx():
    #前置操作
    yield
    time.sleep(2)
    driver.refresh()
