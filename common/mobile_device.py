#coding=utf-8

import os,re

class Device():
    def vesion(self):
        #获取连接电脑的设备名称信息
        self.readDeviceId = list(os.popen('adb devices').readlines())
        deviceId = re.findall(r'^\w*\b', self.readDeviceId[1])[0]
        return deviceId

    def devicevsion(self):
        #获取连接电脑设备的版本
        deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
        deviceVersion = "".join(deviceAndroidVersion).strip()
        return deviceVersion

    def Package(self):
        #获取执行的apk的包名
        pass
    def apk(self):
        pwd = os.getcwd()
        father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
        path=father_path+"\\apk\\app-release.apk"
        return path

    def desired(self,package,activity):
        #移动设备信息
        if len(list(os.popen('adb devices').readlines())[1].rstrip())>0:
            desired_caps = {
            'platformName':'Android',
            'deviceName': self.vesion(),
            'platformVersion': self.devicevsion(),
            'appPackage' : package,   #输入apk的包名
            'appActivity': activity,  #输入apk的activity
            'sessionOverride':'true', #每次启动时覆盖session
            'app':self.apk(),
            'noReset':'True',
            }
            return desired_caps
        else:
            print("测试手机未连接")