# -*- coding: utf-8 -*-
import re
import subprocess
from common import common_mysql_operate
from common.commonglobal import Global
from util.android_debug_bridge import AndroidDebugBridge


def run_getPer():
    """获取性能数据，写入数据库"""
    pid = "0000"
    while pid == "0000": pid = AndroidDebugBridge().get_PID(Global.DEVICES['udid'])
    top = subprocess.Popen('adb -s %s shell top' % Global.DEVICES['udid'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    while Global.FLAG:
        data = str(top.stdout.readline())
        per_compile = re.compile("%s.*com.myzaker" % pid)
        per_list = per_compile.findall(data)
        if len(per_list) > 0:
            per = per_list[0].split()
            common_mysql_operate.devices_per(Global.DEVICES['udid'], per[8], per[9], '')
