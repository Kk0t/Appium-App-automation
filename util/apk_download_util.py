# -*- coding: utf-8 -*-
import os
import requests
from common.common_config import CommonConfig


def download_apk():
    """下载要测试的apk文件"""
    apkList_url = "http://121.9.213.58/zk_client_version/androidapi/?act=list&passcode=456945"
    download_url = requests.get(apkList_url).json()['data']['packages'][0]['binary']
    r = requests.get(download_url)
    pwd = os.getcwd()
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    path = father_path+CommonConfig.PATH['apk']
    print("path:"+path)
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    with open(path,'wb+') as f:
        f.write(r.content)
        print("下载APK完成")
        f.close()

if __name__ == '__main__':
    download_apk()