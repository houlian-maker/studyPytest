# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/12 14:30
# Tool ：PyCharm
import pytest
import json
import requests
import allure


from bizvane.business.comm.bizvane_comm import get_sign
from test_data.read_test_data import get_data
from untilTools.logger import log


@pytest.mark.usefixtures('init_get_token')
@allure.feature("测试")
class TestUrApi:

    @pytest.mark.queryMember
    @allure.title("查询会员数据用例")
    @pytest.mark.parametrize('excel', get_data())
    def test_query_member_info(self, init_get_token, excel):
        with allure.step(excel['case_name']):
            test_url = init_get_token[1] + 'memberInfo'
            body = {
                "wxOpenID": "",
                "mobileTel": json.loads(excel['accpt_name'])['mobileTel'],
                "unionid": "",
                "cardCode": "",
                "brandId": "44"
            }
            log.info("请求参数：%s" % excel)
            headers = get_sign(init_get_token[0], body)
            response = requests.post(url=test_url, data=json.dumps(body), headers=headers)
            print(json.loads(excel['accpt_name'])['mobileTel'])
            assert json.loads(response.content)['code'] == excel['accpt_code']
