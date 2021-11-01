# -*- coding: utf-8 -*-
import time

from common.common_config import CommonConfig
from common.common_mysql_operate import *
from util.adb_util import ADBUtil
from util.apk_util import ApkUtil
from util import devices_util


def get_apk_data(udid):
    """获取测试apk的信息及测试设备的信息，写入数据库"""
    adb = ADBUtil()
    ai = ApkUtil()
    apk_name = ai.get_apk_name()  # app名字
    apk_siz = ai.get_apk_size()  # app大小
    apk_packageName = ai.get_apk_packageName()  # app包名
    apk_versionName = ai.get_apk_versionName()  # app版本名称
    apk_versionCode = ai.get_apk_versionCode()  # app版本号
    phone_name = adb.get_phonemodel(udid)
    release = adb.get_phonerelease(udid)  # 系统版本
    men_total = devices_util.get_men_total("../men_total.txt", udid)  # 运行内存
    cpu_sum = devices_util.get_cpu_kel("../cpu.txt", udid)  # 几核cpu
    pix = devices_util.get_app_pix(udid)  # 得到手机分辨率

    #######  测试包及测试机的信息写入数据库  #######
    CommonConfig.StartTestTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    apk_info(apk_name, apk_siz, apk_packageName,
                                  apk_versionCode, apk_versionName, CommonConfig.StartTestTime)
    test_devices(udid, phone_name, release,
                                      men_total, cpu_sum, pix, CommonConfig.StartTestTime)

    # 赋值全局参数 DEVICES
    CommonConfig.DEVICES['devices'] = phone_name
    CommonConfig.DEVICES['platformVersion'] = release
    CommonConfig.DEVICES['udid'] = udid
    CommonConfig.DEVICES['platformName'] = 'android'
    CommonConfig.DEVICES['pix'] = pix
