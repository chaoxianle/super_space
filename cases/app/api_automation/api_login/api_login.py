from lib.api_app import user
from hytest import *
import json
import traceback

class Login_001:
    name = "正确的用户名和密码 Login_001"
    def teststeps(self):
        STEP(1, '使用已注册手机号18193458090，正确密码123456，类型选择用户名密码进行登录')
        try:
            login_success = user.login('18193458090','123456',1)
            ret = login_success.json()
            expected = {
                        "code": 0,
                        "msg": "success",
                        "data": {
                            "token": "yuWe2+oEUEM/amSNTjK2L1IlrGG2QW+hcF2KAoQQ9FwPT6MG164EQ3xQfNo2lPOl",
                            "user": {
                                "id": 1096746,
                                "ali_user_id": "2088522170603150",
                                "access_token": "",
                                "nick_name": "朝鲜乐",
                                "avatar": "https://tfs.alipayobjects.com/images/partner/TB1petIajyEDuNkUQusXXbvMVXa",
                                "invite_code": "JI82EU",
                                "uuid": "33832ea020ee25999f670d63493b4ab8",
                                "account": "18193458090"
                            }
                        }
                    }
            CHECK_POINT('返回的消息体数据正确',
                        expected["code"] == ret["code"] and
                        expected["msg"] == ret["msg"] and
                        expected["data"]["user"] == ret["data"]["user"]
                        )
            INFO(json.dumps(ret,ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())

class Login_002:

    name = "使用未注册的账号登录 Login_002"

    def teststeps(self):

        STEP(1,'使用手机号13884191286,密码123456，类型选择用户名密码进行登录进行登录')
        login_fail = user.login('13884191286','123456',1)
        ret = login_fail.json()
        expected = {
                  'code': -1,
                  'data': None,
                  'message': '电话不存在'
                }

        CHECK_POINT('返回的消息体正确:',expected == ret)
        INFO(json.dumps(ret,ensure_ascii=False, indent=4))

class Login_003:

    name = "使用错误手机号和密码进行登录 Login_003"

    def teststeps(self):

        STEP(1,'使用手机号12138495948,密码3290ehwif，类型选择用户名密码进行登录进行登录')
        login_fail = user.login('12138495948','3290ehwif',1)
        ret = login_fail.json()
        expected = {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))



class Login_004:

    name = "使用已注册手机号和正确密码,类型2进行登录 Login_004"

    def teststeps(self):

        STEP(1,'使用手机号18193458090,密码123456,类型选择验证码进行登录')
        login_fail = user.login('18193458090','123456',2)
        ret = login_fail.json()
        expected = {
                        'code': -1,
                        'data': None,
                        'message': '验证码错误'
                    }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))


class Login_005:

    name = "使用已注册手机号和错误密码进行登录 Login_005"

    def teststeps(self):

        STEP(1,'使用手机号18193458090,密码9384723，类型选择用户名密码进行登录进行登录')
        login_fail = user.login('18193458090','9384723',1)

        ret = login_fail.json()
        expected = {
                        'code': -1,
                        'data': None,
                        'message': '密码错误'
                    }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

class Login_006:

    name = "手机号、密码、类型均为空进行登录 Login_006"

    def teststeps(self):

        STEP(1,'手机号、密码、类型均为空进行登录')
        login_fail = user.login(None,None,None)

        ret = login_fail.json()
        expected = {
                        'code': -1,
                        'data': None,
                        'message': '账户不可为空'
                    }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

class Login_007:

    name = "手机号小于11位数字，密码小于6位进行登录 Login_007"

    def teststeps(self):

        STEP(1,'使用手机号1819345809,密码12345，类型选择用户名密码进行登录进行登录')
        login_fail = user.login('1819345809','12345',1)

        ret = login_fail.json()
        expected = {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

class Login_008:

    name = "手机号大于11位数字，密码大于6位进行登录 Login_008"

    def teststeps(self):

        STEP(1,'使用手机号118193458090,密码1234567，类型选择用户名密码进行登录')
        login_fail = user.login('118193458090','1234567',1)

        ret = login_fail.json()
        expected = {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

class Login_009:

    name = "手机号参数值传入int类型，密码参数值传入int类型，类型参数值传入str类型 Login_009"

    def teststeps(self):
        STEP(1,'使用手机号18193458090，正确密码123456，类型“1”进行登录')
        try:
            login_fail = user.login(18193458090,123456,'1')
            ret = login_fail.json()
            expected = {
                            'code': -1,
                            'data': None,
                            'message': '类型错误'
                        }

            CHECK_POINT('返回的消息体正确:', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class Login_010:

    name = "只填写手机号和密码，不填写类型进行登录 Login_010"

    def teststeps(self):

        STEP(1,'使用手机号18193458090，密码123456进行登录')
        login_fail = user.login('18193458090','123456',None)

        ret = login_fail.json()
        expected = {
                        'code': -1,
                        'data': None,
                        'message': '类型错误'
                    }

        CHECK_POINT('返回的消息体正确:', expected == ret)
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))

class Login_ddt:
    expected = [
        {
            "code": 0,
            "msg": "success",
            "data": {
                "token": "yuWe2+oEUEM/amSNTjK2L1IlrGG2QW+hcF2KAoQQ9FwPT6MG164EQ3xQfNo2lPOl",
                "user": {
                    "id": 1096746,
                    "ali_user_id": "2088522170603150",
                    "access_token": "",
                    "nick_name": "朝鲜乐",
                    "avatar": "https://tfs.alipayobjects.com/images/partner/TB1petIajyEDuNkUQusXXbvMVXa",
                    "invite_code": "JI82EU",
                    "uuid": "33832ea020ee25999f670d63493b4ab8",
                    "account": "18193458090"
                }
            }
        },
        {
            'code': -1,
            'data':None,
            'message': '电话不存在'
        },
        {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        },
        {
            'code': -1,
            'data': None,
            'message': '验证码错误'
        },
        {
            'code': -1,
            'data': None,
            'message': '密码错误'
        },
        {
            'code': -1,
            'data': None,
            'message': '账户不可为空'
        },
        {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        },
        {
            'code': -1,
            'data': None,
            'message': '电话不存在'
        },
        {
            'code': -1,
            'data': None,
            'message': '类型错误'
        },
        {
            'code': -1,
            'data': None,
            'message': '类型错误'
        }
    ]

    ddt_cases = [
        {
            'name': '正确的用户名和密码 Login_001',
            'para': ['18193458090', '123456', 1, f'{expected[0]}']
        },
        {
            'name': '使用未注册的账号登录 Login_002',
            'para': ['13884191286', '123456', 1, f'{expected[1]}']
        },
        {
            'name': '使用错误手机号和密码进行登录 Login_003',
            'para': ['12138495948', '3290ehwif', 1, f'{expected[2]}']
        },
        {
            'name': '使用已注册手机号和正确密码,类型2进行登录 Login_004',
            'para': ['18193458090', '123456', 2, f'{expected[3]}']
        },
        {
            'name': '使用已注册手机号和错误密码进行登录 Login_005',
            'para': ['18193458090', '9384723', 1, f'{expected[4]}']
        },
        {
            'name': '手机号、密码、类型均为空进行登录 Login_006',
            'para': [None, None, None, f'{expected[5]}']
        },
        {
            'name': '手机号小于11位数字，密码小于6位进行登录 Login_007',
            'para': ['1819345809', '12345', 1, f'{expected[6]}']
        },
        {
            'name': '手机号大于11位数字，密码大于6位进行登录 Login_008',
            'para': ['118193458090', '1234567', 1, f'{expected[7]}']
        },
        {
            'name': '手机号参数值传入int类型，密码参数值传入int类型，类型参数值传入str类型 Login_009',
            'para': [18193458090, 123456, '1', f'{expected[8]}']
        },
        {
            'name': '只填写手机号和密码，不填写类型进行登录 Login_010',
            'para': ['18193458090', '123456', None, f'{expected[9]}']
        }
    ]
    def teststeps(self):
        global expect,ret

        for res,expect in zip(self.ddt_cases,self.expected):
            ret = user.login(res["para"][0],res["para"][1],res["para"][2]).json()
        CHECK_POINT('返回消息体正确',expect["code"] == ret["code"] and
                                  expect["data"] == ret["data"]
                       )
        INFO(json.dumps(ret, ensure_ascii=False, indent=4))
