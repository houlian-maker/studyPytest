# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/13 10:21
# Tool ：PyCharm
from config_data.readPath import root_dir
from untilTools.read_excels import read_excel

"""
读取excel 测试用例模块
"""


def get_data():
    """读取UR 会员查询数据"""
    excel = read_excel(root_dir + '/test_data/test.xlsx', 'student')
    return excel
