# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/9/28 17:58
# Tool ：PyCharm

"""
读取路径
"""
import os


# 获取当前文件的绝对路径
current_path = os.path.abspath(__file__)

# config文件夹路径
config_dir = os.path.dirname(current_path)

# 项目根目录
root_dir = os.path.dirname(config_dir)

# uat.ini 目录
uat_config = os.path.join(config_dir, 'uat.ini')

# 日志路径
logs_path = os.path.join(config_dir, 'printLogs')
