import pytest
from common.basepage import Base
from common.loginpage_locators import LoginPageLocator as lg
import time


class  Test_login():
    test_datas = [
        ({"username": "1354732464", "password": "1223456"}, "账户或密码错误"),
        ({"username": "135473246461", "password": ""},"账户或密码错误"),
        ({"username": "",  "password": "a1234567"},"账户或密码错误"),
        ({"username": "13547324646",  "password": "a1234567"},"")]

    @pytest.mark.parametrize("test_input,expected",test_datas)
    def test_login_eeror1(self,d1,test_input,expected,sx):
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
        Base(d1).send(lg.name_text,text=test_input["username"])


        #步骤二：输入密码
        Base(d1).send(lg.pwd_text,text=test_input["password"])

        #步骤三：点击登陆
        Base(d1).click(lg.login_but)
        time.sleep(1.5)
        assert Base(d1).get_text(lg.tishicuowu)==expected
        time.sleep(1)




