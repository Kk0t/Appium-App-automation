# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai
from math import  floor
import subprocess
import os
import re
from common.common_config import CommonConfig


class ApkUtil():
    def __init__(self):
        pwd = os.getcwd()
        father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        self.apkpath = father_path + CommonConfig.PATH['apk']
        print("path:" + self.apkpath)
        if CommonConfig.SYSTEM_NAME == "WINDOWS":
            self.cmd_find = "findstr"
        elif CommonConfig.SYSTEM_NAME == "UNIX":
            self.cmd_find = "grep"

    # 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath)/(1024*1000))
        return str(size) + "M"

    # versionName
    def get_apk_versionName(self):
        cmd = "aapt dump badging " + self.apkpath + " | %s package"% self.cmd_find
        info = self.get_apk_info(cmd, 9, -1)
        list = info.strip('=').split(' ')
        return eval(list[2].split('=')[1])


    # versionCode
    def get_apk_versionCode(self):
        cmd = "aapt dump badging " + self.apkpath + " | %s package"% self.cmd_find
        info = self.get_apk_info(cmd, 9, -1)
        list = info.strip('=').split(' ')
        return eval(list[1].split('=')[1])

    # packageName
    def get_apk_packageName(self):
        cmd = "aapt dump badging " + self.apkpath + " | %s package" % self.cmd_find
        info = self.get_apk_info(cmd, 9, -3)
        compile_packageName = re.compile("name='(.*?)'")
        return compile_packageName.findall(info)[0]


    #得到应用名字
    def get_apk_name(self):
        cmd = "aapt dump badging " + self.apkpath + " | %s application-label:" % self.cmd_find
        info = self.get_apk_info(cmd, 0, -1)
        list = info.split(':')
        return eval(list[1])

    # 得到app的详细信息
    def get_apk_info(self, commond, start, end): #
        result = ""
        p = subprocess.Popen(commond, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output[start:end]
        return result.decode(encoding = 'utf-8',errors = 'ignore')

    def getAppBaseInfo(self,parm_aapt_path, parm_apk_path):

        get_info_command = "%s dump badging %s" % (parm_aapt_path, parm_apk_path)  # 使用命令获取版本信息  aapt命令介绍可以相关博客
        output = os.popen(get_info_command).read()  # 执行命令，并将结果以字符串方式返回
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(
            output)  # 通过正则匹配，获取包名，版本号，版本名称
        if not match:
            print
            output
            raise Exception("can't get packageinfo")

        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)
        return  packagename


if __name__ == '__main__':
    ai = ApkUtil()
    # apk_info1 = ai.get_apk_version()
    # print(ai.get_apk_packageName())
    # print(ai.get_apk_versionName())
    # print(ai.get_apk_versionCode())
    print(ai.get_apk_name())


