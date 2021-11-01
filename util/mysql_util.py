# -*- coding: utf-8 -*-
import pymysql
from common.common_config import CommonConfig

# 读取数据库配置信息
host = CommonConfig.MYSQL['host']
user = CommonConfig.MYSQL['user']
password = CommonConfig.MYSQL['password']
port = CommonConfig.MYSQL['port']


def mysql_util(sql):
    """
    :param sql_insert: 操作的数据库语句
    :return:
    """
    # 打开数据库连接
    db = pymysql.connect(host=host, user=user, password=password, port=int(port), charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    try:
        cur.execute(sql)
        # 提交
        db.commit()
        db.close()
        return cur.fetchall()
    except Exception as e:
        print(e)
        # 错误回滚
        db.rollback()
        db.close()
        return None