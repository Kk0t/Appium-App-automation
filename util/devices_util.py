# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
import os
import re
from math import ceil


# 得到手机信息
def getPhoneMsg(cmd_log, device):
    os.system('adb -s %s shell cat /system/build.prop >' % device + cmd_log)
    l_list = {}
    with open(cmd_log, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('=')
            # Android 系统，如anroid 4.0
            if (line[0] == 'ro.build.version.release'):
                l_list["release"] = line[1]
                # 手机名字
            if (line[0] == 'ro.product.model'):
                l_list["phone_name"] = line[1]
                # 手机品牌
            if (line[0] == 'ro.product.brand'):
                l_list["phone_model"] = line[1]

    # 删除本地存储的手机信息文件
    if os.path.exists(cmd_log):
        os.remove(cmd_log)
    return l_list


# 得到手机总内存
def get_men_total(cmd_log, device):
    os.system("adb -s %s shell cat /proc/meminfo >" % device + cmd_log)
    men_total = ""
    with open(cmd_log, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('=')
            if line[0]:
                men_total = re.findall(r"\d+", line[0])[0]
                break
    if os.path.exists(cmd_log):
        os.remove(cmd_log)
    return str(ceil(int(men_total) / 1000)) + "M"


# 得到几核cpu
def get_cpu_kel(log, device):
    os.system("adb -s %s shell cat /proc/cpuinfo >" % device + log)
    cpu_kel = 0
    with open(log, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(':')
            if line[0].find("processor") >= 0:
                cpu_kel += 1
    if os.path.exists(log):
        os.remove(log)
    return str(cpu_kel) + "核"


# print(get_cpu_kel("d:\\men.txt"))

# 得到手机分辨率
def get_app_pix(device):
    result = os.popen("adb -s %s shell wm size" % device, "r")
    return result.readline().split("Physical size: ")[1].strip("\n")


def get_cpu_use(device):
    result = os.system("adb -s %s shell top -m 10 -s cpu" % device)
    return result


if __name__ == '__main__':
    device = "9889d5345436474446"
    # get_phone_msg = getPhoneMsg("..\phone.txt")
    # print(get_phone_msg)  # 获取手机信息
    # men_total = get_men_total("..\men_total.txt", device)  # 运行内存
    # print('phone_raw:',men_total)
    # cpu_sum = get_cpu_kel("..\cpu.txt")  # 几核cpu
    # print(cpu_sum)
    # pix = get_app_pix()  # 得到手机分辨率
    # print(pix)
    print(get_cpu_use(device))
