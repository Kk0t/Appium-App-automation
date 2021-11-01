# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai

import os, re


class ADBUtil:

    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
        pass

    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        flag = [device for device in devices if len(device) > 2]
        if flag:
            return True
        else:
            return False

    # 获取已连接设备列表
    def get_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, device, remote, local):
        result = self.call_adb("-s %s pull %s %s" % (device, remote, local))
        return result

    # 同步更新 很少用此命名
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # 从指定设备的打开app，并计算启动时间
    def open_app(self, device, packagename, activity):
        result = self.call_adb("-s %s shell am start -W %s/%s" % (device, packagename, activity))
        # check = result.partition('\n')[2]
        return result

    # 安装apk至指定设备
    def install_apk(self, device, apk):
        result = self.call_adb("-s %s install %s" % (device, apk))
        return result

    # 从指定设备卸载apk
    def uninstall_apk(self, device, packagename):
        result = self.call_adb("-s %s uninstall %s" % (device, packagename))
        return result

    # 从指定设备强制关闭APP
    def force_stop_app(self, device, packagename):
        result = self.call_adb("-s %s shell am force-stop %s" % (device, packagename))
        return result

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep " + pkg_name)
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]

    def get_packageName(self, device):
        "adb shell pm list packages"
        result = self.call_adb("-s %s shell pm list packages" % device)
        return result

    def get_phonemodel(self, device):
        """获取手机型号信息"""
        resullt = self.call_adb("-s %s shell getprop ro.product.model" % device)
        return resullt

    def get_phonerelease(self, device):
        """获取手机系统版本"""
        resullt = self.call_adb("-s %s shell getprop ro.build.version.release" % device)
        return resullt

    def get_PID(self, device):
        result = self.call_adb("-s %s shell ps | findstr com.myzaker.ZAKER_Phone" % device)
        pid_compile = re.compile(" .*com.myzaker.ZAKER_Phone\n")
        pidlist = pid_compile.findall(result)
        if len(pidlist) > 0:
            pid = pidlist[0].split()[0]
            return pid
        else:
            return '0000'

    # def get_phone_cpu(self, device):
    #     """获取手机系统版本"""
    #     resullt = self.call_adb("-s %s shell dumpsys cpuinfo | findstr com.myzaker.ZAKER_Phone" %  device)
    #     return resullt
    #
    # def get_app_mem(self, device):
    #     """获取手机系统版本"""
    #     result = self.call_adb("-s %s shell dumpsys meminfo com.myzaker.ZAKER_Phone" %  device)
    #     mem_compile = re.compile("TOTAL:\s*(.*?) ")
    #     # \s*: 匹配任意多个空格
    #     # (.*?) : 非贪婪匹配第一个以空格隔开的值
    #
    #     # result = self.call_adb("-s %s shell top" % device)
    #     # mem_compile = re.compile("(.*)com.myzaker")
    #     men = mem_compile.findall(result)
    #     return men

    def adb_connect(self, device, port):
        # adb无线连接设备调试，首先需要将设备通过USB连接完成端口设定
        ip_compile = re.compile("inet (.*?)/.* scope global wlan0")
        ip = ip_compile.findall(self.call_adb("-s %s shell ip addr" % device))[0]  # 自动获取设备ip
        result_tcpip_port = self.call_adb("-s %s tcpip %s" % (device, port))  # 对应设备设定端口号
        result_connect = self.call_adb("connect %s:%s" % (ip, port))  # 无线连接对应ip
        print(result_tcpip_port)
        print(result_connect)
        return ip  # 返回设备的ip

    def disconnect(self):
        # 断开所有adb无线连接
        result_disconnect = self.call_adb("disconnect")
        print(result_disconnect)

    def get_chromedriver_version(self, device):
        """获取手机自带浏览器的webview版本"""
        result = self.call_adb("-s %s shell dumpsys package com.google.android.webview | findstr versionNam" % device)
        versionName_compile = re.compile("versionName=(.*)")
        versionName = versionName_compile.findall(result)  # 获取webview 的versionName
        print(versionName)
        version = versionName[0].split(".")[0]  # 只取版本名称前面部分，转换为int型
        return int(version)

    def get_devices_ime(self, device):
        """获取手机输入法"""
        result = self.call_adb("-s %s shell ime list -s"% device)
        print(result)
        return result

    def set_devices_ime(self, device):
        """获取手机输入法"""
        result = self.call_adb("-s %s shell ime list -s" % device)
        print(result)
        result2 = self.call_adb("-s %s shell ime set com.sec.android.inputmethod/.SamsungKeypad"% device)

    def get_screencap(self, device):
        result = self.call_adb("-s %s shell /system/bin/screencap -p /sdcard/screenshot.png"%device)
        return result

if __name__ == '__main__':
    # apkfile = r"C:\Users\wenqi\Desktop\ZAKER_v8.2.8-adapt.apk"
    # zaker_package = "com.myzaker.ZAKER_Phone"
    devices = ADBUtil().get_devices()
    # print(devices)
    for device in devices:
        #     package_list = AndroidDebugBridge().get_packageName(device)
        #     if zaker_package in package_list:
        #         AndroidDebugBridge().uninstall_apk(device, zaker_package)
        #     AndroidDebugBridge().install_apk(device, apkfile)
        #     print(CommonADB().get_PID(device))
        result =ADBUtil().get_devices_ime(device)
        print(type(result))
        print(device)
        print(ADBUtil().get_phonerelease(device))
        # ADBUtil().set_devices_ime(device)

