# -*- encoding: utf-8 -*-

"""
**********************************************************
* $ |    .     *         *                          | ￥ *
* $ |           .           .               .       | ￥ *
* $ |    *                      ,                   | ￥ *
* $ |        .         .                     *      | ￥ *
* $ |          .                                    | ￥ *
* $ |                               *               | ￥ *
* $ |          |\___/|                              | ￥ *
* $ |          )    -(             .        *     · | ￥ *
* $ |   .     =\ -   /=                             | ￥ *
* $ |           )===(       *           .           | ￥ *
* $ |  .       /   - \                          *   | ￥ *
* $ |          |-    |                            . | ￥ *
* $ |         /   -   \     0.|.0                   | ￥ *
* $ |  _______\__( (__/_____(\=/)_________________  | ￥ *
* $ |  _|____|____) )______|______|_______|_____|_  | ￥ *
* $ |  ___|______( (____|______|______|______|____  | ￥ *
* $ |  ______|____\_|______|______|______|______|_  | ￥ *
* $ |  ___|______|______|______|______|______|____  | ￥ *
* $ |  ______|______|______|______|______|______|_  | ￥ *
* $ |  ___|______|______|______|______|______|____  | ￥ *
**********************************************************
    *************************************************
    *  吾有一猫一鼠，猫可控萝莉，鼠可镇基佬！           *
    *                          ——来自某位低调大帅比   *
    *************************************************    
@Author  :   王东林

@License :   清羽 (C) Copyright 2013-2019

@Contact :   qyu0615@gmail.com

@Software:   PyCharm

@File    :   07.快手美女下载.py

@Time    :   2019/7/1 23:26

"""
import requests
from lxml import etree

url = r"http://www.fuliget.net/player"
gHeads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}
html = requests.get(url, headers=gHeads)
xmlContent = etree.HTML(html.content)
hrefList = xmlContent.xpath("//option/@value")
nameList = xmlContent.xpath("//option/@title")
count = 0
for i in range(len(hrefList)):
    count = count + 1
    mp4 = requests.get(hrefList[i], gHeads)
    with open(r"C:\Users\wdl10\Desktop\爬取美女\{0}.mp4".format(nameList[i]), "wb+") as f:
        f.write(mp4.content)
        print("第%d视频已下载" % count)

