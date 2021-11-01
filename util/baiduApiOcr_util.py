# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai

from aip import AipOcr


class BaiduApiOcr:

    def __init__(self):
        self.APP_ID = "19520441"
        self.API_KEY = "6bssdo7nyiOHhCPh6TG2FyVQ"
        self.SECRET_KEY = "zgqZYQ5mTEso5lFNLsWwCXCN8Epmqtgz"
        # 初始化文字识别分类器
        self.AIPOCR = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    """ 读取图片 """
    def get_file_content(self,imageFile):
        with open(imageFile, 'rb') as fp:
            return fp.read()

    def getWordFromImage(self,imageFile,text):
        flag = False
        image = self.get_file_content(imageFile)
        result = self.AIPOCR.basicGeneral(image)
        for item in result['words_result']:
            # print(item['words'])
            if item['words'] == text:
                flag = True
                break
            else:
                flag =False
        return  flag


if __name__=="__main__":
    APP_ID='19520441'
    API_KEY='6bssdo7nyiOHhCPh6TG2FyVQ'
    SECRET_KEY='zgqZYQ5mTEso5lFNLsWwCXCN8Epmqtgz'
    obj = BaiduApiOcr()
    imageFile='C:\\git-wordspace\Android-Ztest\\new-zaker-android\\screenShots\\2020-04-20\\test1.jpg'
    result = obj.getWordFromImage(imageFile,"上滑带你去发现")
