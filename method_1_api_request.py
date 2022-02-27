#!/usr/bin/env python3
# coding=utf-8
#########################################################################
# Author: @Crystal
# Created Time: Jan 7  2022 18:30:00 PM CST
# File Name: method_1_api_request.py
# Description: 调用百度API获取地标类结果信息
# 测试连接：无
#########################################################################
import sys
import requests
import base64
from get_token import fetch_token


def get_baidu_landmark_api_res(local_file):
    '''
    地标识别API
    '''
    # 调用地标识别API：
    # api 调取参数 1
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token

    # api 调取参数 2
    # 二进制方式打开图片文件
    f = open(local_file, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}

    # api 调取参数 3
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # 获取api request 结果
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()
    else:
        return {}

if __name__ == '__main__':
    # Unit Test
    local_file = './images_uncategorized/test_image0.jpg'  # [本地文件]
    res = get_baidu_landmark_api_res(local_file)
    print(res)

