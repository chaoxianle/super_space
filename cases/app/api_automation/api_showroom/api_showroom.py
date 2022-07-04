from lib.api_app import user
from hytest import *
import json
import traceback


# 展出任意一个藏品
class NftExhibit_001:
    name = '展出任意一个藏品  NftExhibit_001'
    def teststeps(self):
        # 获取展厅列表
        showroomList = user.getShowroomList().json()
        expected = {
            {
                "code": 0,
                "data": [
                    {
                        "id": "c9bpoemtan7hrh3d4nkg",
                        "name": "官方",
                        "details": "官方2D展厅",
                        "nature": 1,
                        "dimension_type": 1,
                        "created_at": "2022-04-13 11:04:26",
                        "updated_at": "",
                        "deleted_at": ""
                    }
                ],
                "message": "成功"
            }
        }
        CHECK_POINT('返回消息体正确', expected == showroomList)
        INFO(json.dumps(showroomList, ensure_ascii=False, indent=4))

        # 我的藏品
        myNft = user.myNft(2, 1, 10000).json()
        expected = {
            "code": 0,
            "data": {
                "list": [
                    {
                        "id": 2262574,
                        "cid": "5",
                        "spu_id": 275,
                        "user_name": "朝鲜乐",
                        "name": "520告白卡",
                        "image": "http://oss.hzchainup.com/pub_upload/2022-05-20/eefb7a6b75bba7106cb02c4f4d6974dc.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-05-20/eefb7a6b75bba7106cb02c4f4d6974dc.jpg",
                        "content": "",
                        "content_mini": "",
                        "three": "pub_upload/2022-05-20/ck4965i1pocsq8tlsp.glb",
                        "three_map": "",
                        "creator": "超维空间创作团队",
                        "creator_image": "pub_upload/2022-05-20/c205d5a0137ac1599906dcbe01ba999e.jpg",
                        "issuer": "超维空间",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "superd50ba75c2e42525e6874f602f3ff8c7f0",
                        "pay_number": "2022052022001403151413725302",
                        "code": "520GBK#12625#200000",
                        "hash": "",
                        "trade_hash": "",
                        "status": 2,
                        "created_at": "2022-05-20 13:26:06",
                        "three_type": 2,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 2096538,
                        "cid": "5",
                        "spu_id": 236,
                        "user_name": "朝鲜乐",
                        "name": "母亲的康乃馨",
                        "image": "http://oss.hzchainup.com/pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "content": "http://oss.hzchainup.com/pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "content_mini": "",
                        "three": "pub_upload/2022-05-08/cjto9ksiuejwjcugst.glb",
                        "three_map": "",
                        "creator": "超维空间创作团队",
                        "creator_image": "http://oss.hzchainup.com/pub_upload/2022-05-08/99c064ffe8d8536dad86d016fd16af70.jpg",
                        "issuer": "超维空间",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "c9rmel4vpifu1bphh6rg",
                        "pay_number": "4200001471202205083850449910",
                        "code": "MQDKNX#196290#200000",
                        "hash": "",
                        "trade_hash": "effd5837fc08f78d8e1efc66dc16e266f997e387601f4c32e7713c07e8699564",
                        "status": 2,
                        "created_at": "2022-05-08 14:46:44",
                        "three_type": 2,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1880145,
                        "cid": "5",
                        "spu_id": 236,
                        "user_name": "朝鲜乐",
                        "name": "母亲的康乃馨",
                        "image": "pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "content": "pub_upload/2022-05-08/799f2f8f6bf802eeab44d283bc80a122.jpg",
                        "content_mini": "",
                        "three": "pub_upload/2022-05-08/cjto9ksiuejwjcugst.glb",
                        "three_map": "",
                        "creator": "超维空间创作团队",
                        "creator_image": "pub_upload/2022-05-08/99c064ffe8d8536dad86d016fd16af70.jpg",
                        "issuer": "超维空间",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "superd7f4d2e76041625ceae5fb4c3c6289187",
                        "pay_number": "2022050822001403151402416878",
                        "code": "MQDKNX#11866#200000",
                        "hash": "",
                        "trade_hash": "",
                        "status": 2,
                        "created_at": "2022-05-08 09:20:49",
                        "three_type": 2,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1757865,
                        "cid": "5",
                        "spu_id": 215,
                        "user_name": "朝鲜乐",
                        "name": "超维空间五一纪念徽章",
                        "image": "pub_upload/2022-04-30/414c7fc2748e51e3abda5378732932e5.png",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-04-30/414c7fc2748e51e3abda5378732932e5.png",
                        "content": "",
                        "content_mini": "",
                        "three": "pub_upload/2022-05-01/cjo3qgxiyxlczbk6h2.glb",
                        "three_map": "",
                        "creator": "超维空间创作团队",
                        "creator_image": "pub_upload/2022-04-30/c205d5a0137ac1599906dcbe01ba999e.jpg",
                        "issuer": "超维空间",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "superdda32862d30d223b9a42169f5cb7c4621",
                        "pay_number": "2022050122001403151456591453",
                        "code": "WYJNHZ#79860#200000",
                        "hash": "",
                        "trade_hash": "27423092004ce0e415a66279b22e46790065cba84bf1c665a4ee2e68cbea685f",
                        "status": 2,
                        "created_at": "2022-05-01 15:41:18",
                        "three_type": 2,
                        "send_status": 1,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1513491,
                        "cid": "1",
                        "spu_id": 201,
                        "user_name": "朝鲜乐",
                        "name": "超维小宇",
                        "image": "pub_upload/2022-04-24/da3709f577cb6e09ed020a132a37476f.png",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/2022-04-24/da3709f577cb6e09ed020a132a37476f.png",
                        "content": "pub_upload/2022-04-24/da3709f577cb6e09ed020a132a37476f.png",
                        "content_mini": "",
                        "three": "",
                        "three_map": "",
                        "creator": "超维空间创作团队",
                        "creator_image": "pub_upload/2022-04-24/39f26e0754fc4d6c165d004350a410d3.png",
                        "issuer": "超维空间",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "c9ik26svpifo6mm2tnog",
                        "pay_number": "4200001478202204240656592434",
                        "code": "CWXY#139#200000",
                        "hash": "",
                        "trade_hash": "4865ec8cb13b79504757a7a7ae2c56f3b2a86d8a0252a380d01fd02a5aec27b4",
                        "status": 2,
                        "created_at": "2022-04-24 20:22:51",
                        "three_type": 0,
                        "send_status": 1,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1413650,
                        "cid": "5",
                        "spu_id": 156,
                        "user_name": "朝鲜乐",
                        "name": "暗黑破坏神",
                        "image": "pub_upload/2022-04-05/cj28ylgg7al96omvpg.gif",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/image/156.png",
                        "content": "",
                        "content_mini": "",
                        "three": "pub_upload/2022-04-05/cj2908jo4du7jcp1lx.glb",
                        "three_map": "",
                        "creator": "费鲁吉欧·兰博基尼 Ferrucio Lamborghini",
                        "creator_image": "",
                        "issuer": "北京海岬文化创意有限公司",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 69.9,
                        "send_integral": 0,
                        "order_number": "",
                        "pay_number": "",
                        "code": "AHPHS#3463#4000",
                        "hash": "",
                        "trade_hash": "f7f68326e331a979a7a89b0b5d4f513daa0905f9d03874fe163ba6e884379116",
                        "status": 2,
                        "created_at": "2022-04-11 17:32:02",
                        "three_type": 2,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1313131,
                        "cid": "1",
                        "spu_id": 163,
                        "user_name": "朝鲜乐",
                        "name": "超维吉祥虎",
                        "image": "pub_upload/2022-04-06/cj34wy9h4x49vvnbah.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/image/163.png",
                        "content": "",
                        "content_mini": "",
                        "three": "",
                        "three_map": "",
                        "creator": "超维元宇宙设计团队",
                        "creator_image": "pub_upload/2022-04-06/cj34z3orv0eeqhabtx.jpg",
                        "issuer": "超维空间",
                        "introduction": "超维吉祥虎",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "",
                        "pay_number": "",
                        "code": "CWJXH#99999#100000",
                        "hash": "",
                        "trade_hash": "f7f68326e331a979a7a89b0b5d4f513daa0905f9d03874fe163ba6e884379116",
                        "status": 2,
                        "created_at": "2022-04-06 21:50:02",
                        "three_type": 0,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1205672,
                        "cid": "1",
                        "spu_id": 163,
                        "user_name": "朝鲜乐",
                        "name": "超维吉祥虎",
                        "image": "pub_upload/2022-04-06/cj34wy9h4x49vvnbah.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/image/163.png",
                        "content": "",
                        "content_mini": "",
                        "three": "",
                        "three_map": "",
                        "creator": "超维元宇宙设计团队",
                        "creator_image": "pub_upload/2022-04-06/cj34z3orv0eeqhabtx.jpg",
                        "issuer": "超维空间",
                        "introduction": "超维吉祥虎",
                        "price": 0.1,
                        "send_integral": 0,
                        "order_number": "48534315372429197155",
                        "pay_number": "2028533915",
                        "code": "CWJXH#6#100000",
                        "hash": "",
                        "trade_hash": "f10f8fe0bc8ff064152821613dec55dde2e5d37fa2f5a31f41c6b1711f2a7001",
                        "status": 2,
                        "created_at": "2022-04-06 20:05:31",
                        "three_type": 0,
                        "send_status": 2,
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
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1188556,
                        "cid": "5",
                        "spu_id": 152,
                        "user_name": "朝鲜乐",
                        "name": "《红楼梦-金陵十二钗-小女赴蝶》",
                        "image": "pub_upload/2022-04-01/ciyylnmzzcj1sibclo.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/image/152.png",
                        "content": "",
                        "content_mini": "",
                        "three": "pub_upload/2022-04-02/ciz2sn9hct0zvim0io.glb",
                        "three_map": "",
                        "creator": "国家级非遗传承人张宗凡",
                        "creator_image": "",
                        "issuer": "鲸喜玛特",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 29.9,
                        "send_integral": 0,
                        "order_number": "51824842744418819743",
                        "pay_number": "4200001306202204038169793740",
                        "code": "XNFD#2910#3000",
                        "hash": "",
                        "trade_hash": "6bfe931c2372b71741a027c39fe3930555bbec21d89f0a9bbfe9b66b075f687d",
                        "status": 2,
                        "created_at": "2022-04-03 13:20:15",
                        "three_type": 2,
                        "send_status": 2,
                        "position_type": {
                            "x": 0,
                            "y": 0,
                            "z": 0
                        },
                        "scale_type": {
                            "x": 1,
                            "y": 1,
                            "z": 1
                        },
                        "height": 380,
                        "is_show": 1,
                        "exhibits_id": ""
                    },
                    {
                        "id": 1187508,
                        "cid": "5",
                        "spu_id": 153,
                        "user_name": "朝鲜乐",
                        "name": "红楼梦-金陵十二钗-棋逢知己",
                        "image": "pub_upload/2022-04-01/ciyyrvkznh74hhjs88.jpg",
                        "thumbnail": "http://oss.hzchainup.com/pub_upload/image/153.png",
                        "content": "",
                        "content_mini": "",
                        "three": "pub_upload/2022-04-02/ciz3e27q7p9doizddi.glb",
                        "three_map": "",
                        "creator": "国家级非遗传承人张宗凡",
                        "creator_image": "",
                        "issuer": "鲸喜玛特",
                        "introduction": "数字藏品为虚拟数字商品，具有特殊性，一经售出，不支持退换。数字藏品的版权由发行方或原创者拥有，除另行取得版权拥有者书面同意外，用户不得将数字藏品用于任何商业用途。请勿对数字藏品进行炒作、场外交易、欺诈，或以任何其他非法方式进行使用。",
                        "price": 29.9,
                        "send_integral": 0,
                        "order_number": "77985457885792273558",
                        "pay_number": "4200001313202204035146523564",
                        "code": "QFZJ#2469#3000",
                        "hash": "",
                        "trade_hash": "1e697ee7b5b85ba564337415941fbec317009bc5518ca16b4671b328526b5a56",
                        "status": 2,
                        "created_at": "2022-04-03 13:06:44",
                        "three_type": 2,
                        "send_status": 2,
                        "position_type": {
                            "x": 0,
                            "y": 0,
                            "z": 0
                        },
                        "scale_type": {
                            "x": 1,
                            "y": 1,
                            "z": 1
                        },
                        "height": 380,
                        "is_show": 1,
                        "exhibits_id": ""
                    }
                ],
                "page": 1,
                "total": 14
            },
            "message": "成功"
        }
        CHECK_POINT('返回消息体正确', expected == myNft)
        INFO(json.dumps(myNft, ensure_ascii=False, indent=4))

        # 藏品展出
        nftExhibit = user.getNftExhibit(f'{showroomList["data"]["id"]}',myNft["data"]["list"][-1]["spu_id"],'价格便宜',
                                        '很有收藏价值').json()
        expected = {
                        "code": 0,
                        "data": {
                                    "id": "c9dounsvpifsom9bc4l0",
                                        },
                        "message": "成功"

                    }

        CHECK_POINT('返回消息体正确',expected == nftExhibit)
        INFO(json.dumps(nftExhibit,ensure_ascii=False,indent=4))

# 展出任意一个藏品后再取消展出
class NftExhibit_002:
    name = '展出任意一个藏品后再取消展出  NftExhibit_002'
    def teststeps(self):
        # 获取展厅列表
        showroomList = user.getShowroomList().json()["data"]["id"]
        # 我的藏品
        myNft = user.myNft(2, 1, 10000).json()["data"]["list"][-1]["spu_id"]
        # 藏品展出
        nftExhibit = user.getNftExhibit(f'{showroomList}', myNft, '价格便宜',
                                        '很有收藏价值').json()
        # 取消展出的藏品
        cancelNftExhibit = user.cancelNftExhibit(f'{nftExhibit["data"]["id"]}').json()
        expected = {
                        "code": 0,
                        "message": "成功"
                    }
        CHECK_POINT('返回消息体正确',expected == cancelNftExhibit)
        INFO(json.dumps(cancelNftExhibit,ensure_ascii=False,indent=4))

# 展出藏品后添加一条评论
class NftExhibit_003:
    name = '展出任意一个藏品后再取消展出  NftExhibit_003'
    def teststeps(self):
        # 获取展厅列表
        showroomList = user.getShowroomList().json()
        # 我的藏品
        myNft = user.myNft(2, 1, 10000).json()
        # 藏品展出
        nftExhibit = user.getNftExhibit(f'{showroomList["data"]["id"]}', myNft["data"]["list"][-1]["spu_id"], '价格便宜',
                                        '很有收藏价值').json()
        # 添加一条评论
        addcomment = user.commentList(f'{nftExhibit["data"]["list"]["id"]}','这个卖多少？').json()
        expected = {
                        "code": 0,
                        "message": "评论成功"
                    }
        CHECK_POINT('返回消息体正确',expected == addcomment)
        INFO(json.dumps(addcomment,ensure_ascii=False,indent=4))

