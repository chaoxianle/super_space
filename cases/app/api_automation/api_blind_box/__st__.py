from hytest import *
from lib.api_app import user
from lib.api_web import admin
from datetime import timedelta
import random
import time
import datetime
import json


# 套件初始化方法
def suite_setup():
    global Tid,Sid, ids, start_at, end_at

    INFO('新增系列')
    currentTime = int(time.time())
    admin.createSeries(f'阿乐{currentTime}')
    INFO(json.dumps(admin.createSeries(f'阿乐{currentTime}').json(), ensure_ascii=False, indent=4))

    INFO('获取所有系列')
    admin.getSeries(None)
    INFO(json.dumps(admin.getSeries(None), ensure_ascii=False, indent=4))

    INFO('修改新增系列为超维空间系列')
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    admin.modiySeries(f'{seriesId}', '超维空间')
    INFO(json.dumps(admin.modiySeries(f'{seriesId}', '超维空间'), ensure_ascii=False, indent=4))

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
    admin.createNft(f'{seriesId}', 3, f'阿乐大礼包{num}',
                       'http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg',
                       '阿乐', '阿乐快跑', '阿乐著名画家真人画作', 0.01, '0', '2', f'{currentTime}', f'{num}' + '#', '艺术品')
    INFO(json.dumps(admin.createNft(f'{seriesId}', 3, f'阿乐大礼包{num}',
                            'http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg',
                            '阿乐', '阿乐快跑', '阿乐著名画家真人画作', 0.01, '0', '2', f'{currentTime}', f'{num}' + '#',
                            '艺术品').json(),ensure_ascii=False,indent=4))

    INFO('修改藏品为盲盒')
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

        admin.modifyNft(f'{ids}', 3, f'阿乐大礼包{num}',
                           'http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg', '阿乐',
                           '阿乐快跑', '阿乐著名画家真人画作', 0.01, '0', '2', f'{currentTime}', f'{num}' + '#', '艺术品', 3, 1, 1,f'{seriesId}')
    INFO(json.dumps(admin.modifyNft(f'{ids}', 3, f'阿乐大礼包{num}',
                            'http://oss.hzchainup.com/pub_upload/2022-04-30/09457657a6eac2a34f903fecebe33002.jpg','阿乐',
                            '阿乐快跑', '阿乐著名画家真人画作', 0.01, '0', '2', f'{currentTime}', f'{num}' + '#', '艺术品', 3, 1 , 1,
                            f'{seriesId}').json(),ensure_ascii=False,indent=4))

    INFO('创建盲盒主题')
    # 设置随机数
    num = str(random.randint(1,100000))
    admin.createBlindBoxTheme(f'阿乐test{num}',0.03)
    INFO(admin.createBlindBoxTheme(f'阿乐test{num}',0.03).json())

    INFO('创建盲盒活动')
    # 获取盲盒主题theme_id
    theme_id = admin.getBlindBoxTheme().json()["data"]["list"]
    themeIdList = []
    for item in theme_id:
        themeIds = item["id"]
        themeIdList.append(themeIds)
    # 获取新增藏品spu_id
    spu_id = admin.getNftList(100000000).json()["data"]["list"]
    spuIdList = []
    for item in spu_id:
        spuIds = item["id"]
        spuIdList.append(spuIds)
    for Tid,Sid in zip(themeIdList,spuIdList):
        # 设置随机数
        num = str(random.randint(1, 100000))
        # 设置盲盒活动开始、结束时间
        start_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        end_at = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        admin.createBlindBoxActivity(f"{Tid}",f"阿乐大礼包{num}","阿乐福利大礼包",10,[{"spu_id": f"{Sid}", "num": 10, "score": 5.0}],
                                     f"{start_at}",f"{end_at}")
    INFO(json.dumps(admin.createBlindBoxActivity(f"{Tid}",f"阿乐大礼包{num}","阿乐福利大礼包",[{"spu_id": f"{Sid}", "num": 10, "score": 5.0}],
                                 f"{start_at}",f"{end_at}").json(),ensure_ascii=False))

# 套件清除方法
def suite_teardown():
    global id
    INFO('删除藏品')
    # 获取新增藏品spu_id
    spu_id = admin.getNftList(100000000)
    for id in spu_id:
        admin.delObject(f'{id}')
    INFO(admin.delObject(f'{id}').json())

    INFO('删除盲盒主题')
    # 获取盲盒主题
    theme_id = admin.getBlindBoxTheme()
    for id in theme_id:
        admin.delBlindBoxTheme(f"{id}")
    INFO(admin.delBlindBoxTheme(f"{id}").json())

    INFO('删除盲盒活动')
    # 获取盲盒活动
    activity_id = admin.getBlindBoxActivity()
    for id in activity_id:
        admin.delBlindBoxActivity(f"{id}")
    INFO(admin.delBlindBoxActivity(f"{id}").json())

    INFO('删除系列')
    series_id = admin.getSeries(None).json()["data"]["list"]
    seriesList = []
    for item in series_id:
        seriesIds = item["id"]
        seriesList.append(seriesIds)
    seriesId = seriesList[-1]
    admin.delSeries(seriesId)
    INFO(json.dumps(admin.delSeries(seriesId).json(), ensure_ascii=False, indent=4))