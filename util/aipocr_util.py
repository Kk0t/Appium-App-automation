# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai

from aip import AipOcr

class OcrUtil:


    def __init__(self, imgfile):
        self.IMGFILE = imgfile
        self.APP_ID = "11700559"
        self.API_KEY = "xH6y0SlGxx2cy0pZ6njYyAbf"
        self.SECRET_KEY = "vWSwaM9pEiuPlsWCe4BmznyDjYqKbtgn"
        # 初始化文字识别分类器
        self.AIPOCR = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def ocrGeneral(self):
        """百度AI图像识别文字"""
        fp = open(self.IMGFILE, 'rb')
        try:
            fp.read()
            options = {
                'detect_direction': 'true',
                'language_type': 'CHN_ENG',
            }
            # 调用通用文字识别接口
            result = self.AIPOCR.basicGeneral(fp, options)
            words_result = result['words_result']
            words = ""
            for i in range(len(words_result)):
                words = words + words_result[i]['words']
                # print(">>>>图像识别文字结果：", words_result[i]['words'])
            return words
        finally:
            fp.close()



if __name__ == '__main__':
    pass
