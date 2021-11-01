# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
import PIL.Image as Image
import cv2


def CropImage4File(filepath, destpath, pa, pb, pc, pd):
    # 裁剪指定位置
    image = cv2.imread(filepath)
    sp = image.shape  # obtain the image shape
    sz_x = sp[0]  # height(rows) of image
    sz_y = sp[1]  # width(colums) of image
    # sz3 = sp[2]#the pixels value is made up of three primary colors, here we do not use
    # 你想对文件的操作
    a = int(sz_x * pa)  # x start
    b = int(sz_x * pb)  # x end
    c = int(sz_y * pc)  # y start
    d = int(sz_y * pd)  # y end
    cropImg = image[a:b, c:d]  # crop the image
    cv2.imwrite(destpath, cropImg)  # write in destination path


def difference(hist1, hist2):
    sum1 = 0
    for i in range(len(hist1)):
        if (hist1[i] == hist2[i]):
            sum1 += 1
        else:
            sum1 += 1 - float(abs(hist1[i] - hist2[i])) / max(hist1[i], hist2[i])
    return sum1 / len(hist1)


def similary_calculate(path1, path2, mode):
    if (mode == 3):  # 感知哈希算法
        img1 = Image.open(path1).resize((8, 8)).convert('1')
        img2 = Image.open(path2).resize((8, 8)).convert('1')
        hist1 = list(img1.getdata())
        hist2 = list(img2.getdata())
        return difference(hist1, hist2)

    # 预处理
    img1 = Image.open(path1).resize((256, 256)).convert('RGB')
    img2 = Image.open(path2).resize((256, 256)).convert('RGB')
    if (mode == 1):  # 直方图的距离计算
        return difference(img1.histogram(), img2.histogram())
    if (mode == 2):  # 分块直方图的距离计算
        sum = 0
        for i in range(4):
            for j in range(4):
                hist1 = img1.crop((i * 64, j * 64, i * 64 + 63, j * 64 + 63)).copy().histogram()
                hist2 = img2.crop((i * 64, j * 64, i * 64 + 63, j * 64 + 63)).copy().histogram()
                sum += difference(hist1, hist2)
                # print difference(hist1, hist2)
        return sum / 16
    return 0
