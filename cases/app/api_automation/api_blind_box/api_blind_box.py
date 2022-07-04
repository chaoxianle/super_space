from lib.api_app import user
from lib.api_web import admin
from hytest import *
import json
import traceback

#微信抢购盲盒创建订单
class blind_box_create_order_001:
    name = "抢购盲盒生成订单 create_order_001"
    def teststeps(self):
        global openBlindBoxSuccess
        # 获取盲盒活动
        STEP(1,'获取盲盒活动')
        setResponse = admin.getBlindBoxActivity().json()["data"]["list"]
        setList = []
        for item in setResponse:
            setList.append(item["id"])
        #开盲盒
        STEP(2,'开盲盒')
        for id in setList:
            openBlindBoxSuccess = user.openBlindBox(f'{id}',1).json()
            expected = {
                        "code": 0,
                        "data": "",
                        "message": "成功"
                    }
            try:
                CHECK_POINT('返回消息体正确',
                            expected["code"] == openBlindBoxSuccess["code"] and
                            expected["message"] == openBlindBoxSuccess["message"]
                )
                INFO(json.dumps(openBlindBoxSuccess,ensure_ascii=False,indent=4))
            except Exception:
                INFO(traceback.format_exc())
                STEP(2,'查看我的盲盒')
                myBlindBox = user.myBlindBox(1000,1000,f'{id}').json()
                expected = {
                            "code": 0,
                            "data": {
                                "list": [],
                                "page": 0,
                                "total": 1
                            },
                            "message": "成功"
                        }
                CHECK_POINT('返回消息体正确',
                            expected["code"] == openBlindBoxSuccess["code"] and
                            expected["message"] == openBlindBoxSuccess["message"]
                            )
                INFO(json.dumps(myBlindBox, ensure_ascii=False, indent=4))

#微信抢盲盒限购2份
class blind_box_create_order_002:
    name = "抢购盲盒生成订单 create_order_002"
    def teststeps(self):
        global openBlindBoxSuccess
        # 获取盲盒活动
        STEP(1,'获取盲盒活动')
        setResponse = admin.getBlindBoxActivity().json()["data"]["list"]
        for number in range(3):
            setList = []
            for item in setResponse:
                setList.append(item["id"])
            #开盲盒
            STEP(2,'开盲盒')
            for id in setList:
                openBlindBoxSuccess = user.openBlindBox(f'{id}',1).json()
                expected = {
                    "code": 1,
                    "data": None,
                    "message": "购买数量已上限"
                }
                try:
                    CHECK_POINT('返回消息体正确',
                                expected["code"] == openBlindBoxSuccess["code"] and
                                expected["message"] == openBlindBoxSuccess["message"]
                    )
                    INFO(json.dumps(openBlindBoxSuccess,ensure_ascii=False,indent=4))
                except Exception:
                    #打印异常
                    INFO(traceback.format_exc())
                    STEP(2,'查看我的盲盒')
                    myBlindBox = user.myBlindBox(1000,1000,f'{id}').json()
                    expected = {
                                "code": 0,
                                "data": {
                                    "list": [],
                                    "page": 0,
                                    "total": 1
                                },
                                "message": "成功"
                            }
                    CHECK_POINT('返回消息体正确',
                                expected["code"] == openBlindBoxSuccess["code"] and
                                expected["message"] == openBlindBoxSuccess["message"]
                                )
                    INFO(json.dumps(myBlindBox, ensure_ascii=False, indent=4))