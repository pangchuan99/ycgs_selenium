import pytest

from selenium import webdriver


from TestData.zh_001 import zh_01_login

import time


class  Test_login:



    def test_login_eeror(self,d1,sx):
        '''
        输入错误账号进行登录
        步骤一：输入账号
        步骤二：输入密码
        步骤三：点击登陆
        步骤四：断言提示语是否正确
        :param d123:
        :return:
        '''
        #步骤一：输入账号
        zh_01_login(d1).login_name("13547324")

        #步骤二：输入密码
        zh_01_login(d1).login_pwd("a12354567")

        #步骤三：点击登陆
        zh_01_login(d1).login_click()
        time.sleep(1.5)
        #步骤四：断言提示语是否正确
        text=zh_01_login(d1).login_text()
        print(text)
        assert text=="账户或密码错误"

    def test_login_correct(self,d1):
        time.sleep(3)
        '''
        输入错误账号进行登录
        步骤一：输入账号
        步骤二：输入密码
        步骤三：点击登陆
        :param d123:
        :return:
        '''
        #步骤一：输入账号
        zh_01_login(d1).login_name("13547324646")

        #步骤二：输入密码
        zh_01_login(d1).login_pwd("a1234567")

        #步骤三：点击登陆
        zh_01_login(d1).login_click()
        time.sleep(1.5)
        # #步骤四：断言提示语是否正确
        # text=zh_01_login(d1).login_text()
        # print(text)
        # assert text=="账户或密码错误"






