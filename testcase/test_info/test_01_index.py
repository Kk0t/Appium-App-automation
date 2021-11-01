# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 15:25
# @Author  : WuBingTai
import unittest
import logging
import nose
from nose.tools import *
from common.common_operate import *
from page.common.index_page import IndexPage
from page.common.widget_page import WidgetPage


class TestHotTopTab(unittest.TestCase):
    log = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        cls.index = IndexPage()
        cls.widget = WidgetPage()

    # @nose.allure.feature('资讯Tab')
    # @nose.allure.story('热点Tab-检查热点下拉刷新')
    def test_01_click_md_button_negative(self):
        try:
            self.widget.click_md_button_negative(0)
            assert_true(is_visibility(self.index.bottomTabIcon))
            self.index.click_top_tab_title(1)
        except TimeoutException as e:
            take_screenShot(u"测试")
            logging.error(e)
            assert_false(True)



    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        get_press_keycode(4)
