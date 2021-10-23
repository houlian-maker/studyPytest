# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/7 22:46
# Tool ：PyCharm


def pytest_configure(config):
    config.addinivalue_line("markers", 'do')
    config.addinivalue_line("markers", 'undo')
    config.addinivalue_line("markers", 'queryMember')
