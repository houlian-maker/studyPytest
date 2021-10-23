# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/10 14:24
# Tool ：PyCharm
import base64
import hashlib
import json
import operator

import requests

from config_data.readPath import uat_config
from untilTools.read_ini import MyConf

# 读取配置文件
my_conf = MyConf(uat_config)
uat_base_url = my_conf.get_comm_url('uat_base_url')
accountCode = my_conf.get_user('uat_username')
hashPassword = my_conf.get_user('uat_password')


def get_stage_token(sys_company_id):
    r"""根据企业id 获取中台token
    :param sys_company_id : 企业 ID
    """

    # 获取中台登录验证码
    verification_code_url = uat_base_url + 'centerstage.api/verificationCode'
    verification_code_body = {}
    verification_code_response = requests.post(url=verification_code_url,
                                               data=verification_code_body)
    verification_key = json.loads(verification_code_response.content)['data']['verifKey']
    verification_code = verification_key[0:4]

    # 获取登录接口token
    uat_login_url = uat_base_url + 'centerstage.api/login'
    uat_login_body = {'verifKey': verification_key,
                      'accountCode': accountCode,
                      'hashPassword': hashPassword,
                      'verifCode': verification_code,
                      'sysCompanyId': sys_company_id}
    uat_login_response = requests.post(url=uat_login_url, data=uat_login_body)
    login_token = json.loads(uat_login_response.content)['data']['stageToken']
    stage_token = {'stageToken': login_token}

    return stage_token


def get_open_access_token(company_name):
    r"""开发平台获取token

    :param company_name : 企业名称
    """

    token_url = 'http://openapi.bizvane.cn/oauth2/accessToken'
    header = {
        'Accept-Encoding': 'gzip, deflate, br',
        "Accept": "*/*",
        "Content-Type": "application/json"
    }
    body = {
        "appKey": my_conf.get_str('OPEN_API', company_name + '_appkey'),
        "appSecret": my_conf.get_str('OPEN_API', company_name + '_appsecret')
    }
    data = json.dumps(body)
    response = requests.post(token_url, data=data, headers=header)
    return json.loads(response.content).get('accessToken')


def getOrderObject(param):
    return dict(sorted(param.items(), key=operator.itemgetter(0)))


def get_sign(headers, body):
    """生成签名"""
    row_body = {**headers, **body}
    sorted_dict = dict(sorted(row_body.items(), key=operator.itemgetter(0)))
    data_array = list()
    for key, value in sorted_dict.items():
        if isinstance(value, list):
            arr = []
            for valuelement in value:
                arr.append(getOrderObject(valuelement))
            data_array.append(key + '=' + json.dumps(arr))
        # 如果传进来空字符串,toString的时候会有问题
        elif isinstance(value, str) and len(value) == 0:
            continue
        else:
            data_array.append(key + '=' + str(value))
    raw_data = '&'.join(data_array)
    byte_data = base64.b64encode(bytes(raw_data, 'utf-8'))
    hl = hashlib.md5()
    hl.update(byte_data)
    sign = hl.hexdigest()
    headers.setdefault('bizvane-signature', sign)
    headers.setdefault('Content-Type', 'application/json')
    headers.pop('bizvane-appsecret')
    return headers
