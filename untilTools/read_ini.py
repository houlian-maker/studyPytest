# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/9/28 17:54
# Tool ：PyCharm

"""
封装读取ini配置文件类
"""
from configparser import ConfigParser


class MyConf:
    def __init__(self, filename=None, encoding="utf8"):
        self.filename = filename
        self.encoding = encoding
        self.conf = ConfigParser()
        self.conf.read(filename, encoding)

    def get_str(self, section, option):
        return self.conf.get(section, option)

    def get_comm_url(self, option):
        return self.conf.get('COMM_URL', option)

    def get_user(self, option):
        return self.conf.get('USER', option)

    def get_open_api(self, option):
        return self.conf.get('OPEN_API', option)
