
from selenium.webdriver.support.wait import WebDriverWait        #显示等待类
#显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC  #判断元素16种方法
from selenium.webdriver.common.keys import Keys  #键盘输入
from selenium.webdriver.common.action_chains import ActionChains  #鼠标事件
from selenium.common.exceptions import TimeoutException #异常超时
from selenium.common.exceptions import ElementNotVisibleException




class LocatorTypeError(Exception):
    '''
    参数类型错误
    '''
    pass


class ElementNotFound(Exception):
    '''
    定位元素出现超时
    '''
    pass


class Base:
    def __init__(self,driver, timeout=10, t=0.5):
        self.driver=driver
        self.timeout = timeout
        self.t = t

    def find(self, locator):
        """定位到元素，返回元素对象，没定位到，Timeout异常
       WebDriverWait里面有三个参数
        第一个是：driver:浏览器驱动
        第二个是：timeout:最长超时时间默认以秒为单位
        第三个是：poll_frequency：检测的间隔步长，默认为0.5s"""

        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时！！！！，不要盯着报错看了，也不用截图贴群里了，"
                                      "先把定位技术学好，别复制粘贴xpath, 请检查你的定位方式，在浏览器先调试成功，观察页面是否正常打开")
            return ele

    def finds(self, locator):
        '''复数定位，返回elements对象 list'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles


    def click(self, locator):
        '''点击元素
        is_displayed检查元素是否可见
        '''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    def send(self, locator, text=''):
        '''输入文本'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            t = self.find(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""


    def clear_elment_text(self,loc):
        '''
        清除文本
        :param loc:定位的元素
        :return:
        '''
        self.driver.find_element(loc).send_keys(Keys.BACK_SPACE * 20)




    def roll_current_page(self,loc,sy):
      '''
      滚动到当前页面(聚焦元素)
      elements(loc)[-1]  意思是 定位到这个列表  这个列表具体哪一条
      :param loc:定位的元素
      :param sy:索引
      :return:
      '''
      self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(loc)[sy])


    def mouse_suspension(self,loc):
        '''
        鼠标悬浮
        :param loc:定位的元素
        :return:
        '''
        ActionChains(self.driver).move_to_element(self.driver.find_element(loc)).perform()

    def get_text_elements(self,loc,sy):
        '''
        复数定位点击事件
         获取复数定位，然后定位到具体值上面
        :param loc:定位的元素
        :param sy:索引
        :return:
        '''
        self.driver.find_elements(loc)[sy].click()

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)" % x
        self.driver.execute_script(js)












