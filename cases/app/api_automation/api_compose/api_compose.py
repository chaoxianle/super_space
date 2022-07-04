from lib.api_app import user
from hytest import *
import json

# 成功合成三国风云史诗藏品
class Compose_001:
    global holdCompose,nftList
    name = "成功合成三国风云史诗藏品"
    def teststeps(self):
        # 获取所有藏品方案列表
        global holdCompose
        composeList = user.getNftComposeList().json()
        INFO(json.dumps(composeList,ensure_ascii=False,indent=4))
        for item in composeList["data"]["list"]:
            # 藏品合成方案持有情况
            holdCompose = user.searchNftCompose(f'{item["id"]}').json()
            expected = {
                            "code": 0,
                            "data": {
                                "api_compose": {
                                    "id": 6,
                                    "from_nft_id": "99;135;136;137;138;139;",
                                    "from_nft_list": [
                                        {
                                            "id": 99,
                                            "cid": "2",
                                            "name": "官渡之战",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcvqiht6k5eezq8r.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/99.png",
                                            "content": "",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcavdk3e9pwgw91v.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcaiitskxivh7tlv.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 2998,
                                            "sale_num": 2997,
                                            "status": 5,
                                            "start_at": "2022-03-16 13:00:00",
                                            "start_at_timestamp": 1647406800000,
                                            "end_at": "2022-03-16 13:00:00",
                                            "end_at_timestamp": 1647406800000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 0,
                                            "hold_count": 0,
                                            "hold_code": ""
                                        },
                                        {
                                            "id": 135,
                                            "cid": "2",
                                            "name": "千里走单骑",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcw0t7l1aa4j2bnk.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/135.png",
                                            "content": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcg22892e42gi3qb.gif",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikct5qx6fr1aeyy8j.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikcg9aq0h4tx9pnxb.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 3000,
                                            "sale_num": 2990,
                                            "status": 5,
                                            "start_at": "2022-03-16 13:00:00",
                                            "start_at_timestamp": 1647406800000,
                                            "end_at": "2022-03-16 13:00:00",
                                            "end_at_timestamp": 1647406800000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 0,
                                            "hold_count": 0,
                                            "hold_code": ""
                                        },
                                        {
                                            "id": 136,
                                            "cid": "2",
                                            "name": "孔明出山",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd3vksohzf3hadop.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/136.png",
                                            "content": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd3zex1454ifhcyf.gif",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikdazkfihz1kyhkcu.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd46ymci6skf8x2r.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 2998,
                                            "sale_num": 2994,
                                            "status": 5,
                                            "start_at": "2022-03-17 13:00:00",
                                            "start_at_timestamp": 1647493200000,
                                            "end_at": "2022-03-17 13:00:00",
                                            "end_at_timestamp": 1647493200000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 1173998,
                                            "hold_count": 1,
                                            "hold_code": "KMCS#3000#3000"
                                        },
                                        {
                                            "id": 137,
                                            "cid": "2",
                                            "name": "观沧海",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd6iiv6r2cex98up.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/137.png",
                                            "content": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd6oavrfzgzxpabg.gif",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikdba0xgyusktenhw.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikd7epouea5kvjhcd.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 2999,
                                            "sale_num": 2994,
                                            "status": 5,
                                            "start_at": "2022-03-17 13:00:00",
                                            "start_at_timestamp": 1647493200000,
                                            "end_at": "2022-03-17 13:00:00",
                                            "end_at_timestamp": 1647493200000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 0,
                                            "hold_count": 0,
                                            "hold_code": ""
                                        },
                                        {
                                            "id": 138,
                                            "cid": "2",
                                            "name": "赤壁之战",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil1yordnlnjaodgvg.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/138.png",
                                            "content": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil1yu7ov04ptxcubt.gif",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-15/cikdba0xgyusktenhw.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil1z3v02sq3o0riqm.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 2987,
                                            "sale_num": 2977,
                                            "status": 5,
                                            "start_at": "2022-03-18 13:00:00",
                                            "start_at_timestamp": 1647579600000,
                                            "end_at": "2022-03-18 13:00:00",
                                            "end_at_timestamp": 1647579600000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 0,
                                            "hold_count": 0,
                                            "hold_code": ""
                                        },
                                        {
                                            "id": 139,
                                            "cid": "2",
                                            "name": "华容道",
                                            "image": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil20x0megqotlyrcw.gif",
                                            "thumbnail": "http://oss.hzchainup.com/pub_upload/image/139.png",
                                            "content": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil211njjoi3wjdias.gif",
                                            "content_mini": "",
                                            "three": "",
                                            "three_map": "",
                                            "creator": "嘉善衍生工场科技有限公司",
                                            "creator_image": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil5p41ztn406s9lgf.jpg",
                                            "issuer": "中国文物交流中心",
                                            "details": "http://oss.hzchainup.com/pub_upload/2022-03-16/cil215xxkczi27atsa.jpg",
                                            "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                            "price": 29.9,
                                            "tag": "",
                                            "send_integral": 0,
                                            "issue_amount": 3000,
                                            "stock": 2986,
                                            "sale_num": 2981,
                                            "status": 5,
                                            "start_at": "2022-03-18 13:00:00",
                                            "start_at_timestamp": 1647579600000,
                                            "end_at": "2022-03-18 13:00:00",
                                            "end_at_timestamp": 1647579600000,
                                            "stock_status": 0,
                                            "show_type": 0,
                                            "three_type": 0,
                                            "position_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "scale_type": {
                                                "x": 0,
                                                "y": 0,
                                                "z": 0
                                            },
                                            "height": 0,
                                            "hold_order_id": 1087525,
                                            "hold_count": 1,
                                            "hold_code": "HRD#31#3000"
                                        }
                                    ],
                                    "to_nft_id": 200,
                                    "to_nft": {
                                        "id": 200,
                                        "cid": "2",
                                        "name": "三国风云史诗",
                                        "image": "http://oss.hzchainup.com/pub_upload/2022-04-24/01d5d12893333aaa31a57cbdf6904ffb.gif",
                                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-04-24/01d5d12893333aaa31a57cbdf6904ffb.gif",
                                        "content": "http://oss.hzchainup.com/pub_upload/2022-04-24/7d18c0b10a972b24f0d9b64f613504f9.gif",
                                        "content_mini": "",
                                        "three": "",
                                        "three_map": "",
                                        "creator": "嘉善衍生工场科技有限公司",
                                        "creator_image": "http://oss.hzchainup.com/pub_upload/2022-04-24/e35bff464649c9a08862faea9157f7ae.jpg",
                                        "issuer": "中国文物交流中心",
                                        "details": "http://oss.hzchainup.com/pub_upload/2022-04-24/0fa7aad57923e667c3a4f44a6121c98f.jpg",
                                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                                        "price": 0,
                                        "tag": "",
                                        "send_integral": 0,
                                        "issue_amount": 3000,
                                        "stock": 3000,
                                        "sale_num": 0,
                                        "status": 4,
                                        "start_at": "2022-04-25 00:00:00",
                                        "start_at_timestamp": 1650816000000,
                                        "end_at": "2022-04-25 00:00:00",
                                        "end_at_timestamp": 1650816000000,
                                        "stock_status": 0,
                                        "show_type": 0,
                                        "three_type": 0,
                                        "position_type": {
                                            "x": 0,
                                            "y": 0,
                                            "z": 0
                                        },
                                        "scale_type": {
                                            "x": 0,
                                            "y": 0,
                                            "z": 0
                                        },
                                        "height": 0,
                                        "hold_order_id": 0,
                                        "hold_count": 0,
                                        "hold_code": ""
                                    },
                                    "created_at": "2022-04-25 11:18:47",
                                    "updated_at": "2022-04-25 11:18:47"
                                }
                            },
                            "message": "成功"
                        }
            CHECK_POINT('返回消息体正确',expected == holdCompose)
            INFO(json.dumps(composeList,ensure_ascii=False,indent=4))
        fromNftId = holdCompose["data"]["api_compose"]["from_nft_id"].split(';')
        fromNftId.pop(-1)
        # fromNftId
        # 获取我的藏品
        nftList = []
        myNft = user.myNft(2,1,10000).json()["data"]["list"]
        INFO(json.dumps(myNft,ensure_ascii=False,indent=4))
        for item in myNft:
            nftList.append(item["spu_id"])
        if set(fromNftId) < set(nftList):
            user.nftCompose(f'{nftList}').json()
            INFO(user.nftCompose(f'{fromNftId}'))
        else:
            print('不可以合成')
            print(fromNftId)
        # for item in myNft:
        #     nftList.append(item["spu_id"])
        # print(nftList)

        # for spu_id in nftList:
        #     if spu_id in a:
        #         print('可以合成')
        #     else:
        #         print("不可以合成")
            # print(spu_id)
        # if nftList in holdCompose["data"]["api_compose"]["from_nft_id"]:
        #     print('藏品可以合成')
        # else:
        #     print('藏品不可以合成')
            # if item["spu_id"] == holdCompose["data"]["api_compose"]["from_nft_id"]:
            #     print('可以进行藏品合成')
        #     if item not in holdCompose:
        #     nftList.append(item["spu_id"])
        # print(nftList)
            # nftList = []
            # nftList.append(holdCompose["data"]["api_compose"]["from_nft_id"])
            # print(nftList)
        # INFO(holdCompose)
        # nftList = []
        # c = holdCompose["data"]["list"]["from_nft_id"]
        # print(c)
        #     nftList.append(api_compose)
        # for item in str(nftList[0]["id"]):
        #     print(item)
            # for item in api_compose:
                # print(item)

        # print(composeList)
# a = Compose_001()
# print(a.teststeps())