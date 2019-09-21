import os,time,yaml
# from ruamel import yaml
from appium import webdriver

curpath = os.path.dirname(os.path.realpath(__file__))

print(curpath)
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
#
yamlpath="C:\\study\\xpower_appium1\\pageelement\\loginpage"
a= open(yamlpath,'rb')
c=yaml.load(a.read(),Loader=yaml.Loader)
print(c['sj']['phone']['id'])
# data=yaml.load(a,Loader=yaml.FullLoader)
# print(c['ChuaTony']['联络'][0])
# # print(data['公司'])g
# # print(data)
#
# yamlpath = "C:\\study\\xpower_appium1\\pageelement\\device"
# a= open(yamlpath,'r')
# data=yaml.load(a,Loader=yaml.FullLoader)
# desired_caps={}
# desired_caps['platformName']=data['platformName']
# desired_caps['platformVersion']=data['platformVersion']
# desired_caps['deviceName']=data['deviceName']
#
# desired_caps['appPackage']=data['appPackage']
# desired_caps['appActivity']=data['appActivity']
#
#
# #启动app
# print('启动app')
# #driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
