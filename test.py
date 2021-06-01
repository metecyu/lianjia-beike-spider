#!/usr/bin/env python
# coding=utf-8
# author: Zeng YueTian
# 此代码仅供学习与交流，请勿用于商业用途。
# 获得指定城市的二手房数据

from lib.spider.ershou_spider import *

if __name__ == "__main__":
    spider = ErShouSpider(SPIDER_NAME)

    spider.print_ershou_total()


    spider.get_xiaoqu_ershou_info("sh","beicai");
    ershou_list = spider.get_xiaoqu_ershou_info("sh", "c5011000002853");
    spider.get_xiaoqu_roomNum("南山雨果（公寓）",ershou_list)

    ershou_list = spider.get_xiaoqu_ershou_info("sh", "c5011000004989");
    spider.get_xiaoqu_roomNum("中金海棠苑（一期）", ershou_list)

    ershou_list = spider.get_xiaoqu_ershou_info("sh", "c5011000019832");
    spider.get_xiaoqu_roomNum("繁荣华庭", ershou_list)

    ershou_list = spider.get_xiaoqu_ershou_info("sh", "c5011000013690");
    spider.get_xiaoqu_roomNum("金杨五街坊", ershou_list)





    #print(ershou_list)


