# coding: utf-8
# Team : BIZVANE BEST TESTER
# Author：HouLian
# Date ：2021/10/10 16:19
# Tool ：PyCharm
import allure
import pytest
import requests
import json

from bizvane.business.comm.bizvane_comm import get_stage_token
from config_data.readPath import uat_config
from untilTools.read_ini import MyConf


@pytest.fixture()
def init_url_token():
    with allure.step("登录获取token"):
        my_conf = MyConf(uat_config)
        uat_center_stage_url = my_conf.get_comm_url('uat_center_stage_url')
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, get_stage_token(1))
        yield uat_center_stage_url, session


class TestCenterStage:

    @pytest.mark.do
    @pytest.mark.usefixtures('init_url_token')
    def test_get_brand_info(self, init_url_token):
        with allure.step("获得首页品牌信息"):
            test_url = init_url_token[0] + 'brand/getBrandListByAccountId'
            response = init_url_token[1].post(test_url, data={})
            # 将json数据格式化输出到控制台
            json_str = json.dumps(json.loads(response.content),
                                  indent=2,
                                  ensure_ascii=False)
            print(json_str)
            assert json.loads(response.content)['code'] == 0
            assert json.loads(response.content)['message'] == '操作成功！'

    @pytest.mark.do
    @pytest.mark.usefixtures('init_url_token')
    def test_get_upload_image(self, init_url_token):
        with allure.step("获取首页图片"):
            test_url = init_url_token[0] + 'uploadImg/getUploadImg'
            response = init_url_token[1].post(url=test_url, data={})
            assert json.loads(response.content)['code'] == 0
