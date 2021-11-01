# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
import os, time

from appium.webdriver.common.touch_action import TouchAction

from common.common_appium_driver import CommonAppiumDriver
from util.aipocr_util import OcrUtil
from common.common_config import CommonConfig
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *  # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from util.baiduApiOcr_util import BaiduApiOcr

CommonConfig.DRIVER = CommonAppiumDriver().get_driver()


def get_new_list_len(locator):
    '''
    :param locator: ("id","xxx")
    :param timeout: 10s
    :return: len
    '''
    elements = WebDriverWait(CommonConfig.DRIVER, CommonConfig.TIMEOUT).until(
        EC.presence_of_all_elements_located(locator))
    return len(elements)


def find_element(locator):
    element = WebDriverWait(CommonConfig.DRIVER, CommonConfig.TIMEOUT).until(EC.visibility_of_element_located(locator))
    return element


def find_elements(locator: object) -> object:
    elements = WebDriverWait(CommonConfig.DRIVER, CommonConfig.TIMEOUT).until(
        EC.visibility_of_any_elements_located(locator))
    return elements


def click(locator):
    '''
    点击操作
    Usage:
    locator = ("id","xxx")
    driver.click(locator)
    '''
    element = find_element(locator)
    element.click()

def clicks(locator, index):
    '''
    点击操作
    Usage:
    locator = ("id","xxx")
    driver.click(locator)
    '''
    elements = find_elements(locator)
    elements[index].click()

def send_keys(locator, text):
    '''
    发送文本，清空后输入
    Usage:
    locator = ("id","xxx")
    driver.send_keys(locator, text)
    '''
    element = find_element(locator)
    element.clear()
    element.send_keys(text)

def send_key(locator, index, text):
    '''
    发送文本，清空后输入，适用于elements
    '''
    elements = find_elements(locator)
    elements[index].clear()
    elements[index].send_keys(text)


def is_text_in_element(locator, text, timeout=10):
    '''
    判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
    result = driver.text_in_element(locator, text)
    '''
    try:
        result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
    except TimeoutException:
        print("元素没定位到：" + str(locator))
        return False
    else:
        return result


def is_text_in_value(locator, value, timeout=10):
    '''
    判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
    result = driver.text_in_element(locator, text)
    '''
    try:
        result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(
            EC.text_to_be_present_in_element_value(locator, value))
    except TimeoutException:
        print("元素没定位到：" + str(locator))
        return False
    else:
        return result


def is_title(title, timeout=10):
    '''判断title完全等于'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.title_is(title))
    return result


def is_title_contains(title, timeout=10):
    '''判断title包含'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.title_contains(title))
    return result


def is_selected(locator, timeout=10):
    '''判断元素被选中，返回布尔值,'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.element_located_to_be_selected(locator))
    return result


def is_selected_be(locator, selected=True, timeout=10):
    '''判断元素的状态，selected是期望的参数true/False
    返回布尔值'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(
        EC.element_located_selection_state_to_be(locator, selected))
    return result


def is_alert_present(timeout=10):
    '''判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)
    没有返回False'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 3).until(EC.alert_is_present())
    return result


def is_visibility(locator: object) -> object:
    '''元素可见返回本身，不可见返回Fasle'''
    '''元素可见返u回Tre，不可见返回Fasle'''
    try:
        WebDriverWait(CommonConfig.DRIVER, CommonConfig.TIMEOUT).until(
            EC.visibility_of_any_elements_located(locator))
        return True
    except TimeoutException:
        return False


def is_invisibility(locator, timeout=10):
    '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
    '''元素不可见返回True，可见返回Fasle'''
    try:
        WebDriverWait(CommonConfig.DRIVER, timeout).until(EC.invisibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def is_clickable(locator, timeout=10):
    '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.element_to_be_clickable(locator))
    return result


def is_located(locator, timeout=10):
    '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
    result = WebDriverWait(CommonConfig.DRIVER, timeout, 1).until(EC.presence_of_element_located(locator))
    return result


def move_to_element(locator):
    '''
    鼠标悬停操作
    Usage:
    locator = ("id","xxx")
    driver.move_to_element(locator)
    '''
    element = find_element(locator)
    ActionChains(CommonConfig.DRIVER).move_to_element(element).perform()


def back():
    """
    Back to old window.
    Usage:
    driver.back()
    """
    CommonConfig.DRIVER.back()


def forward():
    """
    Forward to old window.
    Usage:
    driver.forward()
    """
    CommonConfig.DRIVER.forward()


def close():
    """
    Close the windows.
    Usage:
    driver.close()
    """
    CommonConfig.DRIVER.close()


def quit():
    """
    Quit the driver and close all the windows.
    Usage:
    driver.quit()
    """
    CommonConfig.DRIVER.quit()


def get_title():
    '''获取title'''
    return CommonConfig.DRIVER.title


def get_text(locator):
    '''获取文本'''
    element = find_element(locator)
    return element.text

def get_texts(locator, index):
    '''获取文本'''
    elements = find_elements(locator)
    return elements[index].text


def get_attribute(locator, name):
    '''获取属性'''
    element = find_element(locator)
    return element.get_attribute(name)


def js_execute(js):
    '''执行js'''
    return CommonConfig.DRIVER.execute_script(js)


def js_focus_element(locator):
    '''聚焦元素'''
    target = find_element(locator)
    CommonConfig.DRIVER.execute_script("arguments[0].scrollIntoView();", target)


def js_scroll_top():
    '''滚动到顶部'''
    js = "window.scrollTo(0,0)"
    CommonConfig.DRIVER.execute_script(js)


def js_scroll_end():
    '''滚动到底部'''
    js = "window.scrollTo(0,document.body.scrollHeight)"
    CommonConfig.DRIVER.execute_script(js)


def select_by_index(locator, index):
    '''通过索引,index是索引第几个，从0开始'''
    element = find_element(locator)
    Select(element).select_by_index(index)


def select_by_value(locator, value):
    '''通过value属性'''
    element = find_element(locator)
    Select(element).select_by_value(value)


def select_by_text(locator, text):
    '''通过文本值定位'''
    element = find_element(locator)
    Select(element).select_by_value(text)


def getSize():
    """获得机器屏幕大小x,y
    :return: x, y
    """
    x = CommonConfig.DRIVER.get_window_size()['width']
    y = CommonConfig.DRIVER.get_window_size()['height']
    return (x, y)


def swipeUp(t):
    """屏幕向上滑动
    :param t: 滑动时间(ms)
    """
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.8)  # 起始y坐标
    y2 = int(l[1] * 0.2)  # 终点y坐标
    CommonConfig.DRIVER.swipe(x1, y1, x1, y2, t)


def swipeDown(t):
    """屏幕向下滑动
    :param t: 滑动时间(ms)
    """
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.2)  # 起始y坐标
    y2 = int(l[1] * 0.8)  # 终点y坐标
    CommonConfig.DRIVER.swipe(x1, y1, x1, y2, t)


def swipLeft(t):
    """屏幕向左滑动
    :param t: 滑动时间(ms)
    """
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    CommonConfig.DRIVER.swipe(x1, y1, x2, y1, t)


def swipRight(t):
    """屏幕向右滑动
    :param t: 滑动时间(ms)
    """
    l = getSize()
    x1 = int(l[0] * 0.1)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    CommonConfig.DRIVER.swipe(x1, y1, x2, y1, t)


def long_press(locator, index):
    '''长按元素
    :param locator:
    :return:
    '''
    TouchAction(CommonConfig.DRIVER).long_press(find_elements(locator)[index]).wait(3000).perform()


def move_to(locator, x, y):
    '''移动元素
    :param locator:
    :return:
    '''
    TouchAction(CommonConfig.DRIVER).long_press(find_elements(locator)[x]).move_to(
        find_elements(locator)[y]).release().perform()


def switch_to_webview():
    context = CommonConfig.DRIVER.contexts
    CommonConfig.DRIVER.switch_to.context(context[1])


def get_current_context():
    return CommonConfig.DRIVER.current_context

def get_press_keycode(x):
    """
    手机事件  回车code=66
    具体参考：https://blog.csdn.net/u013250071/article/details/89437085
    """
    time.sleep(3)
    CommonConfig.DRIVER.press_keycode(x)



def take_screenShot(name):
    '''
    method explain:获取当前屏幕的截图
    parameter explain：【name】 截图的名称
    Usage:
    device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
    '''
    day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    fq = "..\\..\\screenShots\\" + day
    # fq =os.getcwd()[:-4] +'screenShots\\'+day    #根据获取的路径，然后截取路径保存到自己想存放的目录下
    tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    type = '.png'
    filename = ""
    if os.path.exists(fq):
        filename = fq + "\\" + tm + "_" + name + type
    else:
        os.makedirs(fq)
        filename = fq + "\\" + tm + "_" + name + type
        # c = os.getcwd()
        # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
    CommonConfig.DRIVER.get_screenshot_as_file(filename)
    return filename


def assert_screenshot_text(name, message):
    screenshotpath = take_screenShot(name)
    result = BaiduApiOcr().getWordFromImage(screenshotpath, message)
    return  result

# 通过text查找元素
def find_uiautomator_textClick(text):
    # text = "new UiSelector().text("+str(s)+")"
    CommonConfig.DRIVER.find_element_by_android_uiautomator('text(\"'+text+'\")').click()

# 通过text 模糊查找元素
def find_uiautomator_textContainsClick(text):
    # text = "new UiSelector().text("+str(s)+")"
    CommonConfig.DRIVER.find_element_by_android_uiautomator('textContains(\"'+text+'\")').click()

# 通过text 模糊查找元素
def find_scrollIntoView_textClick(text):
    # text = "new UiSelector().text("+str(s)+")"
    CommonConfig.DRIVER.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text(\"'+text+'\"));').click()