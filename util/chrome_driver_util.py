# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
import os
from util.adb_util import ADBUtil
from common.common_config import CommonConfig
import shutil


def copy_file(oldfile, newfile):
    old_filepath = os.path.join(CommonConfig.PATH['chromedriver_version'], oldfile)
    new_filepath = os.path.join(CommonConfig.PATH['chromedriver_win'], newfile)
    if os.path.exists(old_filepath):
        print('拷贝%s开始...' % oldfile)
        shutil.copyfile(old_filepath, new_filepath)
        print('拷贝完成')
    else:
        print('未找到%s文件' % oldfile)


def get_chromedriver(udid):
    a = ADBUtil()
    version = a.get_chromedriver_version(udid)
    if version >= 6403282.0:
        copy_file("chromedriver2.37.exe", "chromedriver.exe")
    elif version >= 6303239.0 and version <= 6403282.0:
        copy_file("chromedriver2.36.exe", "chromedriver.exe")
    elif version >= 6203202.0 and version <= 6303239.0:
        copy_file("chromedriver2.35.exe", "chromedriver.exe")
    elif version >= 6103163.0 and version <= 63032390:
        copy_file("chromedriver2.34.exe", "chromedriver.exe")
    elif version >= 6003112.0 and version <= 6103163.0:
        copy_file("chromedriver2.33.exe", "chromedriver.exe")
    elif version >= 5903071.0 and version <= 6003112.0:
        copy_file("chromedriver2.32.exe", "chromedriver.exe")
    elif version >= 5803029.0 and version <= 5903071.0:
        copy_file("chromedriver2.30.exe", "chromedriver.exe")
    elif version >= 5702987.0 and version <= 5803029.0:
        copy_file("chromedriver2.29.exe", "chromedriver.exe")
    elif version >= 5502883.0 and version <= 5702987.0:
        copy_file("chromedriver2.28.exe", "chromedriver.exe")
    elif version >= 5402840.0 and version <= 5502883.0:
        copy_file("chromedriver2.27.exe", "chromedriver.exe")
    elif version >= 5302785.0 and version <= 5402840.0:
        copy_file("chromedriver2.25.exe", "chromedriver.exe")
    elif version >= 5202743.0 and version <= 5302785.0:
        copy_file("chromedriver2.24.exe", "chromedriver.exe")
    elif version >= 5102704.0 and version <= 5202743.0:
        copy_file("chromedriver2.23.exe", "chromedriver.exe")
    elif version >= 4902623.0 and version <= 5102704.0:
        copy_file("chromedriver2.22.exe", "chromedriver.exe")
    elif version >= 4602490.0 and version <= 4602490.0:
        copy_file("chromedriver2.21.exe", "chromedriver.exe")
    elif version >= 4302357.0 and version <= 4602490.0:
        copy_file("chromedriver2.19.exe", "chromedriver.exe")
    elif version <= 4302357.0:
        copy_file("chromedriver2.18.exe", "chromedriver.exe")
