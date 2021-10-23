#!/usr/bin/env python
# encoding: utf-8
# @author: yangpei
# @file: logger.py
# @time: 2021/9/22 18:51
import logging

from config_data.readPath import logs_path


def get_logger(name='root',
               logger_level='DEBUG',
               stream_level='DEBUG',
               file=None,
               file_level='INFO',
               ftm='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
               ):
    logger = logging.getLogger(name)
    # 设置logging的等级
    logger.setLevel(logger_level)
    # handler = logging.FileHandler(file, encoding='utf-8')

    # 设置写入的日志格式
    fmt_obj = logging.Formatter(ftm)

    # 将日志输出到屏幕上，写入到文件中
    stream_handler = logging.StreamHandler()
    # 设置日志格式# 设置stream_handler的的等级
    stream_handler.setLevel(stream_level)
    stream_handler.setFormatter(fmt_obj)
    logger.addHandler(stream_handler)

    # 判断是否有传文件，如果有就初始化file_handler,如果没有文件就创建文件
    if file:
        file_handler = logging.FileHandler(file, encoding='utf-8')
        # 设置headler的等级
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
        # 设置日志格式
        file_handler.setFormatter(fmt_obj)

    return logger


# 传入file的文件绝对路径（读取path_common文件中的路径）
log = get_logger(file=logs_path)
