# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 11:19
# @Author  : hjj
# @Site    : 使用requests.post方式测试豆瓣登录接口
# @File    : test_post_login_douban.py

import requests

def test_post_login_douban():
    url = "https://accounts.douban.com/j/mobile/login/basic"
    payload = {"ck":"",
               "name":"18810054187",
               "password": "qwe789",
               "remember": "false",
               "ticket":""
               }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
              }
    res = requests.post(url=url, verify=False, data= payload,headers = headers)
    print(res.json())
    assert  res.json().get("status") == "success"