#!/usr/bin/env python3
# coding=utf-8
#########################################################################
# Author: @Crystal
# Created Time: Jan 7  2022 18:30:00 PM CST
# File Name: method_2_sdk.py
# Description: 调用百度SDK获取地标类结果信息
# 测试连接：无
#########################################################################
import sys
import json
from aip import AipImageClassify
from conf import *

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_baidu_landmark_sdk_res(local_file):
    '''
    地标识别SDK
    '''

    """ 你的AK SK """
    client = AipImageClassify("..............", "..................", ".......................")

    """ 读取图片 """
    image = get_file_content(local_file)

    """ 调用地标识别 """
    res = client.landmark(image)
    return res

if __name__ == '__main__':
    # Unit Test
    local_file = './images_uncategorized/test_image0.jpg'  # [本地文件]
    res = get_baidu_landmark_sdk_res(local_file)
    print(res)

