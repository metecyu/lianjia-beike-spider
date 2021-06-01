#!/usr/bin/env python
# coding=utf-8
# author: yuzp
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShouDetail(object):
    def __init__(self, district, area, name, price, desc, pic):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.desc = desc
        self.pic = pic
        detail = self.desc.split("|",6)
        self.roomNum = detail[0][0:1]
        roomFloorLevelStr = detail[4][0:2]
        roomFloorLevelStr =roomFloorLevelStr.strip()
        roomFloorLevel =-1
        if roomFloorLevelStr =='低':
            roomFloorLevel=1
        elif roomFloorLevelStr =='中':
            roomFloorLevel = 2
        elif roomFloorLevelStr == '高':
            roomFloorLevel = 3
        self.roomFloorLevel = roomFloorLevel
        self.year = detail[5].strip()[0:4]
        #print(detail)

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.desc + "," + \
                self.pic
