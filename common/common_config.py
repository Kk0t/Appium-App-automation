# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
class CommonConfig:
    SYSTEM_NAME = "WINDOWS"  # 平台系统：Windows/Unix
    ANDROID = "android"
    IOS = "ios"
    WEBVIEW = ''
    NATIVE = "NATIVE_APP"
    DRIVER = ""
    TIMEOUT = 10
    SWIPETIME = 300
    SLEEPTIME = 3
    CYCLETIME = 3
    REMOTE="http://localhost:4723/wd/hub"
    OS_NAME=""
    StartTestTime=""

    PATH = {  # 根据自己目录修改
        'apk': "\\testapk\\xxx.apk",
        'testReport': './testData/testReport.json',
        'chromedriver_version': 'C:/Program Files (x86)/Appium/node_modules/appium/node_modules/appium-chromedriver/chromedriver/driver_version/',
        'chromedriver_win': 'C:/Program Files (x86)/Appium/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/',
    }

    DEVICES = {'devices': '三星S8',  # 自行修改测试设备的型号，可以随便写
               'platformName': 'android',  # 必须写'android'
               'platformVersion': '7.0',  # 可以自己写，无响应，但必须存在
               'udid': '84721d18'  # 必须填写已连接的设备UDID
               }
    APP = {'appPackage': '',  # 测试APK的包名
           'appActivity': '',  # 测试APK的AppActivity
           }
    APPIUM = {'Remote': 'http://127.0.0.1:4723/wd/hub',  # 默认
              'appiumjs': 'node C:\\Appium\\node_modules\\appium\\bin\\appium.js'  # 根据自己的本地路径修改
              }
    MYSQL = {  # 数据库信息
        'host': '', 'user': '', 'password': '', 'port': ''}
