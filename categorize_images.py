# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2022/1/7 18:30
# @FileName: categorize_images.py
# @Desc    : Picture 2 classification, architectural or non architectural
import sys
import os
import shutil
from method_1_api_request import get_baidu_landmark_api_res
from method_2_sdk import get_baidu_landmark_sdk_res
from utils import redis_queue

def get_file_name(local_file):
    fpath, fname = os.path.split(local_file)
    return fname

def catgorize_images(local_file,target_path):

    # 获取识别结果，此处使用SDK调用，也可使用API
    # res = get_baidu_landmark_api_res(local_file)
    res = get_baidu_landmark_sdk_res(local_file)
    original_file_name = get_file_name(local_file)
    # 根据结果对文件进行分类
    if type(res) == dict:
        if 'result' in res:
            if 'landmark' in res['result']:
                if res['result']['landmark']:
                    try:
                        image_landmark_name = res['result']['landmark']
                        target = target_path + 'landmark_images/' + image_landmark_name + "_" + original_file_name
                        # 如需保留原文件夹信息，可使用copyfile
                        # shutil.copyfile(local_file,target)
                        # 如不需保留原文件夹信息，可使用move直接分拆
                        shutil.move(local_file, target)
                    except Exception as e:
                        print('move file to landmark_image folder FALSE ', e)
                else:
                    try:
                        target = target_path + 'unknown_images/' + original_file_name
                        # 如需保留原文件夹信息，可使用copyfile
                        # shutil.copyfile(local_file, target)
                        # 如不需保留原文件夹信息，可使用move直接分拆
                        shutil.move(local_file, target)
                    except Exception as e:
                        print('move file to unknown_images folder FALSE ', e)
    else:
        print('调用API 或 SDK 失败')
        print(res)

def run():
    target_path = '/tmp/ossfs_02/xu/cleanArchitectures/zhao/'
    while True:
        data_dict = redis_queue.get_one_data('Classification_of_architectural_pictures_123')
        if data_dict == -1:
            print('没有读取到数据，程序退出')
            break
        path = data_dict['file_path'].replace("ossfs_02","ossfs_01")
        print(f'将移动:{path}')

        catgorize_images(path, target_path)


if __name__ == '__main__':
    run()

