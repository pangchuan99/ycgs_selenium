
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from common.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from common.basepage import Base
import time


class zh_01_login(Base):#继承Base

    def login_name(self,name):
        '''
        输入账号
        :param name: 账号
        :return:
        '''
        self.send(loc.name_text,name)

    def login_pwd(self,pwd):
        '''
        输入密码
        :param pwd:密码
        :return:
        '''
        self.send(loc.pwd_text, pwd)

    def login_click(self,):
        '''
        点击登陆
        :param pwd:密码
        :return:
        '''
        self.click(loc.login_but)

    def login_text(self):
        '''
        获取提示语
        :param pwd:密码
        :return:
        '''
        text=self.get_text(loc.tishicuowu)
        print("获取到元素的文本内容是：{} ".format(text))
        return text
















