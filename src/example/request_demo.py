# coding=utf-8

import requests

# 通过requests.get(url)获取雪球页面涨幅榜的情况
# 1.找到请求地址
# 2.分析请求方法和请求体 、headers
# 3.通过requests访问请求接口 返回值
# 4.断言
url = "https://xueqiu.com/service/v5/stock/screener/screen?category=CN&size=10&order=desc&order_by=deal7d&only_count=0&page=1&_=1553412817831 "
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
# 设置代理 执行代码，在charles中看请求结果数据
proxies = {
    'http':'127.0.0.1:8888',
    'https':'127.0.0.1:8888'
}
# verify设置为false表示忽略证书，因为要请求的地址是https格式，需要ssl证书
res = requests.get(url =url,verify=False,headers=headers,proxies=proxies)
print(res.json())
print("*"*200)
print(res.text)
print("*"*200)
print(res.content)
