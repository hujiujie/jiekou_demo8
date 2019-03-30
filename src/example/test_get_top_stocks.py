# coding=utf-8
import requests
import pytest

# 雪球行情页面，涨幅榜 ，断言第一个股票的涨跌幅大于9.9
# 参数化size ，size是返回的股票的数量
@pytest.mark.parametrize("size",[3,-1,10,100])
def test_get_top_stocks(size):
    url = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
    payload = {"type": "sha", "order_by": "percent",
              "order": "desc", "size": str(size),
              "page": "1", "_": 1553418305938}
    res = requests.get(url=url, verify=False, headers=headers, params=payload)
    print(res.json())
    # 返回数据是字典时，可以用get方法获取字典中的值
    no_one = res.json().get("data").get("list")[0].get("percent")
    print(no_one)
    assert no_one > 9.9