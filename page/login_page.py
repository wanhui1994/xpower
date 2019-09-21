#conding=utf-8

from common.element import Elemen
from appium import webdriver
import os,yaml,time

curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
yamlpath = os.path.join(curpath, "pageelement\\loginpage")
a = open(yamlpath, 'rb')
data = yaml.load(a, Loader=yaml.FullLoader)

class Lg(Elemen):
    sjphone_loca=('id',data['sj']['phone']['id'])
    sjpas_loca = ('id', data['sj']['pas']['id'])
    sjlg_loca = ('id', data['sj']['lg']['id'])
    sjys_loca = ('id', data['sj']['ys']['id'])
    sjforgetpas_loca = ('id', data['sj']['forgetpas']['id'])


    def sjinput_phone(self,txt):
        self.send(self.sjphone_loca,txt)

    def sjinput_pas(self,txt):
        self.send(self.sjpas_loca,txt)

    def sjclick_lg(self):
        self.click(self.sjlg_loca)

    def sjclick_ys(self):
        self.click(self.sjys_loca)

    def sjclick_forgetpas(self):
        self.click(self.sjforgetpas_loca)

    def  sjlogin(self,phone,pas):
        '''商家端登录'''
        self.sjinput_phone(phone)
        self.sjinput_pas(pas)
        self.sjclick_lg()

