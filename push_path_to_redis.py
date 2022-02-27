# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2022/2/8 16:44
# @FileName: push_path_to_redis.py
# @Desc    : push needed data to redis
import os
import sys
from utils import redis_queue

def file_path(file_dir):
    result = []
    x = True
    for root, dirs, files in os.walk(file_dir):
        if x:
            x = False
        else:
            for item in files:
                path = root + "/" + item
                result.append(path.replace("\\","/"))  # 所有文件
    return result


def from_mysql(db_name):
    # 找叶子节点

    fp = file_path("/tmp/ossfs_02/out/image1/xu/Architectures/")
    fp.extend(file_path("/tmp/ossfs_02/out/image2/xu/Architectures/"))
    fp.extend(file_path("/tmp/ossfs_02/out/image3/xu/Architectures/"))
    
    for item in fp:
        print(item)
        data = {
            'file_path': item,
        }
        redis_queue.insert_data(db_name, data)
    


def main():
    db_name = 'Classification_of_architectural_pictures_123'
    from_mysql(db_name)


if __name__ == '__main__':
    main()
