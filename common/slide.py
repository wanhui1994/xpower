#conding=utf-8

from appium import webdriver
from common.mobile_device import Device


#屏幕滑动封装
class wh():
     def __init__(self):
         desired_caps=Device()
         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps.desired('com.android.bsch.yundianbiz','com.faxuan.law.app.login.WelcomeActivity'))

     def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

     def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
wwh=wh()
wwh.swipLeft(n=2)