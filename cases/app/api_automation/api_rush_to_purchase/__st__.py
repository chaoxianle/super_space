from hytest import *
from lib.api_app import user
from lib.api_web import admin
import time
import random
import json

# 套件初始化方法
def suite_setup():
    global ids
    INFO('新增系列')
    currentTime = int(time.time())
    admin.createSeries(f'阿乐{currentTime}')
    INFO(json.dumps(admin.createSeries(f'阿乐{currentTime}').json(),ensure_ascii=False,indent=4))

    INFO('获取所有系列')
    admin.getSeries(None)
    INFO(json.dumps(admin.getSeries(None),ensure_ascii=False,indent=4))

    INFO('修改新增系列为超维空间系列')
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    admin.modiySeries(f'{seriesId}','超维空间')
    INFO(json.dumps(admin.modiySeries(f'{seriesId}','超维空间'),ensure_ascii=False,indent=4))

    INFO('新增藏品')
    # 设置藏品发售开始/结束时间
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 设置随机数
    num = str(random.randint(1, 100000))
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    admin.createNft(seriesId,3,f'阿乐大礼包{num}','http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg',
                        '阿乐','阿乐快跑','阿乐著名画家真人画作',0.01,'0','2',f'{currentTime}',f'{num}'+'#','艺术品')
    INFO(json.dumps(admin.createNft(seriesId,3,f'阿乐大礼包{num}','http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg',
                        '阿乐','阿乐快跑','阿乐著名画家真人画作',0.01,'0','2',f'{currentTime}',f'{num}'+'#','艺术品').json(), ensure_ascii=False, indent=4))

    INFO('修改藏品为热卖中藏品')
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    spu_id = admin.getNftList(100000000).json()["data"]["list"]
    spuList = []
    for item in spu_id:
        spu_ids = item["id"]
        spuList.append(spu_ids)
    for ids in spuList:
        # 设置藏品发售开始/结束时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # 设置随机数
        num = str(random.randint(1, 100000))
        admin.modifyNft(f'{ids}',3,f'阿乐大礼包{num}','http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg','阿乐',
                           '阿乐快跑','阿乐著名画家真人画作',0.01,'0','2',f'{currentTime}',f'{num}'+'#','艺术品',2,2,1,seriesId)
    INFO(json.dumps(admin.modifyObject(f'{ids}',3,f'阿乐大礼包{num}','http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg','阿乐',
                       '阿乐快跑','阿乐著名画家真人画作',0.01,'0','2',f'{currentTime}',f'{num}'+'#','艺术品',2,2,1,seriesId).json(),ensure_ascii=False,indent=4))

    INFO('用户登录')
    user.appLogin()
    INFO(json.dumps(user.appLogin(),ensure_ascii=False,indent=4))

# 套件清除方法
def suite_teardown():
    global id
    GSTORE
    INFO('删除新增藏品')
    # 获取新增藏品spu_id
    spu_id = admin.getNftList(100000000)
    for id in spu_id:
        admin.delNft(f'{id}')
    INFO(json.dumps(admin.delNft(f'{id}').json(),ensure_ascii=False,indent=4))

    INFO('删除系列')
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    admin.delSeries(seriesId)
    INFO(json.dumps(admin.delSeries(seriesId).json(),ensure_ascii=False,indent=4))