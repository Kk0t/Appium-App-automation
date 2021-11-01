# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
from common.common_operate import *
from selenium.webdriver.common.by import By


class IndexPage:
    mainTabSearch = (By.ID, "com.pmc.rmt:id/mainTabSearch")  # 搜索
    bottomTabIcon = (By.ID, "com.pmc.rmt:id/bottomTabIcon")  # 底部tab
    topTabTitle = (By.ID, "com.pmc.rmt:id/topTabTitle")  # 顶部tab
    columnsItemPic = (By.ID, "com.pmc.rmt:id/columnsItemPic")  # 专栏图片
    mssItemIcon = (By.ID, "com.pmc.rmt:id/mssItemIcon")  # 媒体号icon
    mssItemTitle = (By.ID, "com.pmc.rmt:id/mssItemTitle")  # 媒体号Title
    mssMore = (By.ID, "com.pmc.rmt:id/mssMore")  # 媒体号更多

    # 点击底部tab
    def click_bottom_Tab_icon(self, index):
        clicks(self.bottomTabIcon, index)

    # 点击顶部tab
    def click_top_tab_title(self, index):
        clicks(self.topTabTitle, index)
