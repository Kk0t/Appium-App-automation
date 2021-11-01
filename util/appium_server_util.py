# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 14:54
# @Author  : WuBingTai

import os
import psutil
import urllib.request
import threading
from urllib.error import URLError
from multiprocessing import Process


# readConfigLocal = readConfig.ReadConfig()
class AppiumServerUtil:

    def __init__(self, openAppium, baseUrl):
        self.openAppium = openAppium
        self.baseUrl = baseUrl

    def not_exist_process(sefl,processname):
        pl = psutil.pids()
        for pid in pl:
            if psutil.Process(pid).name() == processname:
                return False
            else:
                return True


    def start_server(self):
        """start the appium server
        :return:
        """
        t = RunServer(self.openAppium)
        p = Process(target=t.start())
        p.start()

    def stop_server(self):
        """stop the appium server
        :return:
        """
        # kill myServer
        os.system('taskkill /f /im node.exe')

    def is_exit_port(self,port):
        results = os.popen('netstat -ano | findstr "%d"' % port, 'r')
        while 1:
            line = results.readline()
            if len(str(line)) > 0:
                flag = True
                break
            else:
                flag = False
                break
        results.close()
        return flag



    def stop_port(self, port):
        """stop the port:
        :return:
        """
        # kill PID
        command_result = ''
        command_result1 = ''
        results = os.popen('netstat -ano | findstr "%d"'%port, 'r')
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        # pid_compile = re.compile("LISTENING       (.*?)\n")
        # pid = pid_compile.findall(command_result)
        pid = command_result.split(' ')[-1].strip('\n')
        if pid:
            print("appium_server 已运行，正在停止，并重新启动")
            result1 = os.popen('taskkill /pid %s /f'%pid)
            while 1:
                line = result1.readline()
                if not line: break
                command_result1+= line
            print(command_result1)

    def is_exit_server(self):
        results = os.popen('tasklist | findstr node.exe', 'r')
        while 1:
            line = results.readline()
            if len(str(line)) > 0:
                flag = True
                break
            else:
                flag = False
                break
        results.close()
        return flag

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = self.baseUrl + "/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


if __name__ == "__main__":

    udid = "03157df31999cb33"
    for i in range(1):
        port = 4723 + i * 2
        # bp = 2251+i*2
        remote = 'http://127.0.0.1:%d/wd/hub' % port
        # openAppium = "appium -p %d -bp %d" % (port, bp)
        openAppium = "appium -p %d -U %s" % (port, udid)
        appium_server = AppiumServerUtil(openAppium, remote)
        appium_server.start_server()  # 启动Appium server
        # appium_server.is_exit_port(port)

