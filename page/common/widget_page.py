# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
from common.common_operate import *
from selenium.webdriver.common.by import By


# 弹窗组件
class WidgetPage:
    md_root = (By.ID, "com.pmc.rmt:id/md_root")  # 升级弹框
    md_button_negative = (By.ID, "com.pmc.rmt:id/md_button_negative")  # 取消

    # 点击取消/升级
    def click_md_button_negative(self, index):
        clicks(self.md_button_negative, index)
