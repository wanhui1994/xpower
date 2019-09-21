#coding=utf-8
'''页面元素封装'''
from appium import webdriver
from common.driver import Device
from appium.common.exceptions import NoSuchContextException



class Elemen():
    def __init__(self):
        at = Device()
        self.driver = at.get_driver()

    def element(self, locator):
        '''元素定位方法'''
        try:
            element = self.driver.find_element(*locator)  # *号是把两个参数分开传值
            return element
        except NoSuchContextException as msg:
            print('元素查找异常：%s' % msg)

    def click(self, locator):
        ''' 点击效果'''
        element = self.element(locator)
        element.click()

    def clea(self, locator):
        '''清空效果'''
        element = self.element(locator).clear()
        element.clear()

    def send(self, locator, txt):
        ''' 输入信息'''
        element = self.element(locator)
        element.clear()
        element.send_keys(txt)


