# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
import os

def test_zzzz_stop_server():
    """stop the appium server
    :return:
    """
    # kill myServer
    os.system('taskkill /f /im node.exe')

if __name__ == '__main__':
    test_zzzz_stop_server()