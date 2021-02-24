import pytest
from selenium import webdriver
import time
import os
import sys
from TestData.zh_001 import zh_01_login
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\PYcharm\python16")))





#声明他是一个fixture
@pytest.fixture(scope="class")
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
def d12():
    driver=webdriver.Chrome()
    driver.get('https://gsm.jdjinsui.com/signin.html?redirect=/monitor/browser')
    driver.maximize_window()
    #输入账号
    zh_01_login(driver).login_name(name="13547324646")
    # 输入密码
    zh_01_login(driver).login_pwd(pwd="a1234567")
    # 点击登陆
    time.sleep(2)
    zh_01_login(driver).login_click()
    time.sleep(5)
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
