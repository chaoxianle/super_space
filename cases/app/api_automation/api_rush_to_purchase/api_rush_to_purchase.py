from lib.api_app import user
from lib.api_web import admin
from hytest import *
import json
import time

# 微信抢购藏品创建订单
class Create_order_001:
    name = '抢购藏品创建微信订单 create_order_001'
    def teststeps(self):
        global create_order_success
        STEP(1, '获取app首页藏品列表')
        allObject = user.getNftList().json()
        STEP(2, '抢购热卖中的藏品')
        for item in allObject["data"]:
            if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                STEP(3, '创建微信订单')
                while True:
                    create_order_success = user.wechat_pay(item["id"],None)
                    if create_order_success.json() == {
                        "code": -1,
                        "data": None,
                        "message": "当前抢购人数过多，请稍后再试"
                    }:
                        continue
                    else:
                        break
            expected = {
                "code": 0,
                "data": {
                    "appid": "wx4cc3a98eb9a14f31",
                    "partnerid": "1619446527",
                    "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                    "package": "Sign=WXPay",
                    "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                    "timestamp": "1652447626",
                    "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
                },
                "message": "成功"
            }
            ret = create_order_success.json()
            CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                        expected["data"]["appid"] == ret["data"]["appid"] and
                        expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                        expected["message"] == ret["message"]
                        )
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))

# 微信超时支付后重新创建订单
class Create_order_002:
    name = '微信超时支付后重新创建订单 create_order_002'
    def teststeps(self):
        STEP(1, '获取app首页藏品列表')
        allObject = user.getNftList().json()
        STEP(2, '抢购热卖中的藏品')
        for item in allObject["data"]:
            if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                STEP(3, '创建微信订单')
                while True:
                    create_order_success = user.wechat_pay(item["id"], None)
                    if create_order_success.json() == {
                        "code": -1,
                        "data": None,
                        "message": "当前抢购人数过多，请稍后再试"
                    }:
                        continue
                    else:
                        break
                expected = {
                    "code": 0,
                    "data": {
                        "appid": "wx4cc3a98eb9a14f31",
                        "partnerid": "1619446527",
                        "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                        "package": "Sign=WXPay",
                        "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                        "timestamp": "1652447626",
                        "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
                    },
                    "message": "成功"
                }
                ret = create_order_success.json()
                CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                            expected["data"]["appid"] == ret["data"]["appid"] and
                            expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                            expected["message"] == ret["message"]
                            )
                INFO(json.dumps(ret, ensure_ascii=False, indent=4))
                time.sleep(250)
                while True:
                    create_order_success = user.wechat_pay(item["id"], None)
                    if create_order_success.json() == {
                        "code": -1,
                        "data": None,
                        "message": "当前抢购人数过多，请稍后再试"
                    }:
                        continue
                    else:
                        break
                expected = {
                    "code": 0,
                    "data": {
                        "appid": "wx4cc3a98eb9a14f31",
                        "partnerid": "1619446527",
                        "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                        "package": "Sign=WXPay",
                        "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                        "timestamp": "1652447626",
                        "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
                    },
                    "message": "成功"
                }
                ret = create_order_success.json()
                CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                            expected["data"]["appid"] == ret["data"]["appid"] and
                            expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                            expected["message"] == ret["message"]
                            )
                INFO(json.dumps(ret, ensure_ascii=False, indent=4))

# 汇付抢购藏品创建订单
class Create_order_003:
    name = '汇付抢购藏品创建订单 create_order_003'
    def teststeps(self):
        global create_order_success
        STEP(1, '获取app首页藏品列表')
        allObject = user.getNftList().json()
        STEP(2, '抢购热卖中的藏品')
        for item in allObject["data"]:
            if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                STEP(3, '创建汇付订单')
                while True:
                    create_order_success = user.remittance_pay(item["id"])
                    if create_order_success.json() == {
                        "code": -1,
                        "data": None,
                        "message": "当前抢购人数过多，请稍后再试"
                    }:
                        continue
                    else:
                        break
            expected = {
                "code": 0,
                "data": {
                    "appid": "wx4cc3a98eb9a14f31",
                    "partnerid": "1619446527",
                    "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                    "package": "Sign=WXPay",
                    "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                    "timestamp": "1652447626",
                    "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
                },
                "message": "成功"
            }
            ret = create_order_success.json()

            CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                        expected["data"]["appid"] == ret["data"]["appid"] and
                        expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                        expected["message"] == ret["message"]
                        )
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))

# 汇付超时支付后重新创建订单
class Create_order_004:
    name = '汇付超时支付后重新创建订单 create_order_004'
    def teststeps(self):
        global create_order_success
        STEP(1, '获取app首页藏品列表')
        allObject = user.getNftList().json()
        STEP(2, '抢购热卖中的藏品')
        for item in allObject["data"]:
            if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                STEP(3, '创建汇付订单')
                while True:
                    create_order_success = user.remittance_pay(item["id"])
                    if create_order_success.json() == {
                        "code": -1,
                        "data": None,
                        "message": "当前抢购人数过多，请稍后再试"
                    }:
                        continue
                    else:
                        break
            expected = {
                "code": 0,
                "data": {
                    "appid": "wx4cc3a98eb9a14f31",
                    "partnerid": "1619446527",
                    "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                    "package": "Sign=WXPay",
                    "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                    "timestamp": "1652447626",
                    "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
                },
                "message": "成功"
            }
            ret = create_order_success.json()
            CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                        expected["data"]["appid"] == ret["data"]["appid"] and
                        expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                        expected["message"] == ret["message"]
                        )
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            time.sleep(250)
            while True:
                create_order_success = user.remittance_pay(item["id"])
                if create_order_success.json() == {
                    "code": -1,
                    "data": None,
                    "message": "当前抢购人数过多，请稍后再试"
                }:
                    continue
                else:
                    break
        expected = {
            "code": 0,
            "data": {
                "appid": "wx4cc3a98eb9a14f31",
                "partnerid": "1619446527",
                "prepayid": "wx13211346419726daacf7265fd28a4d0000",
                "package": "Sign=WXPay",
                "noncestr": "ljE1RkCCiY174KbtZ9OUjMoGXBsir8NH",
                "timestamp": "1652447626",
                "sign": "mjqJbLjZnNLNKFGlXKh9ZczF8lmAa1btpG/jLXht6ALndz50+8sgZbhYD1/NezxEL8weapsNFFtaNmuW1hwEUAWtRLpG1dFuoxUkfgbwX9JQh4h0Q82aRJap+VCrMKLhHFPAP2ioqWRbhAQeaWjrnBhqtE4K9XiihK/jjDaWPJOVhcIITLnuLx4wYfiNkhNrLJZnvxSjMoSJqWhwLuU9TJ89qdfT+bFVZMnUTqhc1AvViThY8dNgZyRCfwYFM73JHE3NkHusYUd5Rw1WEDLDHAvbhD2sJF+Lw+l+elpzSWTeeLEgvkLd03z7Ohe/eg+3fCRjMCxiG5UAhhppcs2Glg=="
            },
            "message": "成功"
        }
        ret = create_order_success.json()
        CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                    expected["data"]["appid"] == ret["data"]["appid"] and
                    expected["data"]["partnerid"] == ret["data"]["partnerid"] and
                    expected["message"] == ret["message"]
                    )
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

#微信抢购藏品限购2份
class Create_order_005:
    name = '微信抢购藏品限购2份 create_order_005'
    def teststeps(self):
        global create_order_success
        STEP(1, '获取app首页藏品列表')
        allObject = user.getObjectList().json()
        STEP(2, '抢购热卖中的藏品')
        for number in range(3):
            for item in allObject["data"]:
                if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                    STEP(3, '创建微信订单')
                    while True:
                        create_order_success = user.wechat_pay(item["id"],None)
                        if create_order_success.json() == {
                            "code": -1,
                            "data": None,
                            "message": "当前抢购人数过多，请稍后再试"
                        }:
                            continue
                        else:
                            break
            expected = {
                "code": 1,
                "data": None,
                "message": "购买数量已上限"
            }
            ret = create_order_success.json()
            CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                        expected["message"] == ret["message"]
                        )
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))

#汇付抢购藏品限购2份
class Create_order_006:
    name = '汇付抢购藏品限购2份 create_order_006'
    def teststeps(self):
        global create_order_success
        STEP(1, '获取app首页藏品列表')
        allObject = user.getObjectList().json()
        STEP(2, '抢购热卖中的藏品')
        for number in range(3):
            for item in allObject["data"]:
                if item["status"] == 2:  # status是订单状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                    STEP(3, '创建汇付订单')
                    while True:
                        create_order_success = user.remittance_pay(item["id"])
                        if create_order_success.json() == {
                            "code": -1,
                            "data": None,
                            "message": "当前抢购人数过多，请稍后再试"
                        }:
                            continue
                        else:
                            break
            expected = {
                "code": 1,
                "data": None,
                "message": "购买数量已上限"
            }
            ret = create_order_success.json()
            CHECK_POINT('返回的消息体正确', expected["code"] == ret["code"] and
                        expected["message"] == ret["message"]
                        )
            INFO(json.dumps(ret,ensure_ascii=False, indent=4))


