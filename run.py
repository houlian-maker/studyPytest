# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/11 17:34
# Tool ：PyCharm

import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-m", "do", "-v", '--alluredir=reports/allure_reports',
                 '--clean-alluredir'])
# 方法一 ： 直接查看
# allure serve reports/allure_reports

# 方法二： 在本地html 查看
# 生成本地html测试报告
# allure generate ./reports/allure_reports -o ./reports/reports -c
# 命令打开html测试报告
# allure open -h 127.0.0.1 -p 8888 ./reports/reports
# split = 'allure' + 'generate' + './reports/allure_reports' + '-o' + './reports/reports' + '-c'
