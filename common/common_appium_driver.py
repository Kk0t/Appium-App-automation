# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
from appium import webdriver
from common.common_config import CommonConfig
from util.adb_util import ADBUtil



class CommonAppiumDriver:



    def get_driver(self):
        try:
            adb = ADBUtil()
            udids = adb.get_devices()
            self.desired_caps = {}
            self.desired_caps['platformName'] = CommonConfig.DEVICES['platformName']  # 平台
            self.desired_caps['platformVersion'] = adb.get_phonerelease(udids[0]) # 系统版本
            self.desired_caps['appPackage'] = CommonConfig.APP['appPackage']  # APK包名
            self.desired_caps['appActivity'] = CommonConfig.APP['appActivity']  # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = 'true'  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法
            self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            self.desired_caps['deviceName'] = CommonConfig.DEVICES['devices']  # 手机ID
            self.desired_caps['udid'] = udids[0]
            self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
            self.desired_caps['autoGrantPermissions'] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
            return self.driver
        except Exception as e:
            print(e)



