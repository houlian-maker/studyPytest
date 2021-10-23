# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/12 16:00
# Tool ：PyCharm
import random
import time

import allure
import pytest

from bizvane.business.comm.bizvane_comm import get_open_access_token
from config_data.readPath import uat_config
from untilTools.read_ini import MyConf


@pytest.fixture()
def init_get_token():
    with allure.step('公用前置条件:获取签名'):
        my_conf = MyConf(uat_config)
        ur_appkey = my_conf.get_open_api('ur_appsecret')
        ur_url = my_conf.get_comm_url('ur_url')
    # 时间戳
    number = round(random.random() * 1000000)
    headers = {
        'bizvane-nonce': str(number),
        'bizvane-timestamp': str(int(round(time.time() * 1000))),
        'bizvane-appsecret': ur_appkey,
        "bizvane-access-token": get_open_access_token('ur')
    }
    yield headers, ur_url
