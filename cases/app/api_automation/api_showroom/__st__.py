from lib.api_app import user
from hytest import *
import json

# 套件初始化方法
def suite_setup():
    # 用户账号登录
    user.login('18193458090','123456',1)
    INFO(json.dumps(user.login('18193458090','123456',1).json(), ensure_ascii=False,indent=4))
