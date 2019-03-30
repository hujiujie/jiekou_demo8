# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 9:41
# @Author  : hjj
# @Site    : 接口返回很多字段,通过schema批量校验返回字段值是否符合预期
# @File    : schema_xueqiu_hq.py


# 雪球行情
# 接口返回很多字段,通过schema 批量校验返回字段值是否符合预期
# 接口地址https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=volume&order=desc&size=10&page=1&_=1553615629225
from jsonschema import validate

schema_stock_zf = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "data",
        "error_code",
        "error_description"
    ],
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "count",
                "list"
            ],
            "properties": {
                "count": {
                    "type": "integer",
                    "default": 0,
                },
                "list": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "symbol",
                            "amount",
                            "chg",
                            "type",
                            "percent",
                            "has_follow",
                            "tick_size",
                            "volume",
                            "current",
                            "volume_ratio",
                            "amplitude",
                            "pb",
                            "current_year_percent",
                            "turnover_rate",
                            "float_market_capital",
                            "name",
                            "market_capital",
                            "pe_ttm",
                            "dividend_yield",
                            "lot_size",
                            "percent5m"
                        ],
                        "properties": {
                            "symbol": {
                                "type": "string",
                                "maxLength":8
                            },
                            "amount": {
                                "type": "integer"
                            },
                            "chg": {
                                "type": "number"
                            },
                            "type": {
                                "type": "integer"
                            },
                            "percent": {
                                "type": "number",
                                "minimum": -5,
                                "maximum": 10,
                                "exclusiveMaximum":True
                            },
                            "has_follow": {
                                "type": "boolean"
                            },
                            "tick_size": {
                                "type": "number"
                            },
                            "volume": {
                                "type": "integer"
                            },
                            "current": {
                                "type": "number"
                            },
                            "volume_ratio": {
                                "type": "number"
                            },
                            "amplitude": {
                                "type": "number"
                            },
                            "pb": {
                                "type": "number"
                            },
                            "current_year_percent": {
                                "type": "number"
                            },
                            "turnover_rate": {
                                "type": "number"
                            },
                            "float_market_capital": {
                                "type": "integer"
                            },
                            "name": {
                                "type": "string"
                            },
                            "market_capital": {
                                "type": "integer"
                            },
                            "pe_ttm": {
                                "type": "number"
                            },
                            "dividend_yield": {
                                "type": "number"
                            },
                            "lot_size": {
                                "type": "integer"
                            },
                            "percent5m": {
                                "type": "number"
                            }
                        }
                    }
                }
            }
        },
        "error_code": {
            "type": "integer",
        },
        "error_description": {
            "type": "string",
        }
    }
}
livevalue = {
    "data": {
        "count": 1458,
        "list": [{
            "symbol": "SH6003520000",
            "amount": 6431629772,
            "chg": 0.48,
            "type": 11,
            "percent": 12,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 437145030,
            "current": 14.3,
            "volume_ratio": 5.24,
            "amplitude": 8.1,
            "pb": 2.395,
            "current_year_percent": 48.19,
            "turnover_rate": 13.44,
            "float_market_capital": 46522645598,
            "name": "浙江龙盛",
            "market_capital": 46522645598,
            "pe_ttm": 12.307,
            "dividend_yield": 1.748,
            "lot_size": 100,
            "percent5m": -0.49
        }, {
            "symbol": "SH601989",
            "amount": 2398055702,
            "chg": -0.33,
            "type": 11,
            "percent": -5.68,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 426974962,
            "current": 5.48,
            "volume_ratio": 1.79,
            "amplitude": 6.71,
            "pb": 1.477,
            "current_year_percent": 28.94,
            "turnover_rate": 2.33,
            "float_market_capital": 100621924562,
            "name": "中国重工",
            "market_capital": 125381266972,
            "pe_ttm": 109.267,
            "dividend_yield": 0.201,
            "lot_size": 100,
            "percent5m": -0.18
        }, {
            "symbol": "SH600010",
            "amount": 671937017,
            "chg": -0.06,
            "type": 11,
            "percent": -3.23,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 368474500,
            "current": 1.8,
            "volume_ratio": 1.1,
            "amplitude": 4.3,
            "pb": 1.579,
            "current_year_percent": 21.62,
            "turnover_rate": 1.16,
            "float_market_capital": 57018980857,
            "name": "包钢股份",
            "market_capital": 82053058766,
            "pe_ttm": 27.734,
            "dividend_yield": 0.278,
            "lot_size": 100,
            "percent5m": -0.55
        }, {
            "symbol": "SH600157",
            "amount": 611113842,
            "chg": -0.1,
            "type": 11,
            "percent": -4.57,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 285726465,
            "current": 2.09,
            "volume_ratio": 0.92,
            "amplitude": 5.94,
            "pb": 1.066,
            "current_year_percent": 55.97,
            "turnover_rate": 2.3,
            "float_market_capital": 25969912231,
            "name": "永泰能源",
            "market_capital": 25969912231,
            "pe_ttm": 117.073,
            "dividend_yield": 1,
            "lot_size": 100,
            "percent5m": -0.48
        }, {
            "symbol": "SH600030",
            "amount": 5991016227,
            "chg": -0.79,
            "type": 11,
            "percent": -3.33,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 257207455,
            "current": 22.91,
            "volume_ratio": 1,
            "amplitude": 4.81,
            "pb": 1.813,
            "current_year_percent": 43.1,
            "turnover_rate": 2.62,
            "float_market_capital": 224853899547,
            "name": "中信证券",
            "market_capital": 277598371444,
            "pe_ttm": 29.564,
            "dividend_yield": 1.746,
            "lot_size": 100,
            "percent5m": 0.09
        }, {
            "symbol": "SH600050",
            "amount": 1680880705,
            "chg": -0.23,
            "type": 11,
            "percent": -3.38,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 252915224,
            "current": 6.58,
            "volume_ratio": 1.03,
            "amplitude": 4.85,
            "pb": 1.456,
            "current_year_percent": 27.27,
            "turnover_rate": 1.19,
            "float_market_capital": 139473604279,
            "name": "中国联通",
            "market_capital": 204249567380,
            "pe_ttm": 50.052,
            "dividend_yield": 0.301,
            "lot_size": 100,
            "percent5m": 0.3
        }, {
            "symbol": "SH600635",
            "amount": 1958370562,
            "chg": -0.51,
            "type": 11,
            "percent": -6.23,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 247166443,
            "current": 7.67,
            "volume_ratio": 1.04,
            "amplitude": 10.88,
            "pb": 3.209,
            "current_year_percent": 63.54,
            "turnover_rate": 10.22,
            "float_market_capital": 18552132147,
            "name": "大众公用",
            "market_capital": 22645173957,
            "pe_ttm": 49.986,
            "dividend_yield": 0.782,
            "lot_size": 100,
            "percent5m": 0
        }, {
            "symbol": "SH601288",
            "amount": 903353790,
            "chg": 0.01,
            "type": 11,
            "percent": 0.27,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 246438583,
            "current": 3.67,
            "volume_ratio": 0.95,
            "amplitude": 0.82,
            "pb": 0.828,
            "current_year_percent": 1.94,
            "turnover_rate": 0.08,
            "float_market_capital": 1079182928628,
            "name": "农业银行",
            "market_capital": 1284437734314,
            "pe_ttm": 6.279,
            "dividend_yield": 4.858,
            "lot_size": 100,
            "percent5m": 0.27
        }, {
            "symbol": "SH601099",
            "amount": 978595333,
            "chg": -0.1,
            "type": 11,
            "percent": -2.46,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 242845808,
            "current": 3.97,
            "volume_ratio": 0.57,
            "amplitude": 4.18,
            "pb": 2.406,
            "current_year_percent": 59.44,
            "turnover_rate": 3.75,
            "float_market_capital": 25720900989,
            "name": "太平洋",
            "market_capital": 27060775989,
            "pe_ttm": -188.199,
            "dividend_yield": 0.252,
            "lot_size": 100,
            "percent5m": -0.25
        }, {
            "symbol": "SH600572",
            "amount": 2490456845,
            "chg": 0.28,
            "type": 11,
            "percent": 2.81,
            "has_follow": False,
            "tick_size": 0.01,
            "volume": 240537968,
            "current": 10.25,
            "volume_ratio": 1.24,
            "amplitude": 8.12,
            "pb": 4.617,
            "current_year_percent": 72.85,
            "turnover_rate": 9.04,
            "float_market_capital": 27270928057,
            "name": "康恩贝",
            "market_capital": 27340032050,
            "pe_ttm": 31.403,
            "dividend_yield": 1.463,
            "lot_size": 100,
            "percent5m": 0
        }]
    },
    "error_code": 0,
    "error_description": ""
}
validate(instance=livevalue, schema=schema_stock_zf)