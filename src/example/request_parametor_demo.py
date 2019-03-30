# coding=utf-8
import requests

# 通过requests.get(url,params)获取雪球页面涨幅榜的情况
# 资料 http://docs.python-requests.org/en/master/user/quickstart/#response-content


url = "https://xueqiu.com/service/v5/stock/screener/screen"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
payload = {"category": "CN", "size": "10", "order": "desc", "order_by": "deal7d", "only_count": "0", "page": "1",
          "_": "1553412817831"}
res = requests.get(url=url, verify=False, headers=headers, params=payload)
print(res.json())
