# -*- coding: utf-8 -*-

# @Time  : 2019/4/29

# @Author : Randolph Lu

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESS_KEY_ID = 'LTAImqe*****'
ACCESS_KEY_SECRET = '******KZz3f58Q3RYJ*******'


def send_verify_sms(mobile, params=None):
    client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', 'cn-hangzhou')
    request.add_query_param('PhoneNumbers', mobile)
    request.add_query_param('SignName', 'Akso预约平台')
    request.add_query_param('TemplateCode', 'SMS_164506483')
    if params is not None:
        request.add_query_param('TemplateParam', params)

    response = client.do_action_with_exception(request)
# python2:  print(response)
    return json.loads(str(response, encoding="utf-8"))
