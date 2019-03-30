# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 9:44
# @Author  : hjj
# @Site    : 
# @File    : xueqiu_mock.py
# @Software: PyCharm
from flask import Flask
from flask_restful import Resource, Api

#以下简单几行代码，即可拉起一个网站
# 在浏览器中输入 http://127.0.0.1:5000/  即可
# 配置charles中--转发请求到其他服务 Map remote ,可以将请求地址转发到本地服务
app = Flask(__name__)
api = Api(app)

class HotStock(Resource):
    def get(self):
        return {"data":{"items":[{"type":10,"code":"NCTY","name":"NO1","value":7325,"increment":89,"percent":-12.3,"current":2.2101,"chg":-0.3099}, ]},"error_code":0,"error_description":""}

api.add_resource(HotStock, '/')

if __name__ == '__main__':
    app.run(debug=True)