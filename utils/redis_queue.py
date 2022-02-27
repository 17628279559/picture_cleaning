#!/usr/bin/env python3
# coding=utf-8
#########################################################################
# Author: @maris
# Created Time: May 18  2017 18:55:41 PM CST
# File Name:process_user_job.py
# Description:redis队列
#########################################################################
import sys
import os

# root_path = os.path.dirname(os.path.realpath(__file__))  # 根目录文件用这个
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 一级子目录用这个
sys.path.append(root_path)
import datetime
import redis
import json

# 数据库链接
REDIS_HOST = "........"
REDIS_PORT = 6379
REDIS_DB = 10
REDIS_PW = "........"
rdb = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,
                        db=REDIS_DB,
                        password=REDIS_PW)


class CJsonEncoder(json.JSONEncoder):
    """
    功能：解决datatime字段输不出json格式错误
    来自sql_appbk
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 插入数据,默认插入json字符串格式
def insert_data(db, data):
    rdb.lpush(db, json.dumps(data, cls=CJsonEncoder))
    return 0


# 插入多个数据
def insert_data_list(db, data_list):
    for data in data_list:
        insert_data(db, data)


# 获得队列一个数据(同时删除)
def get_one_data(db):
    data = rdb.rpop(db)
    if data:
        return json.loads(data)
    else:
        return -1


# 获得队列长度
def queue_count(db):
    count = rdb.llen(db)
    return count


# 清空队列
def clear_queue(db):
    while True:
        data = rdb.rpop(db)
        if data:  # 如果队列不为空
            pass
        else:  # 如果队列为空，sleep
            break


def get_redis_connect() -> redis.Redis:
    return rdb


def hash_set(db, key, value):
    """
    hset
    :param db: 队列名
    :param key:
    :param value:
    :return:
    """
    rdb.hset(db, key, value)


def hash_get(db, key) -> [None, str]:
    """
    hget
    如果没有对应的key，返回None，否则返回Str
    :param db:队列名
    :param key:
    :return:
    """
    hash_value_bytes = rdb.hget(db, key)
    if hash_value_bytes is None:
        return None
    else:
        return str(hash_value_bytes, encoding='UTF8')


def test_redis_hget():
    print(hash_get('test_hset', 'aaaaaaa_222222222'))
    print(type(hash_get('test_hset', 'aaaaaaa_222222222')))


if __name__ == "__main__":
    # db = "spider_job_account_temp"
    # data = {"account_id": "abcde"}
    # insert_data(db, data)
    # test_redis_hset()
    # test_redis_hget()
    pass
