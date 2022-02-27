# encoding:utf-8
import json
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus
from conf import *

# [调用鉴权接口获取的token], token有效期30天
# 获取参考教程：https://cloud.baidu.com/video-center/video.html?id=639
# step1： 创建应用获取 AK SK
# step2：
# # method 1: postman 获取，参见视频教程步骤
# # method 2: api 获取 https://cloud.baidu.com/apiexplorer/index.html?Product=GWSE-nmhroEsyriA&Api=GWAI-ZrbC4DkR2rP
# # method 3: 通过如下fuc获取

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

"""
    获取token
"""
def fetch_token():
    params = {'grant_type': '...........',
              'client_id': "...............",
              'client_secret': "......................."}
    post_data = urlencode(params).encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)

    result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()