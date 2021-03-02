from selenium import webdriver
import pytest
from common.basepage import Base
from common.loginpage_locators import LoginPageLocator as lg
import time


class  Test_xtsz_qqbpz():


    def test_xtsz_qqbpz_001(self,d3,sx):

        '''
        输入错误账号进行登录
        步骤一：鼠标悬停系统设置
        步骤二：点击情报板配置
        步骤三：点击添加类型
        步骤四：点击厂家
        步骤五：点击下拉第一个
        步骤六：点击保存
        :param d123:
        :return:
        '''

        # 步骤一：鼠标悬停系统设置
        Base(d3).move_to_element(lg.zh_xtsz)
        time.sleep(1.5)
        # 步骤二：点击情报板配置
        Base(d3).click(lg.zh_xtsz_qbbpz)
        time.sleep(1.5)
        # 步骤三：点击添加类型
        Base(d3).click(lg.zh_xtsz_qbbpz_tjxlx)
        # 步骤四：点击厂家
        Base(d3).click(lg.zh_xtsz_qbbpz_cj1)
        # 步骤五：点击下拉第一个
        Base(d3).finds(lg.zh_xtsz_qbbpz_xlnr)[0].click()
        # 步骤六：点击保存
        Base(d3).click(lg.zh_xtsz_qbbpz_bc)


    def test_xtsz_qqbpz_002(self,d3,sx):


        '''
        输入错误账号进行登录
        步骤一：鼠标悬停系统设置
        步骤二：点击情报板配置
        步骤三：点击添加类型
        步骤四：点击厂家
        步骤五：点击下拉第一个
        步骤六：点击保存
        :param d123:
        :return:
        '''
        # 步骤一：鼠标悬停系统设置
        Base(d3).move_to_element(lg.zh_xtsz)
        time.sleep(1.5)
        # 步骤二：点击情报板配置
        Base(d3).click(lg.zh_xtsz_qbbpz)
        time.sleep(2)

        a1=Base(d3).finds(lg.zh_xtsz_qbbpz_lb)[-1]
        Base(d3).js_focus_element(a1)


