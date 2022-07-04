import config
import requests
from hytest import *

urlAppAddress = config.test_url_app
class UserAPI:

    global urlAppAddress

    #控制台打印
    def _printResponse(self,response):
        print('\n\n---------- HTTP response * brgin ----------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}：{v}')

        print('')

        print(response.content.decode('utf8'))
        print('---------- HTTP response * end ----------\n\n')

    #登录单接口封装
    def login(self,Account,Password,Type):

        response = requests.post(url=urlAppAddress + '/app/login_app',
                                 data=
                                 {
                                     "Account": Account,    # 用户名
                                     "Password": Password,  # 密码
                                     "Type": Type           # 登录类型，1密码登录，2验证码登录
                                 }
                                 )
        self._printResponse(response)
        return response


    #获取Token封装
    def appLogin(self) :

        response = requests.post(url=urlAppAddress+'/app/login_app',
                                data=
                                {
                                    "Account" :18193458090,  # 用户名
                                    "Password":123456,       # 密码
                                    "Type":1                 # 登录类型，1密码登录，2验证码登录
                                }
                                )

        userToken = response.json()["data"]["token"]
        Token = 'Bearer' + ' ' + userToken
        header = {
            "Authorization": Token
        }

        return header

    # 获取藏品售卖列表
    def getNftList(self):

        response = requests.get(url=urlAppAddress +'//public/nft/list2',
                                headers=self.appLogin()
                                )

        self._printResponse(response)
        return response


    #微信支付
    def wechat_pay(self,spu_id,pay_type):

        response = requests.post(url=urlAppAddress+'/api_automation automation/wechat/create_order',
                                 headers=self.appLogin(),
                                 data=
                                 {
                                        "spu_id"  :spu_id,           # 库存ID
                                        "pay_type":pay_type          # 购买类型，1是微信支付，2是支付宝支付，3是汇付支付
                                 }
                                )

        self._printResponse(response)
        return response

    #汇付支付
    def remittance_pay(self,spu_id):

        response = requests.post(url=urlAppAddress+'/api_automation automation/fhpay/create_fh_order',
                                 headers=self.appLogin(),
                                 data=
                                 {
                                        "spu_id":spu_id              # 库存ID
                                 }
                                )

        self._printResponse(response)
        return response

     #开盲盒
    def openBlindBox(self,activity_id,pay_type):

        response = requests.post(url=urlAppAddress+'/api_automation automation/box/order/create_box_order',
                                 headers=self.appLogin(),
                                 data=
                                 {
                                    "activity_id":activity_id,          # 盲盒活动id
                                    "pay_type":pay_type                 # 购买类型
                                 }
                                 )

        self._printResponse(response)
        return response

    #我的盲盒
    def myBlindBox(self,page_num,page_size,activity_id):

        response = requests.post(url=urlAppAddress + '/api_automation automation/box/activity/myboxs',
                                 headers=self.appLogin(),
                                 data={
                                         "page_num": page_num,              # 页码
                                         "page_size": page_size,            # 页面数量
                                         "activity_id":activity_id          # 盲盒活动 id
                                      }
                                 )

        self._printResponse(response)
        return response

    # 我的藏品
    def myNft(self,status,page_num,page_size):

        response = requests.get(url=urlAppAddress + '/api_automation automation/nft_order_app/list_page',
                                headers=self.appLogin(),
                                params={
                                            "status":status,                   # 订单状态：1：待支付，2、已支付，4：已取消
                                            "page_num":page_num,               # 页码
                                            "page_size":page_size              # 分页大小
                                           }

                                )
        self._printResponse(response)
        return response

    # 展厅列表
    def getShowroom(self):

        response = requests.get(url=urlAppAddress + '/api_automation automation/api_showroom/list',
                                headers=self.appLogin()
                                )
        self._printResponse(response)
        return response

    # 展厅分类
    def getShowroomCategory(self, showroom_id, name, page_num, page_size):
        response = requests.get(url=urlAppAddress + '/api_automation automation/api_showroom/spu/category/list',
                                headers=self.appLogin(),
                                params={
                                            "showroom_id": showroom_id,             # 展厅id
                                            "name": name,                           # 展厅名称
                                            "page_num": page_num,                   # 页码
                                            "page_size": page_size                  # 页码大小
                                        }
                                )
        self._printResponse(response)
        return response

    # 展厅藏品列表
    def getShowroomList(self, show_room_id, spu_id, page_num, page_size):
        response = requests.get(url=urlAppAddress + '/api_automation automation/api_showroom/spu/list',
                                headers=self.appLogin(),
                                params={
                                            "show_room_id": show_room_id,       # 展厅id
                                            "spu_id": spu_id,                   # 库存id
                                            "page_num": page_num,               # 页码
                                            "page_size": page_size              # 页码大小
                                        }
                                )
        self._printResponse(response)
        return response

    # 藏品展出
    def getNftExhibit(self, showroom_id, spu_id, title, content):
        response = requests.post(url=urlAppAddress + '/api_automation automation/api_showroom/spu/exhibit',
                                 headers=self.appLogin(),
                                 json={
                                     "showroom_id": showroom_id,        # 展厅id
                                     "spu_id": spu_id,                  # 库存id
                                     "title": title,                    # 标题
                                     "content": content                 # 藏品内容
                                 }
                                 )
        self._printResponse(response)
        return response

    # 藏品取消展出
    def cancelNftExhibit(self, exhibits_id):
        response = requests.post(url=urlAppAddress + '/api_automation automation/api_showroom/spu/cancel',
                                 headers=self.appLogin(),
                                 data={
                                     "exhibits_id": exhibits_id         # 要取消的藏品exhibits_id
                                 }
                                 )
        self._printResponse(response)
        return response

    # 评论列表
    def commentList(self, showroom_id, exhibits_id, page_num, page_size):
        response = requests.get(url=urlAppAddress + '/api_automation automation/comment/list',
                                headers=self.appLogin(),
                                params={
                                            "showroom_id": showroom_id,         # 展厅 id
                                            "exhibits_id": exhibits_id,         # 藏品的展示 id
                                            "page_num": page_num,               # 页码
                                            "page_size": page_size              # 页码大小
                                        }
                                )
        self._printResponse(response)
        return response

    # 发送评论
    def sendComment(self, exhibits_id, content, uid_was_replied, parent_id):
        response = requests.post(url=urlAppAddress + '/api_automation automation/comment/post',
                                 headers=self.appLogin(),
                                 data={
                                     "exhibits_id": exhibits_id,            # 藏品的展示 id
                                     "content": content,                    # 评论内容
                                     "uid_was_replied": uid_was_replied,    # 被回复用户 id
                                     "parent_id": parent_id                 # 父目录
                                 }
                                 )
        self._printResponse(response)
        return response

    # 删除评论
    def delComment(self, ids):
        response = requests.get(url=urlAppAddress + '/api_automation automation/comment/delete',
                                headers=self.appLogin(),
                                params={
                                        "id": ids                               # 要删除评论的 id
                                       }
                                )
        self._printResponse(response)
        return response

    # 藏品转增
    def sendNft(self,order_id,send_uuid,pay_password):
        response = requests.post(url=urlAppAddress + '/api_automation automation/nft_order/send',
                                 headers=self.appLogin(),
                                 data={
                                        "id": order_id,                        # 订单 id
                                        "send_uuid":send_uuid,                 # 转增方地址
                                        "pay_password":pay_password            # 交易密码
                                     }
                                 )
        self._printResponse(response)
        return response

    # 藏品订单接口
    def nftOrder(self,status,page_num,page_size):
        response = requests.get(url=urlAppAddress + '/api_automation automation/nft_order_app/list2_page',
                                headers=self.appLogin(),
                                params= {
                                            "status":status,                  # 订单状态：1：待支付，2、已支付，4：已取消
                                            "page_num":page_num,              # 页码
                                            "page_size":page_size             # 分页大小
                                        }
                                )

        self._printResponse(response)
        return response

    # 藏品合成查询持有情况
    # def getNftCompose(self,cid):
    #     response = requests.get(url=urlAppAddress + '/api_automation automation/nft_compose/spu',
    #                             headers=self.appLogin(),
    #                             params={
    #                                         "id":cid                          # 合成方案id
    #                                     }
    #                             )
    #     self._printResponse(response)
    #     return response

    #所有藏品合成方案列表
    def getNftComposeList(self):
        response = requests.get(url=urlAppAddress + '/api_automation automation/nft_compose/list',
                                headers=self.appLogin()
                                )

        self._printResponse(response)
        return response

    # 藏品合成方案持有情况
    def searchNftCompose(self,cid):
        response = requests.post(url=urlAppAddress + '/api_automation automation/nft_compose/search',
                                 headers=self.appLogin(),
                                 data={
                                            "id":cid                          # 合成方案id
                                        }
                                 )

        self._printResponse(response)
        return response

    # 藏品合成
    def nftCompose(self,ids):
        response = requests.post(url=urlAppAddress + '/api_automation automation/nft_order/synthesis',
                                 headers=self.appLogin(),
                                 json={
                                            "ids": [
                                                ids
                                            ]
                                        }
                                 )

        self._printResponse(response)
        return response

user = UserAPI()