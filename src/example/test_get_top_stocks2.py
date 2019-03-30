# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 10:43
# @Author  : hjj
# @Site    : 
# @File    : test_top_stocks2.py

#练习题2
#通过requests.get 方式访问 https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1&_=1553913322345
#用pytest参数化方式实现，不同size的顺序和倒序排序，例如(10,顺序) (20,倒序)
#断言测试是否通过

import requests
import pytest
@pytest.mark.parametrize("size,orderby",[(10,"asc"),(20,"desc")])
def test_get_top_stocks2(size,orderby):
    url = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
    payload = {"type": "sha", "order_by": "percent",
              "order": orderby, "size": str(size),
              "page": "1", "_": 1553418305938}
    res = requests.get(url=url, verify=False, headers=headers, params=payload)
    print(res.json())
    assert  res.status_code == 200