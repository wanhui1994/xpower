#coding=utf-8
import yaml,os
from appium import webdriver

curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
yamlpath = os.path.join(curpath, "pageelement\\device")

# 测试设备封装
class Device():

    def __init__(self):
        a = open(yamlpath, 'rb')
        data = yaml.load(a, Loader=yaml.FullLoader)
        desired_caps = {}
        desired_caps['platformName']=data['platformName']
        desired_caps['platformVersion']=data['platformVersion']
        desired_caps['deviceName']=data['deviceName']
        desired_caps['appPackage']=data['appPackage']
        desired_caps['appActivity']=data['appActivity']
        self.driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver


