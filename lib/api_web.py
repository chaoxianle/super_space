import config
import requests
from hytest import *

urlWebAddress = config.test_url_web

class WebBackgroundAPI:

    global urlWebAddress

    # 控制台打印
    def _printResponse(self, response):
        print('\n\n---------- HTTP response * brgin ----------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}：{v}')

        print('')

        print(response.content.decode('utf8'))
        print('---------- HTTP response * end ----------\n\n')

    #后台获取Token
    def webToken(self):

        Token = 'Bearer' + ' ' + 'denjmIYLfgd1fSC6CnxxSHC5iI+75+deJJl7LpyA5iuQyRGHW1ms1zBVmdXhJ1Xhbql0fMW2nmXilA7Dirp9O/M3HVF5j7l6BvJRyU6X7+6C1cli+h4nAVYYvdwVIUgM7fYY5+PtwGy5P/y4eAX8qQ=='
        header = {
            "Authorization": Token
        }
        return header

    # 后台新建藏品
    def createNft(self,series_id,cid,name,image,creator,issuer,introduction,price,send_integral,issue_amount,end_at,code,tag):
        response = requests.post(url=urlWebAddress + '/project/nft/create',
                                 headers=self.webToken(),
                                 data=
                                 {
                                       "series_id":series_id,                #所属系列ID
                                       "cid":cid,                            #分类ID
                                       "name":name,                          #藏品名称
                                       "image":image,                        #图片
                                       "creator":creator,                    #创作者
                                       "issuer":issuer,                      #发行方
                                       "introduction":introduction,          #介绍
                                       "price":price,                        #价格
                                       "send_integral":send_integral,        #赠送积分
                                       "issue_amount":issue_amount,          #发行数量
                                       "end_at": end_at,                     #开始/结束时间
                                       "code":code,                          #NFT编号
                                       "tag":tag                             #藏品标签
                                },
                                 timeout=5
                                )
        self._printResponse(response)
        return response

    # 获取藏品列表
    def getNftList(self,page_size):

        response = requests.get(url=urlWebAddress + '/project/nft/list_spu',
                                headers=self.webToken(),
                                params={
                                            "page_size": page_size
                                        }
                                )

        self._printResponse(response)
        return response

    #后台修改藏品信息为正常抢购
    def modifyNft(self,mid,cid,name,image,creator,issuer,introduction,price,send_integral,issue_amount,end_at,code,tag,sale_status,status,sort,series_id):

        response = requests.post(url=urlWebAddress + '/project/nft/edit_spu',
                                     headers=self.webToken(),
                                     data =
                                     {
                                         "id":mid,                                 #藏品id
                                         "cid":cid,                                #分类ID
                                         "name":name,                              #藏品名称
                                         "image":image,                            #图片
                                         "creator":creator,                        #创作者
                                         "issuer":issuer,                          #发行方
                                         "introduction":introduction,              #介绍
                                         "price":price,                            #价格
                                         "send_integral":send_integral,            #赠送积分
                                         "issue_amount":issue_amount,              #发行数量
                                         "end_at":end_at,                          #开始/结束时间
                                         "code":code,                              #NFT编号
                                         "tag":tag,                                #藏品标签
                                         "sale_status":sale_status,                #在售（1：否；2：是；3:盲盒）
                                         "status":status,                          #状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                                         "sort":sort,                              #排序（1:首页排序（asc）；3：首页倒叙（desc））
                                         "series_id":series_id                     #系列
                                     })

        self._printResponse(response)
        return response

    #后台删除藏品信息
    def delNft(self,ids):

        response = requests.delete(url=urlWebAddress + '/project/nft/delete',
                                   headers=self.webToken(),
                                   json=
                                   {
                                       "ids": [
                                        ids
                                       ]
                                   }
                                   )

        self._printResponse(response)
        return response

    # 后台修改藏品信息为盲盒抢购
    def modifyBlindBoxObject(self,mid,cid,name,image,creator,issuer,introduction,price,send_integral,issue_amount,end_at,code,tag,sale_status,status,sort,series_id):

        response = requests.post(url=urlWebAddress + '/project/nft/edit_spu',
                                 headers=self.webToken(),
                                 data=
                                 {
                                     "id": mid,                        # 藏品id
                                     "cid": cid,                      # 分类ID
                                     "name": name,                    # 藏品名称
                                     "image": image,                  # 图片
                                     "creator": creator,              # 创作者
                                     "issuer": issuer,                # 发行方
                                     "introduction": introduction,    # 介绍
                                     "price": price,                  # 价格
                                     "send_integral": send_integral,  # 赠送积分
                                     "issue_amount": issue_amount,    # 发行数量
                                     "end_at": end_at,                # 结束时间
                                     "code": code,                    # NFT编号
                                     "tag": tag,                      # 藏品标签
                                     "sale_status": sale_status,      # 在售（1：否；2：是；3:盲盒）
                                     "status": status,                # 状态（1：待开启；2：热卖中；3：已售罄；4：空投；5：已售罄（手动））
                                     "sort": sort,                    # 排序（1:首页排序（asc）；3：首页倒叙（desc））
                                     "series_id": series_id           # 系列
                                 })

        self._printResponse(response)
        return response

    #后台新建盲盒主题
    def createBlindBoxTheme(self,name,price):

        response = requests.post(url=urlWebAddress + '/project/box/theme/create',
                                 headers=self.webToken(),
                                 data=
                                 {
                                     "name" :name,              #主题名称
                                     "price":price              #价格
                                 }
                                 )

        self._printResponse(response)
        return response

    # 后台新建盲盒活动
    def createBlindBoxActivity(self,theme_id,name,description,num,spu_limits,start_at,end_at):
        response = requests.post(url=urlWebAddress + '/project/box/activity/create',
                                 headers=self.webToken(),
                                 json=
                                 {
                                     "theme_id": theme_id,         # 主题id
                                     "name": name,                 # 活动名称
                                     "description": description,   # 描述
                                     "num":num,                    # 活动数量
                                     "spu_limits":spu_limits,      # 盲盒活动中售卖的藏品
                                     "start_at":start_at,          # 盲盒活动开始时间
                                     "end_at": end_at              # 盲盒活动结束时间
                                 })

        self._printResponse(response)
        return response

    #后台获取盲盒主题
    def getBlindBoxTheme(self):

        response = requests.get(url=urlWebAddress + '/project/box/theme/list',
                                headers=self.webToken()
                                )

        self._printResponse(response)
        return response

    #后台获取盲盒活动
    def getBlindBoxActivity(self):

        response = requests.get(url=urlWebAddress + '/project/box/activity/list',
                                headers=self.webToken())

        self._printResponse(response)
        return response

    #后台删除盲盒主题
    def delBlindBoxTheme(self,ids):

        response = requests.delete(url=urlWebAddress + '/project/box/theme/delete',
                                   headers=self.webToken(),
                                   json=
                                   {
                                       "ids": [
                                           ids            # 主题id
                                       ]
                                   }
                                   )

        self._printResponse(response)
        return response


    # 后台删除盲盒活动
    def delBlindBoxActivity(self,ids):

        response = requests.delete(url=urlWebAddress + '/project/box/activity/delete',
                                   headers=self.webToken(),
                                   json=
                                   {
                                       "ids": [
                                           ids           # 活动id
                                       ]
                                   }
                                   )

        self._printResponse(response)
        return response

    #创建新系列
    def createSeries(self,title):

        response = requests.post(url=urlWebAddress + '/project/nft_series/create',
                                 headers=self.webToken(),
                                 data={
                                     "title" :title              # 标题
                                 }
                                 )
        self._printResponse(response)
        return response

    #获取所有系列
    def getSeries(self,title):

        response = requests.get(url=urlWebAddress + '/project/nft_series/list',
                                headers=self.webToken(),
                                params={
                                         "title" :title              # 标题
                                       }
                                )
        self._printResponse(response)
        return response

    #修改系列
    def modiySeries(self,ids,title):

        response = requests.get(url=urlWebAddress + '/project/nft_series/edit',
                               headers=self.webToken(),
                               params={
                                           "id":ids,                 # 系列id
                                           "title":title             # 标题
                                       }
                               )
        self._printResponse(response)
        return response

    #删除系列
    def delSeries(self,ids):

        response = requests.delete(url=urlWebAddress + '/project/nft_series/delete',
                                   headers=self.webToken(),
                                   json={
                                            "id": ids        # 系列id
                                        }
                                   )
        self._printResponse(response)
        return response

admin = WebBackgroundAPI()