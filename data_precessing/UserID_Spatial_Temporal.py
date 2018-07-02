#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 处理一批电信数据，获取用户ID，以及ID对应的时空信息
# 时空信息按照时间序列排列
# 期望获得格式为一个字典
# 每行 UserID:xx, Date:xx,Time:xx,lat:xx,lon,xx
# 读入文件路径为G:\qoidd\qhoidd\2017XXXX\part-r-000YY
# XXXX代表月份和日期 YY代表00-11的压缩包名称
# 单个文件每行的格式如下
# str1	str2 opt1	20170610190744	lon	lat	opt2
# str1 str2 拨出手机号1（哈希后） 接受手机号（哈希后） opt1（通话/短信符号1） 时间 经度 纬度 opt1（通话/短信符号2）
# 程序基本思路
# 分别循环每个文件
# 建立字典 主key为 userID 即str1
# 子字典 子key1 为“time” 内容为list 保存 时间
#  子key2 为“lat” 内容为list 保存 lat
#  子key3 为“lon” 内容为list 保存 lon
# 读取完毕全部文件后 一起输出即可
# 本程序可参考点
# 1 多层字典 两层字典 最后是一层是list或者单个数值
# 2 中文文本读入处理
# 3 多层文件夹读入处理


import os
import json
import codecs
from collections import defaultdict
#遍历文件夹
def iter_files(rootDir):
    #遍历根目录

    data_dict = defaultdict(lambda: defaultdict(int))

    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file)
            print(file_name)
            if("_SUCCESS" in file_name):
                continue
            data_dict = process(file_name,data_dict)
        for dirname in dirs:
            #递归调用自身,只改变目录名称
            iter_files(dirname)

    with open('jsonfile.json', 'w') as f:  # 文件编码JSON数据,写JSON数据
        json.dump(data_dict, f)

# 核心文件处理代码
def process(file_name,data_dict):
    f1 = codecs.open(file_name, 'r', encoding='utf-8')# 必须事先知道文件的编码格式，这里文件编码是使用的utf-8
    for line in f1:
        temp_str = line.strip().split('\t')
        data_dict.setdefault(temp_str[0])#user ID

        time_list=[]

        data_dict[temp_str[0]].setdefault(time,list)
        data_dict[temp_str[0]].temp_str[3]
        lon = temp_str[4]
        lat = temp_str[5]



    return data_dict




if __name__ == '__main__':
    filePath = "G:\\qoidd\\qhoidd\\"
    iter_files(filePath)






